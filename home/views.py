from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def indexView(request):
    return render(request, 'home/index.html', {})

@login_required
def secureView(request):
    return render(request, 'home/index_s.html', {})
