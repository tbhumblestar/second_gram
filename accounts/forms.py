from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def  __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #print(self.field['email'].required)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    
    class Meta(UserCreationForm.Meta):
        #Meta도 usercreationform의 메타이기 때문
        model = get_user_model()
        #model도 직접적으로 설정을 해줘야 함. auth에 있는 모델에 의존하고 있기 때문
        fields = ['username','email','first_name','last_name']

        #form이 제출될 때, clean_field형식의 함수들이 자동으로 호출이 됨? 
        #답변 form.cleaned_data는 유효성 검사가 시작되는 시점에 빈 사전으로 초기화가 되며, 유효성 검사 과정에서 각 필드에 대한 값들이 업데이트됨
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email
        
        