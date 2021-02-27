

# Create your views here.
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')
def detail1(request):
    return render(request,'detail1.html')
def detail2(request):
    return render(request,'detail2.html')


# def index(request):
#     d = my_db.objects.all()
#     return render(request,'index')