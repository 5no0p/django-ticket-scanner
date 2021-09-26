from django.contrib import admin
from qrcode.models import QrcodeGenerator

class QrcodeGeneratorAdmin(admin.ModelAdmin):
    pass

admin.site.register(QrcodeGenerator, QrcodeGeneratorAdmin)