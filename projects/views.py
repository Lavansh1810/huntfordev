from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.views import profiles
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import paginateProjects, searchProject
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
def projects(request):

    projects, search_query = searchProject(request)
    
    
    results = 3
    custom_range, projects = paginateProjects(request, projects, results)
    
    context = {'projects': projects, 'search_query' : search_query, 'custom_range' : custom_range}
    
    
    return render(request,'projects/projects.html', context)


def project(request, pk):
    # projectObj = None
    # for i in projectsList:
    #     if i['id'] == pk :
    #         projectObj=i
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        
        
        projectObj.getVoteCount


        messages.success(request, 'Your review was successfully submitted.')
        return redirect('project', pk=projectObj.id)
    # tags = projectObj.tags.all()
    return render(request,'projects/single-project.html',{'projectObj' : projectObj, 'form': form})

@login_required(login_url="login")
def create_project(request):
    form = ProjectForm()
    profile = request.user.profile

    if request.method == 'POST':
        # print(request.POST)
        form= ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account') 


    context = {'form' : form }
    return render(request, 'projects/project_form.html',context)

@login_required(login_url="login")
def update_project(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    form = ProjectForm(instance=project)
    if request.method == 'POST':
        # print(request.POST)
        form= ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account') 


    context = {'form' : form }
    return render(request, 'projects/project_form.html',context)

@login_required(login_url="login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if(request.method == 'POST'):
        project.delete()
        return redirect('account')
    context = {'object' : project}
    return render(request, 'delete_template.html', context)