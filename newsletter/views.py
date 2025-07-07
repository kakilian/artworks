from django.shortcuts import render, redirect
from .forms import SubscriberForm

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsletter:thank_you')
    return redirect('home')
    
def thank_you(request):
    return render(request, 'newsletter/thank_you.html')