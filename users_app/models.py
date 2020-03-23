from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='User profile'
    )
    e_mail_field = models.EmailField(
        max_length=300,
        verbose_name='E-mail',
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=13,
        verbose_name='Phone number'
    )

    def __str__(self):
        return f'{self.user.username} {self.user.email}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        