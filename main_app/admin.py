from django.contrib import admin
from .models import Profile, Country, Department, \
                    City, Home, Category, SubCategory, Ratings, ClientMessages

# Register your models here.
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(Home)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Ratings)
admin.site.register(ClientMessages)

