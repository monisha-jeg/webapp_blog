from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Post
from django.template import loader
from .models import Post
from django.core.urlresolvers import reverse

# Create your views here.
def loginto(request):
	return render(request, 'blog/login.html', {})


def logindone(request):
	print("LOOL")
	try:
		user=authenticate(username=request.POST['username'], password=request.POST['password'])
		if user:
			login(request, user)
			post_list=user.post_set.all()
			return render(request, 'blog/feed.html', {"post_list" : post_list, "user_id" : user.id})
		else:
			return render(request, 'blog/login.html', {"err_mess" : "INVALID DETAILS"})
	except KeyError:	
		return render(request, 'blog/login.html', {"err_mess" : "PLEASE LOGIN"})

def profile(request, user_id):
	user=User.objects.get(id=user_id)
	if request.user.is_authenticated():		
		post_list=user.post_set.all()
		return render(request, 'blog/profile.html', {"user" : user, "post_list" : post_list})
	else:
		return render(request, 'blog/login.html', {})


def register(request):
	return render(request, 'blog/register.html', {})

def logouto(request):
	logout(request)
	return render(request, 'blog/login.html', {"err_mess" : "LOGGED OUT"})


def process(request):
	if User.objects.filter(username=request.POST['username']).exists():
		return render(request, 'blog/register.html', {"err_mess" : "USERNAME ALREADY EXISTS"})
	else:
		user= User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
		user.first_name=request.POST['fname']
		user.last_name=request.POST['lname']
		user.save()
		return render(request, 'blog/process.html', {})

def addpost(request, user_id):
	return render(request, 'blog/addpost.html', {"user_id" : user_id })

def savepost(request, user_id):
	user=User.objects.get(id=user_id)
	p=Post(author=user, post_text=request.POST['newpost'])
	p.save()
	post_list=user.post_set.all()
	return redirect('/blog/' + user_id + '/profile/')


def deletepost(request, user_id, post_id):
	p = Post.objects.get(id=post_id)
	p.delete()
	return redirect('/blog/' + user_id + '/profile/')
	

def feed(request,user_id):
	post_list=Post.objects.all()
	return render(request, 'blog/feed.html', {"user_id" : user_id, "post_list" : post_list })




