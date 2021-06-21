from django.shortcuts import render

# Create your views here.
def page_not_found_view(request):
     return render(request,'web/404.html')