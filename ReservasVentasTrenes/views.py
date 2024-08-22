from django.shortcuts import render

def pageHome(request):
    return render(request, 'base.html')

