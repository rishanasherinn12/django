from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,UserModel,BookData
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password,check_password
from .forms import Bookform
from django.views.decorators.cache import never_cache




from .models import Products

# Create your views here.
def index(request):
    products=Products.objects.all()
    return render(request,'index.html',{'products':products})
def about(request):
    return HttpResponse("<h2>about page</h2>")


@never_cache
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
   
        if password1 != password2:
            messages.error(request,'password do not match!')
            return redirect('signup')

        elif UserModel.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')  
            return redirect('signup')
        elif UserModel.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('signup')   
            
        else:
            hashed_pass = make_password(password1)
            user = UserModel.objects.create(username = username,email = email, password = hashed_pass,)
            request.session['username'] = user.username
            user.save()
            
            messages.success(request, 'Account created successfully!')
            return redirect('book')

    return render(request, 'signup.html')


@never_cache
def loginpage(request):
    if request.session.get('username'):
        return redirect('book')

    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        if UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.get(username=username)
            if check_password(password1,user.password):
                request.session['username'] = user.username
                return redirect('book')
            else:
                messages.error(request, 'Password didnt match')
        else:
            messages.error(request, 'user name didnt match')
        
    return render(request,'loginpage.html')



@never_cache
def book(request):   
    if 'username' not in request.session:
        messages.warning (request, 'you must log in first!')
        return redirect('login')
    Book_Data = BookData.objects.all()
    return render(request, 'bookhome.html', {'books': Book_Data})



def add_book(request):
    if 'username' not in request.session:
        messages.warning (request, 'you must log in first!')
        return redirect('login')
    if request.POST:
        Bform = Bookform(request.POST, request.FILES)
        if Bform.is_valid():
            Bform.save()
        return redirect('book')
    else:
        Bform = Bookform()
    return render(request, 'add_book.html', {'Bform': Bform})




def Delete(request, pk):
    instance = BookData.objects.get(pk=pk)
    instance.delete()
    return redirect('book')
    


def Editbook(request, pk):
    instance = BookData.objects.get(pk=pk)
    if request.method == 'POST':      
        Bform = Bookform(request.POST, instance=instance)
        if Bform.is_valid():
            Bform.save()
        return redirect('book')
    else:
        Bform = Bookform(instance=instance)
    return render(request, 'add_book.html', {'Bform': Bform})



def members(request):
    if 'username' not in request.session:
        messages.warning (request, 'you must log in first!')
        return redirect('login')
    members_list = UserModel.objects.all()  # fetch all users
    return render(request, 'members.html', {'members': members_list})


def contacts(request):
    if 'username' not in request.session:
        messages.warning (request, 'you must log in first!')
        return redirect('login')
    return render(request, 'contacts.html')

@never_cache
def logout(request):
    request.session.flush()
    messages.success(request,'You have been logout successfully')
    return redirect('login')
