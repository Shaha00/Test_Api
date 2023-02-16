from django.contrib import admin
from doctor.models import Doctor, Record, Review
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Record)
admin.site.register(Review)

