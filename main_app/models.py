from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    profession = models.CharField(max_length=50)
    description = models.TextField()
    phone_number = models.CharField(max_length=50, default='')
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    #
    def __str__(self):
        return f'User ({self.id}): {self.user.username} {self.phone_number}'


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Pais ({self.id}): {self.name}'


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    index = models.IntegerField(default=0)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Departamentos ({self.id}): {self.name} {self.index}'


class City(models.Model):
    id = models.AutoField(primary_key=True)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Ciudades ({self.id}): {self.name} {self.id_status}'


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    aditional_address = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Domicilio ({self.id_user}): {self.address} {self.aditional_address} {self.id_status}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'Categoria ({self.id}): {self.name} {self.id_status}'


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    id_status = models.BooleanField(default=True)

    def __str__(self):
        return f'SubCategoria ({self.id}): {self.name} {self.id_status}'


class Ratings(models.Model):
    id = models.AutoField(primary_key=True)
    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Calificacion ({self.id}): {self.id_profile} {self.id_status}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')


class ClientMessages(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()
    id_status = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Message Client ({self.id}): {self.user.username}'

    def formatted_date_created(self):
        return self.date_created.strftime('%Y-%B-%d %H:%M:%S')
