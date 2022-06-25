from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task

# Create your views here.
@login_required(login_url='loginpage')
def home(request):
    if request.method == 'POST':
        # print(request.POST)
        questions=Task.objects.all()
        score = 0
        wrong = 0
        attended = 0
        correct = 0
        total = 0
        for q in questions:
            total+=1
            # print(request.POST.get(q.Question))
            # print(q.Correct_ans)
            if request.POST.get(q.Question):
                attended+=1
                if q.Correct_ans ==  request.POST.get(q.Question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
            
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'attended':attended,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions = Task.objects.all()
        context = {'questions':questions}
        return render (request,'home.html',context)

def loginPage(request):
    if request.method=='POST':
        email = request.POST.get('email')
        user_exist = User.objects.filter(email=email)
        if user_exist:
            username = User.objects.get(email=email).username
            password = request.POST.get('password')
            user = authenticate(request,username=username ,password =password)
            # print(password,email,user)
            if user is not None:
                login(request,user)
                if user.groups.filter(name='admin').exists():
                    return redirect('/admin')
                else:
                    return redirect('/home')
            else:
                messages.info(request,'Invalid credentials')
        else:
            messages.info(request,'mail id not exist')
    context = {}
    return render(request,'index.html',context)

@login_required(login_url='loginpage')
def logoutUser(request):
    logout(request)
    return redirect('/')