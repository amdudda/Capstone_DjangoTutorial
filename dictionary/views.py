from django.shortcuts import render
# importing as SD saves us a bunch of keystrokes as we write our code
from .models import Somali_German_Dictionary as SD

# Create your views here.

def index(request):
    all_words = SD.objects.all().order_by('-somali', '-German')
    context = {'dictionary': all_words }
    return render(request,'dictionary/index.html',context)

def search(request):
    # initialize variables
    search_for = request.POST['searchfor']
    language = request.POST['language']
    result_set = []
    # get our search results
    if language=='english': result_set = SD.objects.filter(english=search_for)
    elif language=='somali': result_set = SD.objects.filter(somali=search_for)
    elif language=='German': result_set = result_set = SD.objects.filter(German=search_for)
    # send the results to index.html
    context = {'dictionary':result_set}
    return render(request,'dictionary/index.html',context)