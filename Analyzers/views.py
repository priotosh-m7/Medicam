# from django.shortcuts import render
import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm,UploadChestImageForm,UploadKidneyImageForm
from .models import *
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import keras
import random


def brainTumor(request):
    model_o = load_model('C:\\Medicam\\cnn_models\\IEEE-model-28.h5')
    submitted = False
    imagename = ""
    result = []
    p_image = ""
    i = ""
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            yup = ['10000']
            form.user.join(yup)
            user = form.cleaned_data['user']
            i = form.cleaned_data['image']
            submitted = True
            ing = "images/" + str(i)
            form.save()

            p_image = UploadImage.objects.get(user=user)
            from keras.utils import load_img
            import tensorflow
            import cv2

            img = tensorflow.keras.preprocessing.image.load_img("C:\\Medicam" + p_image.image.url,
                                                                target_size=(150, 150))
            img.save('C:\\Medicam\\static\\braintumor' + p_image.image.url)
            # denoising

            import warnings
            import numpy as np
            warnings.filterwarnings('ignore')
            test_image = tensorflow.keras.preprocessing.image.img_to_array(img)
            test_image = test_image / 255
            test_image = np.expand_dims(test_image, axis=0)
            result = model_o.predict(test_image)
            result = np.argmax(result, axis=1)
        # if result[0][0] > 0:
        #     imagename += "Non-Melanoma/ Normal "
        # else:
        #     imagename += "Melanoma / Anomaly Detected"

        else:
            form = UploadImageForm
            if 'submitted' in request.GET:
                submitted = True

    form = UploadImageForm
    # p_image = UploadImage.objects.get(user=user)
    context = p_image

    # load model
    no = datetime.datetime.now().timestamp()
    return render(request, 'brain_tumor_upload.html',
                  {'form': form, 'submitted': submitted, 'context': p_image, 'result': result, 'no': no,
                   'imagename': imagename, 'i': i})

# Create your views here.


def chestXray(request):
    model_o = load_model('C:\\Medicam\\cnn_models\\chest_pneumonia_model_95.h5')
    submitted = False
    imagename = ""
    result = []
    p_image = ""
    i = ""
    if request.method == "POST":
        form = UploadChestImageForm(request.POST, request.FILES)

        if form.is_valid():


            user = form.cleaned_data['user']
            #i = form.cleaned_data['image']
            submitted = True
            #ing = "images/" + str(i)
            form.save()

            p_image = UploadChestImage.objects.get(user=user)
            from keras.utils import load_img
            import tensorflow
            import cv2

            img = tensorflow.keras.preprocessing.image.load_img("C:\\Medicam" + p_image.image.url,
                                                                target_size=(200, 200))
            img.save('C:\\Medicam\\static' + p_image.image.url)
            # denoising

            import warnings
            import numpy as np
            warnings.filterwarnings('ignore')
            test_image = tensorflow.keras.preprocessing.image.img_to_array(img)
            test_image = test_image / 255
            test_image = np.expand_dims(test_image, axis=0)
            result = model_o.predict(test_image)
            #result = np.argmax(result, axis=1)
        # if result[0][0] > 0:
        #     imagename += "Non-Melanoma/ Normal "
        # else:
        #     imagename += "Melanoma / Anomaly Detected"

        else:
            form = UploadChestImageForm
            if 'submitted' in request.GET:
                submitted = True

    form = UploadChestImageForm
    # p_image = UploadImage.objects.get(user=user)
    context = p_image

    # load model
    no = datetime.datetime.now().timestamp()
    return render(request, 'chest_xray_upload.html',
                  {'form': form, 'submitted': submitted, 'context': p_image, 'result': result, 'no': no,
                   'imagename': imagename, 'i': i})

def kidneyScans(request):
    model_o = load_model('C:\\Medicam\\cnn_models\\model_kidney_class.h5')
    submitted = False
    imagename = ""
    result = []
    p_image = ""
    i = ""
    if request.method == "POST":
        form = UploadKidneyImageForm(request.POST, request.FILES)

        if form.is_valid():


            user = form.cleaned_data['user']
            #i = form.cleaned_data['image']
            submitted = True
            #ing = "images/" + str(i)
            form.save()

            p_image = UploadKidneyImage.objects.get(user=user)
            from keras.utils import load_img
            import tensorflow
            import cv2

            img = tensorflow.keras.preprocessing.image.load_img("C:\\Medicam" + p_image.image.url,
                                                                target_size=(180,180))
            img.save('C:\\Medicam\\static' + p_image.image.url)
            # denoising

            import warnings
            import numpy as np
            warnings.filterwarnings('ignore')
            test_image = tensorflow.keras.preprocessing.image.img_to_array(img)
            test_image = test_image / 255
            test_image = np.expand_dims(test_image, axis=0)
            result = model_o.predict(test_image)

            result = np.argmax(result)
        # if result[0][0] > 0:
        #     imagename += "Non-Melanoma/ Normal "
        # else:
        #     imagename += "Melanoma / Anomaly Detected"

        else:
            form = UploadKidneyImageForm
            if 'submitted' in request.GET:
                submitted = True

    form = UploadKidneyImageForm
    # p_image = UploadImage.objects.get(user=user)
    context = p_image

    # load model
    no = datetime.datetime.now().timestamp()
    return render(request, 'kidney_upload.html',
                  {'form': form, 'submitted': submitted, 'context': p_image, 'result': result, 'no': no,
                   'imagename': imagename, 'i': i})
