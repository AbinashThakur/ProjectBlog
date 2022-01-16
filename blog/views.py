from django.shortcuts import render, redirect
from django.http import HttpResponse, response
import json, datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from blog.models import * 

@api_view(['GET','POST'])
def index(request):
    if request.method == 'POST':
        
        username = request.POST['uname']
        password = request.POST['psw']
        
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                request.session['username'] = username
            
            return redirect('/blog/')
        else:
            print("No permission")
            return Response({'Error_Msg':'User not authorized'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('/blog/')

@api_view(['GET','POST'])
def create_post(request):
    if request.method == 'POST':
        
        title = request.POST['ptitle']
        content = request.POST['pcontent']

        if title == None or content == None:
            return Response({'Error_Msg':'Channel Name or Channel Type cannot be blank'}, status=status.HTTP_400_BAD_REQUEST)

        new_Blogpost = Blogpost(
                posttitle=title,
                postcontent=content,
                author=request.session.get('username'),
                publishedon = datetime.datetime.now(),
                deleted=0
            )
        new_Blogpost.save()
        return redirect('/blog/')
        
        # return Response({"Success_Msg", "Successfull"}, status=status.HTTP_200_OK)
    else:
        return render(request, 'post_create.html')

@api_view(['GET','POST'])
def edit_post(request):
    if request.method == 'GET':
        
        postid = request.GET['id']
        
        get_post = list(Blogpost.objects.filter(id=postid, deleted=0).values())
        
        return render(request, 'post_edit.html', {"data": get_post})
    else:
        postid = request.POST['id']
        title = request.POST['ptitle']
        content = request.POST['pcontent']
        
        edit_post = Blogpost.objects.get(id=postid)
        edit_post.posttitle = title
        edit_post.postcontent = content
        edit_post.author = request.session.get('username')
        edit_post.updatedon = datetime.datetime.now()
        edit_post.save()
        
        return redirect('/blog/')

@api_view(['GET','POST'])
def view_post(request):
    if request.method == 'GET':
        
        postid = request.GET['id']
        
        get_post = list(Blogpost.objects.filter(id=postid, deleted=0).values())
        
        return render(request, 'post_view.html', {"data": get_post})


@api_view(['GET'])
def dashboard(request):
    if request.method == 'GET':
        response_Blogpost = list(Blogpost.objects.filter(deleted=0).values().order_by('-id'))

        return render(request, 'dashboard.html', {"data": response_Blogpost})
    else:
        return Response({'Error_Msg':'This is a POST method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','POST'])
def delete_post(request):
    if request.method == 'GET':
        
        postid = request.GET['id']
        
        del_post = Blogpost.objects.get(id=postid)
        del_post.deleted = 1
        del_post.save()

        return redirect('/blog/')
    else:
        return Response({'Error_Msg':'This is a GET method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
