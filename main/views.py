from django.shortcuts import render
from user.models import User
from company.models import Company


def index(response):
    users = User.objects.all()
    companies = Company.objects.all()

    return render(response, 'main/base.html', {
        'users': users, 
        'companies': companies
    })
