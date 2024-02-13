from django.shortcuts import render

def frontpage(request):
    return render(request,"blog/frontpage.html")

def traveljapansite(request):
    return render(request,"blog/traveljapansite.html")

def portfoliosite(request):
    return render(request,"blog/portfoliosite.html")
