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
    subjects = Subject.objects.all()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'), status=200)
    if request.user.is_superuser:
        return render(request, 'users/admin.html', {
            'subjects': subjects
        })
    else:
        return render(request, 'users/index.html')


def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.'
            })

    return render(request, 'users/login.html')


def logoutView(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'You are logged out.'
    })


def enrollCourse(request):  # user_username):

    booking = Booking.objects.filter(
        username_id=request.user.id).values_list('subject_id', flat=True)
    print(booking.query)
    subjects = Subject.objects.exclude(pk__in=booking).all()
    return render(request, 'users/enrollCourse.html', {
        'subjects': subjects,

    })


def enrollComfirm(request):
    if request.method == "POST":
        subjectID = request.POST['subject']
        subject1 = Subject.objects.filter(pk=subjectID).first()
        if subject1.quota != 0:
            print("1111", request)
            b = Booking(subject=subject1, username=request.user)
            b.save()
            subject1.quota -= 1
            subject1.save()
            return enrollCourse(request)
            # return HttpResponseRedirect(reverse('users:enroll'), status=200)
        else:
            booking = Booking.objects.filter(
                username_id=request.user.id).values_list('subject_id', flat=True)
            subjects = Subject.objects.exclude(pk__in=booking).all()
            return render(request, 'users/enrollCourse.html', {
                'subjects': subjects,
            })


def courseView(request):
    booking = Booking.objects.filter(username_id=request.user.id).all()
    return render(request, 'users/myCourse.html', {
        'booking': booking,
    })
    pass


def cancelCourse(request):
    if request.method == "POST":
        subjectID = request.POST['subject']
        booking = Booking.objects.filter(
            username_id=request.user.id, subject_id=subjectID).all()
        print(booking)
        if booking.count() > 0:
            booking.first().delete()
            subject1 = Subject.objects.filter(pk=subjectID).first()
            subject1.quota += 1
            subject1.save()
            return HttpResponseRedirect(reverse('users:myCourse'))
        else:
            allBooking = Booking.objects.filter(
                username_id=request.user.id).all()
            return render(request, 'users/myCourse.html', {
                'booking': allBooking,
                'message': 'Can\'t cancle not exist booking'
            })


def courseEdition(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    if request.user.is_superuser:
        return render(request, 'users/courseEdition.html')
