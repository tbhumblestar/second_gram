from django.contrib import messages
from django.shortcuts import redirect,render
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"회원가입을 환영합니다!")
            next_url = request.Get.get('next','/')
            #post메소드여도, url을 통해 들어오는 get값이 있음
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request,'accounts/signup_form.html',{
        'form':form,
    })