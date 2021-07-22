from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import Account, Address
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail as sm
from django.contrib import messages
import uuid
from django.shortcuts import render, get_object_or_404

from django.conf import settings
from .models import Token, Product,Cart,Customers,Orderplaces
import datetime
now = datetime.datetime.now()
epxt=datetime.datetime.now()+ + datetime.timedelta(days=5)
from django.contrib.auth.decorators import login_required
# Create your views here.


def send_email_registration(email, token):
    subject="Verify email"
    message=f'Hi click on link to varify your account http://127.0.0.1:8000/refile/{token}'
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    sm(subject,
                message,
               'gmail',
                [email],
                fail_silently=False)






def logoutreg(request):
    logout(request)
    return redirect('index')
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        passd=""
        usererror = ""
        vry=""
        if User.objects.filter(username=username).exists():
            usererror = ""
            p=User.objects.get(username=username)
            if p.is_active==False:
                vry="Account is not varify"
        else:
            usererror = "User name not exit"
        context = {
            
            "vry":vry,
            "usererror": usererror,
            "passd": passd,
            "formerror": ""
        }
        if usererror != "":
            return render(request, "login.html",context)
        # below line will validate credentials and store the returned data of the user
        user = auth.authenticate(request, username=username, password=password)
        
        # based on returned value user get logged .
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Signed in successfully")
            return redirect('index')
        else:
            passd="Password is not correct"
            context = {
            "usererror": usererror,
            "vry":vry,
            "passd": passd,
            "formerror": ""
            }
           
            return render(request, "login.html",context)

    else:
        return render(request, "login.html")


     

def registion(request):
    if request.method=='POST':
        reg=Account(request.POST)
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        emailerror=""
        usererror=""
        if User.objects.filter(username=username).exists():
            usererror = "Username already exists"
        else:
            usererror = ""
        if User.objects.filter(email=email).exists():
            emailerror = "Email already exists"
            
        else:
            emailerror = ""
        context = {
            "form": reg,
            "emailerror": emailerror,
            "usererror": usererror,
            "formerror": ""
        }
        if emailerror != "" or usererror != "":
            return render(request, 'register.html', context)
        if reg.is_valid():
            user=User.objects.create_user(username=username,email=email,password=password)
           
            user.is_active=False
            user.save()

            uid=uuid.uuid4()
            toke=Token(user=user,token=uid)
            toke.save()
            send_email_registration(user.email , uid)
            print(uid)
            messages.success(request,"Your Account Create Successful, to Varify Your Account Check your Email")
            return redirect('verify')
        else:
            reg=Account()
            return render(request,'register.html',{'form':reg})
    else:
        reg=Account()
        return render(request,'register.html',{"form": reg})

    

def refile(request,token):
    pf=Token.objects.get(token=token)
    if pf is not None:
        d=User.objects.get(username=pf.user)
    
        d.is_active=True
        d.save()
        print(d)
    
        messages.success(request,"Your Account Create Successful, Your Account is varifily")
        return redirect('index')
        
    return redirect('index')

def forget(request):

    
    return render(request,"forget.html")

def order(request,strgs):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST['pro_id']
            print(id)
            cart=Customers.objects.filter(user=request.user)
            if cart.exists():
                product=Product.objects.get(pk=id)
                cart=Customers.objects.get(user=request.user)
                return render(request,"order.html",{'product':product,'cart':cart})
            else:
                return redirect('profile')
        else:
             return redirect('index')
    else:
        return redirect('login')

def ordershow(request):
    if request.user.is_authenticated:
        order=Orderplaces.objects.filter(user=request.user)
        return render(request,'ordershow.html',{'order':order})
    else:
        return redirect('login')

def trak(request,strgs):
    if request.user.is_authenticated:
        if request.method=='POST':
            id=request.POST['pro_id']
            id2=request.POST['pro_id2']
            product=Product.objects.get(pk=id)
            cus=Customers.objects.get(pk=id2)

            Orderplaces(user=request.user,product=product,costomer=cus,quantity=1,date=now, exp=epxt,deliver='Confirmed').save()

            return render(request,"trak.html")

def profile(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Customers.objects.filter(user=user)
        if cart.exists():
            cart=Customers.objects.get(user=user)
            return render(request,"profile.html",{'cart':cart})
        else:
            return render(request,"profile.html",  )
    else:
        return redirect('login')



def edit(request):
    return render(request,"edit.html")

def verify(request):
    return render(request,"varify.html")



def display(request,strg):
    if request.method=='POST':
        id=request.POST['pro_id']
        print(id)
        product=Product.objects.get(pk=id)
        return render(request,"display.html",{'product':product} )
    else:
        return redirect('index')

def card(request,strgs):
    if request.method=='POST':
        if request.user.is_authenticated:
            id=request.POST['pro_id']
            user=request.user
            product=Product.objects.get(pk=id)
            Cart(user=user,product=product,quantily=1).save()

            return redirect('/product/')
        else:
            return redirect('/login/')
def cardwoman(request,strgs):
    if request.method=='POST':
        if request.user.is_authenticated:
            id=request.POST['pro_id']
            user=request.user
            product=Product.objects.get(pk=id)
            Cart(user=user,product=product,quantily=1).save()

            return redirect('/woman/')
        else:
            return redirect('/login/')

def cardkid(request,strgs):
    if request.method=='POST':
        if request.user.is_authenticated:
            id=request.POST['pro_id']
            user=request.user
            product=Product.objects.get(pk=id)
            Cart(user=user,product=product,quantily=1).save()

            return redirect('/kid/')
        else:
            return redirect('/login/')
def cardElect(request,strgs):
    if request.method=='POST':
        if request.user.is_authenticated:
            id=request.POST['pro_id']
            user=request.user
            product=Product.objects.get(pk=id)
            Cart(user=user,product=product,quantily=1).save()

            return redirect('elect')
        else:
            return redirect('/login/')
            

def Show_card(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        return render(request,"card.html", {"cart":cart})
    else:
        return redirect('login')


def product(request):
    pro=Product.objects.filter(gender='M')
    return render(request,"product.html",{'pro':pro})

def Women(request):
    pro=Product.objects.filter(gender='F')
    return render(request,"women.html",{'pro':pro})

def Kid(request):
    pro=Product.objects.filter(gender='K')
    return render(request,"kid.html",{'pro':pro})

def Electroic(request):
    pro=Product.objects.filter(gender='E')
    return render(request,"elect.html",{'pro':pro})

def Add(request):
    if request.user.is_authenticated:
        
        if request.method=='POST':
            user=request.user
            reg=Address(request.POST)
            name=request.POST['name']
            phone=request.POST['phone']
            locality=request.POST['locality']
            city=request.POST['city']
            state=request.POST['state']
            pincode=request.POST['pincode']
            if reg.is_valid:
                Customers(user=user,name=name,phone=phone,locality=locality,city=city,state=state,pincode=pincode).save()
                return render(request,'address.html',{'form':reg})
            else:
                return render(request,'address.html',{'form':reg})
            
        else:

            reg=Address()
            return render(request,'address.html',{'form':reg})

def update(request,pk):
    instance=get_object_or_404(Customers,id=pk)
    if request.method=='POST':
        
        
        reg=Address(request.POST or None,instance)
        name=request.POST['name']
        phone=request.POST['phone']
        locality=request.POST['locality']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        if reg.is_valid:
            reg.save()
            pi=Customers.objects.get(pk=pk)
            messages.success(request, "Signed in successfully")
            Customers(user=request.user,name=name,phone=phone,locality=locality,city=city,state=state,pincode=pincode).save()
            return redirect('order')
        else:
            return render(request,'adress.html', {'form':reg} )
    else:
        reg=Address(request.POST)
        return render(request,'adress.html', {'form':reg} )

def cart_delete(request,id):
    if request.method=='POST':
        print(id) 
        item = Cart.objects.get(pk=id)
        item.delete()
        return redirect('/showcart/')


def fwoman(request,strgs):
    pro=Product.objects.filter(gender='F', coteg=strgs)
   
    return render(request,"women.html",{'pro':pro})


def fman(request,strgs):
    pro=Product.objects.filter(gender='M', coteg=strgs)
   
    return render(request,"product.html",{'pro':pro})


def fkidd(request,strgs):
    pro=Product.objects.filter(gender='K', coteg=strgs)
   
    return render(request,"kid.html",{'pro':pro})


def fElect(request,strgs):
    pro=Product.objects.filter(gender='E', coteg=strgs)
   
    return render(request,"elect.html",{'pro':pro})
