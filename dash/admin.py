from django.contrib import admin
from .models import ActiveCase,SampleDetail,QuarantineAddress


#set council branding
admin.site.site_title = "Covid19 Dashboard"
admin.site.site_header = 'Covid19 Dashboard'
admin.site.index_title = "Edit Dashboard"


# Register your models here.
admin.site.register(ActiveCase)
admin.site.register(SampleDetail)

@admin.register(QuarantineAddress)
class QuarantineAddressAdmin(admin.ModelAdmin):
    list_display = ("name","reason")
