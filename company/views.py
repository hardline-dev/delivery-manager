from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from user.models import User
from .models import Company
from .forms import CompanyForm


@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            Company.objects.create(name=form.cleaned_data['name'], user_id=request.user.id)

        return HttpResponseRedirect('/')
    else:
        form = CompanyForm()

    return render(request, 'company/company_create.html', {'form': form})
