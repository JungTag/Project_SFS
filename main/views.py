from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

# Create your views here.

# 홈페이지 들어가서 첫 화면
def index(request):
    return render(request, 'index.html')

# 로그인 페이지
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error' : '아이디 혹은 비밀번호가 올바르지 않습니다.'})
    
    return render(request, 'login.html')

# 회원가입 페이지
def signup(request):
    if request.method == 'POST':
        #if request.POST['username'] 
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username = request.POST['username'])
                    return render(request, 'signup.html', {'error' : '이미 사용중인 아이디입니다.'})
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username = request.POST['username'],
                        password = request.POST['password1'],
                        first_name = request.POST['first_name'],
                        last_name = request.POST['last_name']
                    )
                    return render(request, 'login.html')
            else:
                return render(request, 'signup.html', {'error' : '비밀번호가 일치하지 않습니다.'})    
                
    return render(request, 'signup.html')

# 메인페이지 (추천 사이트 출력)
def main(request):
    return render(request, 'main.html')

# 로그아웃 구현
def logout(request):
    auth.logout(request)
    return redirect('/')