from django import forms
from captcha.fields import CaptchaField
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(label="帳號", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label="驗證碼")



    
# class ContactForm(forms.Form):
#     CITY = [
#         ['TP', 'Taipei'],
#         ['TY', 'Taoyuan'],
#         ['TC', 'Taichung'],
#         ['TN', 'Tainan'],
#         ['KS', 'Kaohsiung'],
#         ['NA', 'Others'],
#     ]

#     user_name = forms.CharField(label='姓名', max_length=20, initial='小明')
#     user_city = forms.ChoiceField(label='居住城市', choices=CITY)
#     user_school = forms.BooleanField(label='是否在學', required=False)
#     user_email = forms.EmailField(label='電子郵件')
#     user_message = forms.CharField(label='訊息內容', widget=forms.Textarea)

# class PostForm(forms.ModelForm):
#     captcha = CaptchaField()
#     class Meta:
#         model = models.Post
#         fields = ['mood', 'nickname', 'del_pass', 'message']
#         labels = {
#             'mood': '心情',
#             'nickname': '暱稱',
#             'del_pass': '密碼',
#             'message': '訊息',
#         }
#         widgets = {
#             'message': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
#         }
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['captcha'].label = '驗證碼'