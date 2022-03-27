from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def  __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    
    class Meta(UserCreationForm.Meta):
        #Meta도 usercreationform의 메타이기 때문
        model = get_user_model()
        fields = ['username','email','first_name','last_name']

        #form이 제출될 때, clean_field형식의 함수들이 자동으로 호출이 됨?
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if email:
                qs = User.objects.filter(email=email)
                if qs.exists():
                    raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
            return email
        
        