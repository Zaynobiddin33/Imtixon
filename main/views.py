from django.shortcuts import render
from .models import *

# Create your views here.


#asosiy sahifa
def main(request):
    if request.method == 'POST':
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        date = request.POST["date"]
        time = request.POST["time"]
        print(request.POST['time'])
        people = request.POST["people"]
        message = request.POST["message"]
        BookTable.objects.create(
            name = name,
            phone = phone,
            email = email,
            date = date,
            time = time,
            people = people,
            message = message
        )
    context = {
        'cheffs' : Cheff.objects.all(),
        'images' : Gallery.objects.all()
    }
    return render(request, 'index.html', context)

# "Bog'lanish" sahifasi
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['text']
        Contact.objects.create(
            name = name,
            phone = phone,
            email = email,
            text = text
        )
    return render(request, 'contact.html')

#Blog sahifasi
def blog(request):
    context = {
        'parties': Party.objects.all(),
        'cheffs' : Cheff.objects.all(),
        'images' : Gallery.objects.all()
    }
    return render(request, 'blog.html', context)

#Xizmatlar sahifasi
def service(request):
    context = {
        'foods' : Food.objects.all()
    }
    return render(request, 'service.html', context)
