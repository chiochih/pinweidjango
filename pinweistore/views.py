from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')



# def index(request):
#     context = {
#         'title': '首頁'
#     }
#     return render(request, 'myapp/my.html', context)


