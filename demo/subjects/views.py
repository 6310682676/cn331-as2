from django.shortcuts import render

from subjects.models import Subject

# Create your views here.

def index(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/index.html' ,{
        'subjects' : subjects
    })

def subject(request, subject_id):
    subject =Subject.objects.filter(pk=subject_id).first()
    return render(request,'subjects/subject.html', {
        'subject': subject
    })