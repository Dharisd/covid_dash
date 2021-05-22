from django.contrib import admin
from .models import ActiveCase,SampleDetail,QuarantineAddress


# Register your models here.
admin.site.register(ActiveCase)
admin.site.register(SampleDetail)
admin.site.register(QuarantineAddress)
