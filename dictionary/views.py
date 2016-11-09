from django.shortcuts import render
# importing as SD saves us a bunch of keystrokes as we write our code
from .models import Somali_German_Dictionary as SD

# Create your views here.

def index(request):
    all_words = SD.objects.all().order_by('-somali and -German')
    context = {'dictionary': all_words }
    return render(request,'dictionary/index.html',context)