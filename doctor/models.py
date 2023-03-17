from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    datetime = models.DateField(verbose_name='Дата рождения')
    post = models.CharField(max_length=50, verbose_name='Должность', null=True)
    education = models.TextField(null=True,verbose_name='Образование')
    experience = models.IntegerField(verbose_name='Стаж работы')

    class Meta:
        verbose_name = "Информация о докторе"
        verbose_name_plural = "Добавить доктора"

    def __str__(self):
        return self.name
    

class Service(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    names = models.CharField(max_length=50, null=True, verbose_name='Названия отделов')

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.names

class Record(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, verbose_name="Ваш номер телефона")
    date = models.DateTimeField(verbose_name="Назначить Дату и Время Приема")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Выбрать Услугу", null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Выбрать Врача")

    class Meta:
        verbose_name = "Запись на Прием"
        verbose_name_plural = "Запись на прием"

    def __str__(self):
        return self.phone_number

   

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Автор")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, verbose_name="Выберите доктора")
    text = models.TextField(max_length=255, verbose_name="Tекст")
    created_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.created_date

   