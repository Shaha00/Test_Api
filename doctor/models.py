from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Doctor(models.Model):
    image = models.ImageField(default='photo_2023-03-18_20-43-19.jpg')
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
    phone_number = PhoneNumberField(max_length=13, default='+996', verbose_name="Номер телефона")
    date = models.DateTimeField(verbose_name="Назначить Дату и Время Приема")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Выбрать Услугу", null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Выбрать Врача")

    class Meta:
        verbose_name = "Запись на Прием"
        verbose_name_plural = "Запись на прием"

    

   

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Автор")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, verbose_name="Выберите доктора", related_name='doctor_reviews')
    text = models.TextField(max_length=255, verbose_name="Tекст")
    created_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    # def __str__(self):
    #     return self.created_date

   