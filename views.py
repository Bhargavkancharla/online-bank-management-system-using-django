from django.shortcuts import render,redirect
from .models import Bank
from django.http import HttpResponse

# Create your views here.
def loginpage(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':
        uname=request.POST['uname']
        pswd=request.POST['pwd']
        obj=Bank.objects.filter(email=uname,pwd=pswd).first()
        msg='please enter the correct user details'
        if obj:
            return redirect('operationurl',obj.id)
        else:
            return render(request,'login.html',{'message':msg})

def registerpage(request):
    if request.method=='GET':
        return render(request,'register.html')
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        pno=int(request.POST['phone'])
        adh=int(request.POST['addhar'])
        eml=request.POST['email']
        d=request.POST['dob']
        balance=int(request.POST['mbalance'])
        pic=request.POST['pic']
        paswd=request.POST['pwd']
        obj=Bank.objects.create(fname=fn,lname=ln,phone=pno,addhar=adh,email=eml,dob=d,mbalance=balance,photo=pic,pwd=paswd)
        return redirect('loginurl')
    
def operation(request,no):
    if request.method=='GET':
        return render(request,'operations.html',{'user_id':no})
    
def balance(request,no):
    if request.method=='GET':
        obj=Bank.objects.get(id=no)
        return render(request,'balance.html',{'balance':obj.mbalance,'user_id':no})
    

def withdraw(request,no):
    if request.method=='GET':
        return render(request,'withdraw.html',{'user_id':no})
    if request.method=='POST':
        amount=int(request.POST['amount'])
        obj=Bank.objects.get(id=no)
        if amount<=obj.mbalance:
            if amount>0:
                obj.mbalance=obj.mbalance-amount
                obj.save()
                msg='Amount withdraw successfully'
                return render(request,'withdraw.html',{'message':msg,'user_id':no})
            else:
                msg='Negitive Amount is not Allowed'
                return render(request,'withdraw.html',{'message':msg,'user_id':no})
        else:
            msg='Your Account does not have suffiecent amount to withdraw'
            return render(request,'withdraw.html',{'message':msg,'user_id':no})
        

def deposit(request,no):
    if request.method=='GET':
        return render(request,'deposit.html',{'user_id':no})
    if request.method=='POST':
        amount=int(request.POST['amount'])
        obj=Bank.objects.get(id=no)
        if amount>0:
            obj.mbalance=obj.mbalance+amount
            obj.save()
            msg='Amount deposit successfully'
            return render(request,'deposit.html',{'message':msg,'user_id':no})
        else:
            msg='Negitive amount is not allowed'
            return render(request,'deposit.html',{'message':msg,'user_id':no})
def details(request,no):
    if request.method=='GET':
        obj=Bank.objects.get(id=no)
        fn=obj.fname
        ln=obj.lname
        pn=obj.phone
        ad=obj.addhar
        am=obj.mbalance
        p=obj.photo
        return render(request,'details.html',{'fn':fn,'ln':ln,'pn':pn,'ad':ad,'am':am,'p':p,'user_id':no})

    


