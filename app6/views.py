
from django.shortcuts import redirect, render
from .models import Student,Warden,Gatepasses,Messcut,Grievances,Suggestion
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login

from django.shortcuts import render, get_object_or_404
from .models import Room
from django.http import JsonResponse

from django.shortcuts import render

from django.contrib.auth import logout


import razorpay
from .models import mess

from django.utils import timezone


# from .forms import FeedbackForm
# Create your views here.

def frontpage(request):
    return render(request,'Frontpage.html')

def home(request):
    return render(request,'Home.html')

def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'Contact.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email_id = request.POST['email_id']
        mob_no = request.POST['mob_no']
        password= request.POST['password']
        dob= request.POST['dob']
        confirm_password = request.POST['confirm_password']
        
        if confirm_password == password:
             if User.objects.filter(username=username).exists():
                  dic={'user':"username already exists"}
                  return render(request,'Register.html',dic)
             
             elif User.objects.filter(email=email_id).exists():
                  dic={'user':"email already exists"}
                  return render(request,'Register.html',dic)
             
             else:
                new_entry = User.objects.create_user(username=username,email=email_id,password=password)
                new_entry.save()
                



                stud= Student(users=new_entry,fname=fname,lname=lname,email=email_id,mob_no=mob_no,date_of_birth=dob,password=password,stud_id=username)
                stud.save()

                dic={'login':"Registered successfully"}

                return render(request,'Login.html',dic)
             

        
        else:
             
             dic={'user':"Password mismatched"}
             return render(request,'Register.html',dic)
        
    return render(request,'Register.html')

        
def ulogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        try:
            a=Student.objects.get(users=user)
        except:
            a=None

        if a is not None:
            auth.login(request,user)
            
            return redirect(studentpage)
        else:

            dic={'login':"Invalid Login"}
            return render(request,'Login.html',dic)

    return render(request,'Login.html')




def success(request):
    return render(request,'success.html')

def wardenreg(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email_id = request.POST['email_id']
        mob_no = request.POST['mob_no']
        password= request.POST['password']
        dob= request.POST['dob']
        confirm_password = request.POST['confirm_password']
        
        if confirm_password == password:
             if User.objects.filter(username=username).exists():
                  dic={'user':"username already exists"}
                  return render(request,'Wardenreg.html',dic)
             
             elif User.objects.filter(email=email_id).exists():
                  dic={'user':"email already exists"}
                  return render(request,'Wardenreg.html',dic)
             
             else:
                new_entry = User.objects.create_user(username=username,email=email_id,password=password)
                new_entry.save() 

                

                warden= Warden(users=new_entry,fname=fname,lname=lname,email=email_id,mob_no=mob_no,date_of_birth=dob,password=password,warden_id=username)
                warden.save()

                dic={'login':"Registered successfully"}

                return render(request,'Wardenlogin.html',dic)
             
        else:
             
             dic={'user':"Password mismatched"}
             return render(request,'Wardenreg.html',dic)
        
    return render(request,'Wardenreg.html')



def wardenlogin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        try:
            a=Warden.objects.get(users=user)
        except:
            a=None

        if a is not None:
            auth.login(request,user)
            return redirect(wardenpage)
        
        else:
            dic={'login':"Invalid Login"}
            return render(request,'Wardenlogin.html',dic)

    return render(request,'Wardenlogin.html')

    
    

def studentpage(request):
    user=request.user         #user table username
    name=Student.objects.get(users=user)   #student table username      
    Name=name.fname
    Lname=name.lname
    dic={'log':Name,'log1':Lname}
    return render(request,'Studentpage.html',dic)



def wardenpage(request):
    user=request.user         
    name=Warden.objects.get(users=user)        
    Name=name.fname
    Lname=name.lname
    dic={'log':Name,'log1':Lname}
    return render(request,'Wardenpage.html',dic)


def sgatepass(request):
    return render(request,'Sgatepass.html')



def sgprequest(request):
     

     user=request.user
     s=Student.objects.get(users=user)
     ids=s.id
     if request.method == 'POST':
        dateout = request.POST['date']
        timeout = request.POST['time']
        reason = request.POST['reason']
        
        
        gate_entry = Gatepasses(date_out=dateout,
                              time_out=timeout,
                              reason=reason,
                              time_in=None,
                              date_in=None,
                              users_id=ids,
                              fname=s.fname,
                              lname=s.lname,
                              stud_id=s.stud_id,
                              warden_approve=''

                              )
        gate_entry.save()
        return redirect(sgpdisplay)
            

     return render(request,'Sgprequest.html')



def sgpdisplay(request):

    user=request.user
    stud=Student.objects.get(users=user)
    Id=stud.id
    s=Gatepasses.objects.filter(users_id=Id).all()

    dic={'st':s}


    return render(request,'Sgpdisplay.html',dic)



def sgpin(request):

    user=request.user
    stud=Student.objects.get(users=user)
    Id=stud.id
    s=Gatepasses.objects.filter(users_id=Id).filter(warden_approve=1).all()

    dic={'st':s}

    return render(request,'Sgpin.html',dic)

def gatepassin(request,gi):

    a=Gatepasses.objects.filter(id=gi).all()

    dic={'key':a}

    if request.method=="POST":
        datein=request.POST['date']
        timein=request.POST['time']

        Gatepasses.objects.filter(id=gi).update(date_in=datein)
        Gatepasses.objects.filter(id=gi).update(time_in=timein)
        return redirect(sgatepass)

    return render(request,'Student/Gatepassin.html',dic)



def viewsgatepass(request):
    return render(request,'Warden/viewgatepass.html')

def newgatereq(request):
    new=Gatepasses.objects.filter(warden_approve='').all()
    dic={'new':new}
    return render(request,'Warden/Newgatereq.html',dic)


def accepted(request):
    new=Gatepasses.objects.filter(warden_approve='1').all()
    dic={'new':new}
    return render(request,'Warden/Accepted.html',dic)

def rejected(request):
    new=Gatepasses.objects.filter(warden_approve='0').all()
    dic={'new':new}
    return render(request,'Warden/Rejected.html',dic)


def view(request,wk):
    vari=Gatepasses.objects.get(id=wk)
    dic={'var':vari}
    if request.method=='POST':
        v=request.POST['c']
        if v=='1':
            warden=Gatepasses.objects.filter(id=wk).update(warden_approve=1)
            return redirect(viewsgatepass)
        else:
            warden=Gatepasses.objects.filter(id=wk).update(warden_approve=0)
            return redirect(viewsgatepass)

    return render(request,'Warden/View1.html',dic)

 
def notification(request):
    return render(request,'Notification.html')

# def menu(request):
#     return render(request,'Menu.html')

def attendance(request):
    names = Student.objects.all().values('fname')
    context={'names': names}
    return render(request,'Attendance.html',context)

def rooms(request):
    return render(request,'p.html')

def feedback_form(request):
    return render(request,'feedback_form.html')

def viewmesscut(request):
    return render(request,'viewmesscut.html')


#tessa-g
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if room.vacancy>0:
        return render(request, 'room_detail.html', {'room': room})
    else:
        return render(request, 'noroom.html')

def make_payment(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST' and room.vacancy > 0:
        room.vacancy -= 1
        room.save()
        return render(request,'payment1.html')
    # return JsonResponse({'success': False})
#

def slogout(request):
    logout(request)
    return redirect(frontpage)

#rose
def vmess_cut(request):
    return render(request,'viewmess_cut.html')

def vnewmessreq(request):
    new=Messcut.objects.filter(warden_approve='').all()
    dic1={'mnew':new}
    return render(request,'vnewmessreq.html',dic1)


def maccepted(request):
    new=Messcut.objects.filter(warden_approve='1').all()
    dic1={'mnew':new}
    return render(request,'messaccept.html',dic1)

def mrejected(request):
    new=Messcut.objects.filter(warden_approve='0').all()
    dic1={'mnew':new}
    return render(request,'messreject.html',dic1)


def mview(request,id):
   
    vari=Messcut.objects.get(id=id)
    dic1={'var':vari}
    if request.method=='POST':
        v=request.POST['c']
        if v=='1':
            warden=Messcut.objects.filter(id=id).update(warden_approve=1)
            return redirect(vmess_cut)
        else:
            warden=Messcut.objects.filter(id=id).update(warden_approve=0)
            return redirect(vmess_cut)
    return render(request,'View2.html',dic1)
    


def smess_cut_main(request):

        return render(request,'smess_cut_main.html')

def smess_cutr(request):
     
     return render(request,'smess_cutr.html')
def smess_action(request):

     user=request.user
     s=Student.objects.get(users=user)
     ids=s.id
     if request.method == 'POST':
        datefrom = request.POST['date_from']
        dateto = request.POST['date_to']
        reason = request.POST['reason']
        
        
        mess_cut = Messcut(date_from=datefrom,
                              date_to=dateto,
                              reason=reason,
                              
                              users_id=ids,
                              fname=s.fname,

                              lname=s.lname,
                              stud_id=s.stud_id,
                              warden_approve=''
                              )
        mess_cut.save()
        return redirect(smess_cutd)



def smess_cutd(request):

    user=request.user
    stud=Student.objects.get(users=user)
    Id=stud.id
    s=Messcut.objects.filter(users_id=Id).all()

    dic1={'st1':s}
    return render(request,'smess_cutd.html',dic1)

#


#tesse-t


def payment1(request):
     payment=None
     if request.method=="POST":
         Name=request.POST.get("Name")
         amount=int(request.POST.get("amount"))*100
         client = razorpay.Client(auth=("rzp_test_AeXSXmPhh29704", "mTmhEZM0exYSkgzzUgtQaSVx"))

         DATA = {
              "amount": amount,
              "currency": "INR",
              "receipt": "receipt#1",
              "notes": 
              {
                   "key1": "value3",
                   "key2": "value2"
              }
                 }
         payment=client.order.create(data=DATA)
        
         print(payment)
         Mess=mess(name=Name,amount=amount,payment_id=payment['id'])
         Mess.save()
     return render(request,"index.html",{'payment':payment})

def success1(request):
     if request.method== "POST":
         a=request.POST
         print(a)
     return render(request,"success1.html")


#tessa-t

#rose

def grievance(request):
    if request.method == 'POST':
        room = request.POST['room']
        complaint = request.POST['complaint']
       
   
        current_time = timezone.now()

        grievance = Grievances.objects.create(
            room_no=room,
            complaint=complaint,
            time_in=current_time
           
              # Assign the logged-in user
        )
        grievance.save()

        return redirect('grievance')

    return render(request, 'grievance.html')


def grievance_list(request):
    grievances = Grievances.objects.all()
    return render(request, 'grievance_list.html', {'grievances': grievances})









# def save_checkbox_values(request):
    # Get the checkbox values from the request.
   #  status= request.POST.getlist('status')
#    if request.method == 'POST':
#         checkbox = Attendance.objects.get(id=request.POST['id']) if 'id' in request.POST else None
#         checkbox.status = request.POST['status']
#         checkbox.save()
#    return render(request, 'attendance.html')



# def feedback_form(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return render(request, 'form/thanks.html')
#     else:
#         form = FeedbackForm()
#     return render(request, 'form/feedback_form.html', {'form': form})

def menu(request):
   if request.method == 'POST':
       sugg = request.POST['sugg']
       suggestion = Suggestion.objects.create(
           sugg=sugg
        
         
             # Assign the logged-in user
       )
       suggestion.save()


       return redirect('menu')
   return render(request, 'Menu.html')




def suggestion_list(request):
   suggestions = Suggestion.objects.all()
   return render(request, 'suggestion_list.html', {'suggestions': suggestions})


















