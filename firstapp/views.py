from django.shortcuts import render, redirect

from .models import CustomUser

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.




def signupForm_view(request):
    
    if request.method == "POST":
        
        print("Welcomm to sign up page")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        
        # Check if the user already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'User already exists. Please log in.')
            # return redirect("/login_view")      
        
        else:
            user = CustomUser.objects.create_user(username, email, password, phone_no = phone_no)
            
            print(user)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect("/dashboard_view")
            else:
                # No backend authenticated the credentials
                return redirect("/signupForm_view")

    return render(request, "signup.html")



def login_view(request):

    if request.method == "POST":
       
        print("Welcomm to login page is valid")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/dashboard_view")
        else:
            # No backend authenticated the credentials
            messages.error(request, 'User not exists. Please Sign up.')

    return render(request, "login.html")


def dashboard_view(request):
    
    return render(request, 'Dashboard.html', )


def logout_view(request):
    logout(request)
    return render(request, "dashboard.html", {})


def page(request, page_number):
    page_number = int(page_number)
    total_pages = 25  # Total number of pages
    

    user = CustomUser.objects.get(username = request.user)

    if page_number != 0:
        user.pageviews = user.pageviews + 1;
        user.total_pages = user.total_pages + 1;
        user.save()

    if page_number == 0:
        page_number = 1
        next_page_number = page_number + 1
    elif page_number < total_pages:
        next_page_number = page_number + 1 
    else:
        next_page_number = 1  # Loop back to the first page
    
    context = {
        'next_page_number': next_page_number,
        'page_number'     : page_number,
    }
    
    return render(request, f'page{page_number}.html', context)


def gifts_view(request):

    user = CustomUser.objects.get(username = request.user)
    pageviews = user.pageviews
    total_pages = user.total_pages
    rewards = "{:.2f}".format(pageviews*0.10)
    upi = user.upi

    return render(request, 'gifts.html', {'pageviews' : pageviews, 'total_pages' : total_pages, 'rewards' : rewards, 'upi' : upi})

def save_upi(request):

    upi = request.POST.get("upi_id")
    user = CustomUser.objects.get(username = request.user)
    user.upi = upi

    user.save()

    return redirect('gifts_view')

