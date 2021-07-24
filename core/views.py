from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from job.models import Job
from user_profile.models import UserProfile


def front_page(request):
    jobs = Job.objects.all()

    return render(request, 'core/frontpage.html', {'jobs': jobs})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account_type = request.POST.get('account_type', 'jobseeker')
            if account_type == 'employer':
                userprofile = UserProfile.objects.create(user=user, is_employer=True)
                userprofile.save()
            else:
                userprofile = UserProfile.objects.create(user=user)
                userprofile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

