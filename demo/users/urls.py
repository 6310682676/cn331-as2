from django.urls import path

import subjects

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('enrollCourse', views.enrollCourse, name='enroll'),
    path('myCourse', views.courseView, name='myCourse'),
    path('enrollComfirm', views.enrollConfirm, name='enrollConfirm'),
    path('enrollCancel', views.cancelCourse, name='cancelCourse'),
    path('subjectlist', subjects.views.index, name='subjectsList'),
    path('courseEdition', views.courseEdition, name='courseEdition')
]
