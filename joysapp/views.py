from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
blogposts = [
    {
        'title':'My First Blog Post',
        'content':'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'date_posted':'03.11.2014',
        'authour':'John Deo',
        'category':' Travel, Nature, Business',
    },
    {
        'title':'Sample Blog Post 2',
        'content':'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'date_posted':'03.11.2014',
        'authour':'Mary Jane',
        'category':' Travel, Nature, Business',

    }
    
]

def homepage(request):
    context = {
        'title': 'Welcome to our home page',
        'pagetitle':'Adaugo\'s blog',
        'home':'active',
        'posts':blogposts
    }
    return render(request, 'joysapp/index.html', context)
    # return HttpResponse('<h1>Home Page</h1>')

def aboutpage(request):
    context = {
        'title': 'Welcome to our About page',
        'pagetitle':'Adaugo\'s blog :: About Page',
        'about':'active',
    }
    return render(request, 'joysapp/about.html', context)