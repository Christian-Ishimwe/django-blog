from django.shortcuts import render
from django.http import HttpResponse
posts=[
    
    {
        'author': 'christian ishimwe',
        'title': 'Blog Post 1',
        'content': 'first post of my content',
        'data_posted': "August 23, 2023"
    },
    
    {
        'author': 'Manzi Eric',
        'title': 'Blog Post 2',
        'content': 'second post of my content',
        'data_posted': "August 23, 2023"
    },
    
    {
        'author': 'Iradukunda Fabrice Patience',
        'title': 'Blog Post 3',
        'content': 'Third post of my content',
        'data_posted': "August 23, 2023"
    },
]



def home(request):
    context={
        'posts': posts,
        'title': 'Home page'
    }
    return render(request, 'blog/home.html', context=context)
     
def about(request):
    context={
        "title": "About"
    }
    return render(request, "blog/about.html", context=context)
