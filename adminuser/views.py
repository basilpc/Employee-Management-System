from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            return render(request, 'signup.html', {'error': 'All fields are required'})

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken'})

        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already registered'})

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('signin')

    return render(request, 'sign_up.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)  # Use email

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'signin.html', {'error': 'Invalid email or password'})

    return render(request, 'signin.html')

@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'profile.html', {'user': user})


@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
            return redirect('change_password')

        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect('change_password')

        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)  # Keeps the user logged in after password change

        messages.success(request, 'Your password has been updated successfully.')
        return redirect('profile')

    return render(request, 'change_password.html')