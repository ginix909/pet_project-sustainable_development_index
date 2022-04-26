from django.shortcuts import render
from django.http import HttpResponse
from .models import Project_info

def get_project_info(request):
    '''представление выведет информацию по проекту, которая лжежит в БД, которая описана в models.py'''
    # project_info = Project_info
    # return HttpResponse(project_info)
    return render(request,'csa_app/evaluate_company.html')

def evaluate_company(request):
    return HttpResponse ('оцените компанию')
