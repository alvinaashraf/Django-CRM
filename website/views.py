from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm ,add_record_form
from .models import Record
# Create your views here.
def home(request):
    
    # display records in table 
    record=Record.objects.all()
    
    #display records in table end 
    # check to see if user is logged in 
    if request.method == 'POST':
        username = request.POST['username']
        password=request.POST['password']
        # authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'successfully logged in ')
            return redirect('home')
        else:
            messages.success(request,'error logging in try agagin ')
            return redirect('home')
        
    else:
        return render(request,'home.html',{'record':record})




def logout_user(request):
    logout(request)
    messages.success(request,'your have been logged out ')
    return redirect('home')




def register_user(request):
    if request.method=='POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            # authenticate and login 
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,' Remember your username and password registered ')
            return redirect('home')
        
    else:
        form=RegisterForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


    
def record_detail(request,pk):
    if request.user.is_authenticated:
        cust_rec=Record.objects.get(id=pk)
        return render(request,'record_detail.html',{'cust_rec':cust_rec})
    
    else:
        messages.success(request,' user must be logged in to view ')
        return redirect('home')


def record_delete(request,pk):    
    if request.user.is_authenticated:
        delete_obj=Record.objects.get(id=pk)
        delete_obj.delete()
        messages.success(request,' YOU HAVE DELETED A USER SUCCESSFULLY ')
        return redirect('home')
    else:
        messages.success(request,' error in deleting must have done something wrong ')
        return redirect('home')

    
    
    
def add_record(request):
    form=add_record_form(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_rec=form.save()
                messages.success(request,'Record Added Successfully')
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,'Your Must be Logged In to Add a Record')
        return redirect('home')
        
    
    
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_rec=Record.objects.get(id=pk)
        form=add_record_form(request.POST or None,instance=current_rec)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Updated Successfully')
            return redirect('home')
        
        return render(request,'update_record.html',{'form':form})
    
    else:
        messages.success(request,'Your Must be Logged In to update a Record')
        return redirect('home')
        

    