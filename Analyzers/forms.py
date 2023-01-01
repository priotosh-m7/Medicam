from django import forms
from django.forms import ModelForm
from .models import UploadImage,UploadChestImage, UploadKidneyImage

class UploadImageForm(ModelForm):
    class Meta:
        model = UploadImage
        fields = "__all__"
        labels = {
            'user':'',
            'image':'',
        }
class UploadKidneyImageForm(ModelForm):
    class Meta:
        model = UploadKidneyImage
        fields = "__all__"
        labels = {
            'user': '',
            'image': '',
        }
class UploadChestImageForm(ModelForm):
    class Meta:
        model = UploadChestImage
        fields = "__all__"
        labels = {
            'user': '',
            'image': '',
        }
       # widgets = {
          #  'user': forms.TextInput(attrs= {'class : form-control'}),
           # 'image': forms.ImageField(attrs= {'class : form-control'}),

        #}

