from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Application(models.Model):
    class Meta:
        ordering = ('-application_date',)
        permissions = [('can_approve_application',
                        'Can approve applications to be an author')]

    application_date = models.DateField(help_text='The date when the application was sent for consideration',
                                        auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='User that wants to be an author',
    )
    motivation = models.TextField(max_length=10_000, validators=[MinLengthValidator(
        100)], help_text='Why you are going to write as an author. Describe yourself and your experience')
    status = models.CharField(max_length=1, help_text='Status of the application',
                              choices=(
                                  ('a', 'Accepted'),
                                  ('r', 'Rejected'),
                                  ('w', 'Awaiting')
                              ), default='w')

    def __str__(self) -> str:
        return f'by {self.user} from {self.application_date} | {self.status}'
