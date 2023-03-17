from django.contrib import admin
from doctor.models import Doctor, Record, Review, Service
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Record)
admin.site.register(Review)
admin.site.register(Service)


