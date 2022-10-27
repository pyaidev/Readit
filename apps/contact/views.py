from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


