from django.shortcuts import render
from .forms import SubscriberForm


def subscribe(request):
    subscribed = False
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            subscribed = True
            request.session['newsletter_subscribed'] = True
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/signup.html', {
        'form': form,
        'subscribed': subscribed,
    })


def thank_you(request):
    return render(request, 'newsletter/thank_you.html')

