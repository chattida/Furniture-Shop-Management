from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import Account, Owner, Employee


def my_login(request):
    context = {}

    # Check already login
    if request.user.is_authenticated:
        return redirect('index')

    # Get detail in form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Success
        if user:
            login(request, user)

            # Redirect
            next_url = request.POST.get('next_url')
            if next_url != '':
                return redirect(next_url)
            else:
                return redirect('index')

        # Fail
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'บัญชีผู้ใช้ หรือ รหัสผ่านผิด!'

    # Get url path
    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='Account/login.html', context=context)


@login_required
@permission_required('Account.add_employee')
def register(request):
    context = {}
    # Get detail in form
    if (request.method == 'POST'):
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        acc_type = request.POST.get('type')

        context = {
            'fname': first_name,
            'lname': last_name,
            'email': email,
            'username': username,
            'password': password,
            'phone': phone
        }

        # Check already used
        if (User.objects.filter(username=username).exists()):
            context['error'] = 'Username is already used!'
            return render(request, 'Account/register.html', context=context)
        elif (User.objects.filter(email=email).exists()):
            context['error'] = 'Email is already used!'
            return render(request, 'Account/register.html', context=context)

        # Add user to DB
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        account = Account(
            user=User.objects.get(username=username),
            phone=phone
        )
        account.save()

        context2 = {
            'fname': first_name,
            'lname': last_name,
            'email': email,
            'username': username
        }

        if acc_type != 'owner':
            employee = Employee(
                user=User.objects.get(username=username),
                owner_id=Owner.objects.get(user_id=request.user.id),
                department=request.POST.get('department')
            )
            if acc_type == 'po':
                employee.employee_type = 'PO'
                user.groups.add(Group.objects.get(name='Purchasing_Officer'))
                context2['type'] = 'Purchasing Officer'
            elif acc_type == 'so':
                employee.employee_type = 'SO'
                user.groups.add(Group.objects.get(name='Sale_Officer'))
                context2['type'] = 'Sale Officer'
            employee.save()

        else:
            owner = Owner(
                user=User.objects.get(username=username),
                shop_name=request.POST.get('shop_name')
            )
            owner.save()
            user.groups.add(Group.objects.get(name='Owner'))
            context2['type'] = 'Owner'

        return render(request, template_name='Main/index.html', context=context2)

    return render(request, template_name='Account/register.html', context=context)


@login_required
def my_logout(request):
    logout(request)
    return redirect('login')


@login_required
def change_password(request):
    user = request.user
    context = {}
    context['username'] = user.username

    # Get detail in form
    if request.method == 'POST':
        password1 = request.POST.get('npass1')
        password2 = request.POST.get('npass2')

        # Check password matching
        if password1 != password2:
            context['error'] = 'Password not match!'
            return render(request, template_name='Account/change_password.html', context=context)

        # Set password to DB
        user.set_password(password1)
        user.save()
        logout(request)
        return redirect('login')

    return render(request, template_name='Account/change_password.html', context=context)
