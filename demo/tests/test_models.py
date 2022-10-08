from django.test import TestCase
from subjects.models import Subject


class SubjectTestCase(TestCase):

    def setUp(self):

        Subject.objects.create(subjectCode="EX111",
                               subjectName="Example111",
                               semester=1,
                               year=2565,
                               quota=1,
                               status=True,
                               detail="For example",)

    def test_quota_available(self):

        subject = Subject.objects.first()
        self.assertTrue(subject.is_quota_available())

    def test_quota_not_aviailable(self):
        subject = Subject.objects.first()
        subject.quota -= 1
        self.assertFalse(subject.is_quota_available())
