from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .models import *
import random
from django.conf import settings
from django.core.mail import send_mail
#from django_email_verification import send_email

# Create your views here.

def send_otp(number, otp):
    from twilio.rest import Client

    account_sid = 'AC4eb065101d67c8b96b29879b03b70a16'
    auth_token = '44357165973b9a8df29f7bf04bebdc72'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body='You have Successfully Registered in Organic Veges '
             'Your Otp is'+otp,
        from_='+14847200081',
        to ='+91'+number,

    )

    print(message.sid)

def register(request):
    if request.method == 'POST':

        uname = request.POST['Username']
        number = request.POST['number']
        password = request.POST['Password1']

        if User.objects.filter(username=uname).exists():

            context = {'message': 'Username already exist', 'class': 'danger'}
            return render(request, 'register.html', context)
        else:
            check_profile = Mobile.objects.filter(phonenumber=number).first()
            if check_profile:
                context = {'message': 'Number already exist', 'class': 'danger'}
                return render(request, 'register.html', context)
            else:
                user = User.objects.create_user(username=uname, password=password)

                phone_number = Mobile(user=user, phonenumber=number)
                # user.is_active = False  # Example
                # send_email(user)
                phone_number.save();
                otp = str(random.randint(1000, 9999))
                profile = Profile(user=user, mobile=number, otp=otp)
                user.save();
                profile.save();
                send_otp(number, otp)
                request.session['mobile'] = number
                return redirect('otp')

                print('user_created')
                return redirect('login')
    else:
        return render(request, 'Register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invaild credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(otp=otp)
        if profile:
            return redirect('login')
        else:
            print('Wrong')

            context = {'message': 'Wrong OTP', 'class': 'danger', 'mobile': mobile}
            return render(request, 'otp.html', context)

    return render(request, 'otp.html', context)