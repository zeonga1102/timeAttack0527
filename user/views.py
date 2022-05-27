from django.shortcuts import render, HttpResponse
from .models import UserModel

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        # email = request.form['email']
        # password = request.form['password']
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        if email not in '@':
            return HttpResponse('이메일 형식 에러')

        if len(password) < 8:
            return HttpResponse('비밀번호 길이 에러')

        newUser = UserModel(email, password)
        # newUser.save()
        return HttpResponse('<script>'
                            'alert("가입 완료");'
                            'window.location.href="/index/"'
                            '</script>')
