from django.test import SimpleTestCase
from django.urls import reverse, resolve
from subjects.views import subject, index as indexSubject
from users.views import index, courseEdition , enrollComfirm, loginView, logoutView, enrollCourse, courseView, enrollComfirm, cancelCourse

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('users:index')
        self.assertEquals(resolve(url).func, index)

    def test_login_url_is_resolved(self):
        url = reverse('users:login')
        self.assertEquals(resolve(url).func, loginView)

    def test_logout_url_is_resolved(self):
        url = reverse('users:logout')
        self.assertEquals(resolve(url).func, logoutView)

    def test_enroll_url_is_resolved(self):
        url = reverse('users:enroll')
        self.assertEquals(resolve(url).func, enrollCourse)

    def test_myCourse_url_is_resolved(self):
        url = reverse('users:myCourse')
        self.assertEquals(resolve(url).func, courseView)

    def test_enrollComfirm_url_is_resolved(self):
        url = reverse('users:enrollComfirm')
        self.assertEquals(resolve(url).func, enrollComfirm)
    
    def test_cancelCourse_url_is_resolved(self):
        url = reverse('users:cancelCourse')
        self.assertEquals(resolve(url).func, cancelCourse)

    def test_enroll_url_is_resolved(self):
        url = reverse('users:courseEdition')
        self.assertEquals(resolve(url).func, courseEdition)

    def test_subject_url_is_resolved(self):
        url = reverse('subjects', args=['1'])
        self.assertEquals(resolve(url).func, subject)

    def test_subject_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, indexSubject)

    def test_subject_index_url_in_user_is_resolved(self):
        url = reverse('users:subjectsList')
        self.assertEquals(resolve(url).func, indexSubject)
