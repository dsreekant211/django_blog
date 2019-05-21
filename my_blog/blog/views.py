from django.shortcuts import render
from django.template import Context, Template



def home(request):
	posts = [
	{
	'author': 'sreekanth',
	'title': 'blog post1',
	'content': 'my first content',
	'date_posted': '21 may 2019'
	},
	{
	'author': 'sravanthi',
	'title': 'blog post2',
	'content': 'second content',
	'date_posted': '20 may 2019'
	}
]
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def posts(request):
	return render(request, 'blog/about.html')

