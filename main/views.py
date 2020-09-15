from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
import csv
from random import randint


#이메일 인증 관련 (SMTP)
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

# 썸네일 이미지 관련
from bs4 import BeautifulSoup
import requests

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
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error' : '이미 사용중인 아이디입니다.'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1'],
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    email = request.POST['email_address']
                )
                userprofile = Userprofile()
                userprofile.user = user
                userprofile.job = request.POST['job']
                userprofile.date_of_birth = request.POST['date_of_birth']
                
                user.is_active = False
                user.save()
                userprofile.save()

                current_site = get_current_site(request)
                message = render_to_string('activation_email.html', {
                    'user' : user,
                    'domain' : current_site.domain,
                    'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                    'token' : account_activation_token.make_token(user),
                })
                mail_title = "siteforsites@gmail.com"
                mail_to = request.POST['email_address']
                email = EmailMessage(mail_title, message, to=[mail_to])
                email.send()

                return render(request, 'login.html')
        else:
            return render(request, 'signup.html', {'error' : '비밀번호가 일치하지 않습니다.'})    
            
    return render(request, 'signup.html')

# 메인페이지 (추천 사이트 출력)
def main(request):
    if request.method == "POST":
        keyword = request.POST["searchbar"]
        result = []
        for site in Site.objects.filter(title__contains=keyword):
            result.append(site)
        for site in Site.objects.filter(description__contains=keyword):
            result.append(site)
        result = list(set(result))
        return render(request, 'result.html', {'result' : result, 'keyword' : keyword})
    return render(request, 'main.html')

def result(request):
    return render(request, 'result.html')

# 로그아웃 구현
def logout(request):
    auth.logout(request)
    return redirect('/')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('main')
    else:
        return render(request, 'main.html', {'error' : '계정 활성화 오류'})


def db(request):
    CSV_PATH = './sitedata.csv'
    with open(CSV_PATH, newline='', encoding='euc-kr') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            site = Site()
            site.description = row['description']
            site.title = row['title']
            site.tag = row['tag']
            site.url = row['url']
            url = site.url
            req = requests.get(url, verify=False, allow_redirects=False)
            soup = BeautifulSoup(req.text, 'html.parser')
            try:
                thumbnail = soup.find('meta', {'property':'og:image'})['content']
                site.thumbnail = thumbnail
            except TypeError:
                # 기본 이미지 (임시로 넣음)
                site.thumbnail = 'https://s.pstatic.net/static/www/mobile/edit/2016/0705/mobile_212852414260.png'            
            
            site.save()

    return redirect('main')
