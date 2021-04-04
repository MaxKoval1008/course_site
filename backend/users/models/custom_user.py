from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


"""создание менеджера"""


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(  # создание обычного пользователя через переприсваивание стандартного метода
            self, first_name, email, phone_number,
            last_name='', is_student=False, is_teacher=False,
            is_partner=False, password=None):

        if not email:
            raise ValueError('Email обязателен!')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=self.normalize_email(email),
            is_student=is_student,
            is_teacher=is_teacher,
            is_partner=is_partner)
        user.set.password(password)
        user.save(using=self._db)
        return user

    def create_superuser(  # создание админа через переприсваивание стандартного метода
            self, first_name, email, phone_number, password):
        user = self.create_user(
            first_name, email, phone_number, password=password,
            last_name='', is_student=False,
            is_teacher=False, is_partner=False
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


"""создание кастомного юзера через модель AbstractBaseUser с добавлением новых критериев"""


class CustomUser(AbstractBaseUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Телефон должен быть в формате: '+375(XX)XXXXXXX'")

    firstname = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    phone_number = models.CharField('Телефонный номер', max_length=100, validators=[phone_regex], unique=True)
    email = models.EmailField('Email', unique=True)
    is_student = models.BooleanField('Студент', default=False)
    is_teacher = models.BooleanField('Преподаватель', default=False)
    is_partner = models.BooleanField('Партнёр', default=False)
    is_active = models.BooleanField('Активный', default=True)
    is_staff = models.BooleanField('Сотрудник', default=False)
    is_superuser = models.BooleanField('Админ', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'last_name', 'phone_number']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'

    def get_full_name(self):
        return f'{self.firstname} {self.last_name}'

    def __str__(self):
        return self.get_full_name()
