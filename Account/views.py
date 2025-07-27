from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from Account.forms import LoginUserForm, RegisterUserForm

# Create your views here.

def user_login(request):

    if request.user.is_authenticated and 'next' in request.GET:
        return render(request, 'account/login.html', {
            'error': 'Yetkiniz bulunmamaktadır.'
        })

    if request.method == 'POST':

        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Giriş başarılı.')
                nextUrl = request.GET.get('next', None)

                if nextUrl is None:
                    return redirect('index')
                else:
                    return redirect(nextUrl)

            else:
                return render(request, 'account/login.html', {
                    'form': form,
                })
            
        else:
                return render(request, 'account/login.html', {
                    'form': form,
                })
        
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html', {
            'form': form
        })


def user_register(request):

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
        
        else:
            return render(request, 'account/register.html', {
                'form': form,
            })
    
    else:
        form = RegisterUserForm()
        return render(request, 'account/register.html', {
            'form': form
        })


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Çıkış başarılı.')
    return redirect('index')

