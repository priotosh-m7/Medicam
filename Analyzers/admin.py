from django.contrib import admin

# Register your models here.
from .models import UploadImage,UploadChestImage,UploadKidneyImage

admin.site.register(UploadImage)
admin.site.register(UploadChestImage)
admin.site.register(UploadKidneyImage)