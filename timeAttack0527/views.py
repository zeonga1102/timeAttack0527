from django.shortcuts import render

def showIndex(request):
    if request.method == 'GET':
        return render(request, 'index.html')