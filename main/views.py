from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user.models import User
from company.models import Company
from .forms import SignupForm


@login_required
def index(request):
    user = User.objects.get(id=request.user.id)
    company = Company.objects.get(user=user)

    return render(request, 'main/base.html', {
        'company': user, 
        'company': company
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    return render(request, 'main/signup.html', {'form': form})
