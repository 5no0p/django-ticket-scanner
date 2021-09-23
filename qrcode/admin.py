from django.contrib import admin
from qrcode.models import QRcodeGenerator

class QRcodeGeneratorAdmin(admin.ModelAdmin):
    pass

admin.site.register(QRcodeGenerator, QRcodeGeneratorAdmin)