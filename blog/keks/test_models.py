from django.core.exceptions import ValidationError
from django.test import TestCase
from blog import models


class ApplicationTestCase(TestCase):
    def setUp(self):
        self.user1 = models.User.objects.create_user(
            username='linds', password='ura123123', email='hiuhhHJhj@gmail.com')
        self.application1 = models.Application.objects.create(user=self.user1,
                                                              motivation='a' * 500, bio='the author')

    def test_fields_have_correct_max_length(self):
        bio_max_length = self.application1._meta.get_field('bio').max_length
        motivation_max_length = self.application1._meta.get_field(
            'motivation').max_length

        self.assertEqual(
            bio_max_length, models.Blogger._meta.get_field('bio').max_length)
        self.assertEqual(motivation_max_length, 10000)

        application_wrong = models.Application.objects.create(user=self.user1,
                                                              motivation='a' * 99, bio='the author')
        self.assertRaises(ValidationError, application_wrong.full_clean)

        application_right = models.Application.objects.create(user=self.user1,
                                                              motivation='a' * 100, bio='the author')
        application_right.full_clean()

    def test_has_correct_str(self):
        self.assertEqual(str(self.application1),
                         f'by {self.application1.user} from {self.application1.application_date_time.strftime("%c")} | {self.application1.get_status_display()}')

    def test_get_absolute_url(self):
        self.assertEqual(self.application1.get_absolute_url(),
                         f'/application/{self.application1.id}/')


class BloggerTestCase(TestCase):
    def setUp(self):
        self.user1 = models.User.objects.create_user(
            username='linds', password='ura123123', email='hiuhhHJhj@gmail.com')
        self.blogger1 = models.Blogger.objects.create(
            user=self.user1, bio='the author')

    def test_fields_have_correct_max_length(self):
        bio_max_length = self.blogger1._meta.get_field('bio').max_length
        self.assertEqual(bio_max_length, 1000)

    def test_has_correct_str(self):
        self.assertEqual(str(self.blogger1), self.user1.username)

    def test_get_absolute_url(self):
        self.assertEqual(self.blogger1.get_absolute_url(),
                         f'/blogger/{self.blogger1.id}/')
