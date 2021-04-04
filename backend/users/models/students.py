from django.db import models
from django.conf import settings


def upload_avatar_image_dir(instance, filename):
    return f'avatars/students/{filename.lower()}'


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='student')
    avatar = models.ImageField('Фотография', upload_to=upload_avatar_image_dir, null=True, blank=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_plural = 'Студенты'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @staticmethod
    def get_number_of_students():
        return Student.objects.count()
