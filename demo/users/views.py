from http.client import HTTPResponse
import re
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.models import Booking
from subjects.models import Subject
from subjects.views import subject

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/index.html')
    
def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', {
                'message' : 'Invalid credentials.'
            })

    return render(request, 'users/login.html')

def logoutView(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'You are logged out.'
    })

def enrollCourse(request): #user_username):
    booking = Booking.objects.filter(username_id=request.user.id).values_list('subject_id', flat=True)
    print(booking.query)
    subjects = Subject.objects.exclude(pk__in=booking).all()
    return render(request, 'users/enrollCourse.html', {
        'subjects': subjects,
        
    })

def enrollComfirm(request):
    if request.method == "POST":
        subjectID = request.POST['subject']
        subject1 = Subject.objects.filter(pk=subjectID).first()
        b = Booking(subject = subject1, username=request.user)
        b.save()
        subject1.quota -= 1
        subject1.save()
        return HttpResponseRedirect(reverse('enroll'))
    



def courseView(request):
    booking = Booking.objects.filter(username_id=request.user.id).all()
    return render(request, 'users/myCourse.html',{
        'booking': booking,
    })
    pass

def cancelCourse(request):
    if request.method == "POST":
        subjectID = request.POST['subject']
        booking = Booking.objects.filter(username_id=request.user.id, subject_id=subjectID).get()
        print(booking)
        booking.delete()
        subject1 = Subject.objects.filter(pk=subjectID).first()
        subject1.quota += 1
        subject1.save()
        return HttpResponseRedirect(reverse('myCourse'))