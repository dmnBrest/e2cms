from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def indexView(request):

    # Test emails
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )

    return render(request, 'home/index.html', {})

@login_required
def secureView(request):
    return render(request, 'home/index_s.html', {})
