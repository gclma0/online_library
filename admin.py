from django.contrib import admin
from .models import Author, Book, DeliveryMan, Payment, RentProvider, RentTaker, User, Rents
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(DeliveryMan)
admin.site.register(Payment)
admin.site.register(RentProvider)
admin.site.register(RentTaker)
admin.site.register(Rents)
admin.site.register(User)