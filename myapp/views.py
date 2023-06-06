from django.shortcuts import render,redirect
from .forms import CartoonForm
from .models import cartoon,Category,contact
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

#------------------------------Home page-----------------------------------------
@login_required(login_url='login')
def home(request):
    data=cartoon.objects.all().order_by('-uploaded_on')
    return render(request,'index.html',{'data':data})

#------------------------------About Us page-----------------------------------------
@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

#------------------------------Contact us page-----------------------------------------
@login_required(login_url='login')
def contact1(request):
    if request.method =="POST":
        username =request.POST['username']
        subject =request.POST['subject']
        email =request.POST['email']
        city =request.POST['city']
        number =request.POST['number']
        a=contact.objects.create(username=username,subject=subject,email=email,city=city,number=number)
        a.save()
        if a:
                messages.success(request,'Thanks For Your Response...')
            
            
    return render(request,'contact.html')

#------------------------------Add Show page-----------------------------------------

def addshow(request):
    if request.method == 'GET':
            form = CartoonForm()
            return render (request,'addshows.html',{'form':form})
    else:
            form = CartoonForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
    return render(request,'addshows.html')

#-----------------------Sign-Up Page Here-------------------------------

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
       
        if password == confirm_password:
            
            if User.objects.filter(username=username):
                messages.error(request,'Username Already Exists...')
                return redirect('signup')
            
            elif User.objects.filter(email=email):
                messages.error(request,'Email Already Exists...')
                return redirect('signup')
            
            else:    
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'Account Created...')
                return redirect('signup')
            
        else:
            messages.error(request,'Passwords Must be Same..')
            return redirect('signup')
    else:
        return render(request,'Signup.html')
    
    
    #------------------------------Log in page-----------------------------------------
    
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is None:
            messages.error(request,'Invalid Username/ Password')
            return redirect ('login')
        else:
            auth.login(request,user)
            return redirect('home')
    else:
        return render(request,'login.html')
    
    
    return render(request,'login.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')
    
#------------------------------Genre page-----------------------------------------

@login_required(login_url='login')
def cwd(request,name):
    data = Category.objects.filter(cat__exact = name)
    for i in data:
            data2 = cartoon.objects.filter(category__exact=i.id).values('card_title','image','description')
    return render(request,'cwd.html',{"data":data2,'name':name})


#------------------------------Read More-----------------------------------------
@login_required(login_url='login')
def readmore(request,id):
    data = cartoon.objects.get(id=id)
    return render(request,'readmore.html',{'data':data})


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect("login")


def search(request):
    if request.method == "POST":
        inp = request.POST['search']
        if cartoon.objects.filter(card_title__contains = inp).exists():
            data = cartoon.objects.filter(card_title__contains = inp)
            return render(request,'index.html',{'data':data})
        else:
            messages.error(request,"No Search Results")
            return redirect('home')
    else:
        messages.error(request,"No Search Results")
        return redirect('home')
    
