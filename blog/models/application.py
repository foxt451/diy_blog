from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.conf import settings


class Application(models.Model):
    class Meta:
        ordering = ('-application_date_time',)
        permissions = [('can_approve_application',
                        'Can approve applications to be an author')]

    application_date_time = models.DateTimeField(help_text='When the application was sent for consideration',
                                        auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text='User that wants to be an author',
    )
    motivation = models.TextField(max_length=10_000, validators=[MinLengthValidator(
        100)], help_text='Why you are going to write as an author. Describe yourself and your experience')
    
    bio = models.TextField(max_length=1_000, help_text='Your biography')
    
    status = models.CharField(max_length=1, help_text='Status of the application',
                              choices=(
                                  ('a', 'Accepted'),
                                  ('r', 'Rejected'),
                                  ('w', 'Awaiting')
                              ), default='w')
    
    comment = models.TextField(max_length=2000, help_text='The comment on why the application got this status', blank=True, default='')

    def __str__(self) -> str:
        return f'by {self.user} from {self.application_date_time.strftime("%c")} | {self.get_status_display()}'
    
    def get_absolute_url(self):
        return reverse('blog:application-detail', kwargs={'pk': self.id})
    
