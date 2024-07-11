from django.shortcuts import render

# Create your views here.


def home_view(request):
    
    context = {"home_page_title":"DJ Unchained"}
    return render(request,"a_posts/home.html", context=context)