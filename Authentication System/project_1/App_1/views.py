from django.shortcuts import render, HttpResponse
from django.contrib import messages
from datetime import datetime
from App_1.models import Contact, Signup
from django.contrib import messages

# Create your views here.
#hemil
#marcos3435
def index(request):
    if request.method == "POST":
        signupemail = request.POST.get('signupemail')
        signuppassword = request.POST.get('signuppassword')
        signup = Signup(signupemail=signupemail,signuppassword=signuppassword)
        signup.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'index.html')

 

    
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("about")
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,subject=subject,message=message,date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse("contact")



