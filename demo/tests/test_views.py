import imp
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from users.models import Account, Booking
from subjects.models import Subject
import json
from django.contrib.auth.models import User

# class testViews(TestCase):
#     def test_user_index(self):
#         client = Client()
#         response = client.get(reverse('users:index'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/index.html')


class UserViewTestCase(TestCase):
    def setUp(self):
        # create subjucts
        self.c = Client()
        subject1 = Subject.objects.create(subjectCode="EX111",
                                          subjectName="Example111",
                                          semester=1,
                                          year=2565,
                                          quota=1,
                                          status=True,
                                          detail="For example",)

        student1 = User.objects.create_user(username="AAA", password="111")

        student2 = User.objects.create_user(username="BBB", password="111")


    def test_index_view_status_code(self):
        login = self.client.login(username="AAA", password="111")
        client = Client()

        self.assertTrue(login)
        response = client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_enroll_view_status(self):
        login = self.client.login(username="AAA", password="111")
        client = Client()
        response = client.get(reverse('users:enroll'))
        self.assertEqual(response.status_code, 200)

    def test_enrollConfirm_view_status(self):
        #self.user = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="AAA", password="111")
        client = Client()
        subject = Subject.objects.first()
        response = self.client.post(reverse('users:enrollComfirm'), {
                                    'subject': subject.pk})
        self.assertEqual(response.status_code, 200)

    def test_myCourse_view_status(self):
        login = self.client.login(username="AAA", password="111")
        client = Client()
        response = client.get(reverse('users:myCourse'))
        self.assertEqual(response.status_code, 200)

    def test_cannot_book_quota_zero(self):
        subject1 = Subject.objects.create(subjectCode="EX123",
                                          subjectName="Example123",
                                          semester=1,
                                          year=2565,
                                          quota=0,
                                          status=True,
                                          detail="For example",)
        student3 = User.objects.create_user(username="CCC", password="111")

        booking = Booking.objects.create(subject=subject1, username=student3)

        login = self.client.login(username="AAA", password="111")

        response = self.client.post(reverse('users:enrollComfirm'), {
            'subject': subject1.pk})
        count = Booking.objects.all().count()

        self.assertEqual(count, 1)

    def test_cancle_course(self):
        student3 = User.objects.create_user(username="CCC", password="111")
        login = self.client.login(username="CCC", password="111")
        subject = Subject.objects.first()
        booking = Booking.objects.create(subject=subject, username=student3)
        response = self.client.post(reverse('users:cancelCourse'), {'subject': subject.pk})
        self.assertEqual(response.status_code, 302)


    def test_subject_detail_views_status(self):
        response = self.client.get(reverse('subjects', args=['1']))
        self.assertEqual(response.status_code, 200)

    def test_subject_index_views_status(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_cancle_booking_not_exist(self):
        login = self.client.login(username="AAA", password="111")
        subject = Subject.objects.first()
        response = self.client.post(reverse('users:cancelCourse'), {'subject' : subject.pk})
        self.assertEqual(response.status_code, 200)

