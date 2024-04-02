from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
import requests
from django.core.paginator import Paginator
from home.models import Cate
# My api key : https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=38a42abb&app_key=0fa04e73e9d36c55e40a1f91393750d5


# OpenAI CHATBOT
from openai import OpenAI
import openai



API_KEY = '0fa04e73e9d36c55e40a1f91393750d5'
API_ID = '38a42abb'
global results
# Create your views here.
def index(request):
    url = f'https://api.adzuna.com/v1/api/jobs/in/search/1?app_id={API_ID}&app_key={API_KEY}&results_per_page=100'
    response = requests.get(url)
    data = response.json()

    results = data['results'] 

    # for pagination
    paginator = Paginator(results,12)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)
    totalpage = jobs.paginator.num_pages
    
    context = {
        'results':jobs,
        'lastpage':totalpage,
        'totalPagelist': [n+1 for n in range(totalpage)],
    }
    if request.user.is_authenticated:
        return render(request, 'index.html', context)
    else:
        return render(request, 'firstpage.html')
def submitform(request):
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('pass')
            global user
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('first')
        else:
            return render(request, 'index.html')
def firstpage(request):
    if request.method == "POST":
        if request.POST.get('password1')==request.POST.get('password2'):
            username = request.POST.get('username')
            password = request.POST.get('password1')        
            try:
                saveuser = User.objects.create_user(username, password)
                saveuser.set_password(password)
                saveuser.save()
                messages.success(request, "Account created successfully")
                return redirect('first')
            except IntegrityError:
                messages.success(request, 'Username already exists!')
                return render(request, 'firstpage.html',)
        else:
            return render(request, 'firstpage.html',)
    else:
        return render(request, 'firstpage.html')
def logoutUser(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, 'You have been successfully logged out')
        return redirect('first')
def about(request):
    return render(request, 'about.html')
def resume(request):
    return render(request, 'resume.html')
def resume_main(request):
    return render(request, 'resume-main.html')
def resume_main1(request):
    return render(request, 'resume-main2.html')
def jobs(request):
    return render(request, 'jobs.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')
def resources(request):
    return render(request, 'resources.html')
def questions(request):
    return render(request, 'questions.html')
def mock(request):
    return render(request, 'mock.html')
def handbooks(request):
    return render(request, 'handbooks.html')
def react(request):
    return render(request, 'index1.html')

def country(request):
    country = request.GET.get('country')
    url = f'https://api.adzuna.com/v1/api/jobs/{country}/search/1?app_id={API_ID}&app_key={API_KEY}&results_per_page=100'
    response = requests.get(url)
    data = response.json()
    results = data['results']
    params = {'results' : results}
    return render(request, 'country.html', params)
def category(request):
    category = request.GET['category']
    if len(category)>78:
        results = Cate.objects.none()
    else:
        resultsRole = Cate.objects.filter(role__icontains = category)
        resultsLocation = Cate.objects.filter(location__icontains = category)
        results = resultsRole.union(resultsLocation)
    if results.count() == 0:
        messages.error(request, "please fill the form correctly")
    params = {'results':results, 'category': category}
    return render(request, 'category.html', params)