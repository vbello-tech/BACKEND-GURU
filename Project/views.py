from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import *
from django.core.exceptions import PermissionDenied
from .models import *
from django.urls import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, "base.html")

#Create project
class CreateProjectView(CreateView, LoginRequiredMixin):
    model = Project
    template_name = 'Projects/createproject.html'
    form_class = CreateProjectForm
    login_url = 'account_login'
    success_url = reverse_lazy('challenge:home_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Render all projects to frontend
class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "Projects/projectlist.html"

    def get_queryset(self):
        return Project.objects.order_by('-posted_date')

class ProjectDetailView(View):
    def get(self, request, slug, name, *args, **kwargs):
        project = Project.objects.get(slug=slug, project_name=name)
        form = ReviewForm(request.POST)
        context = {
            'project': project,
            'form':form,
        }
        return render(request, 'Projects/projectdetail.html', context)

    def post(self, request, slug, name, *rgs, **kwargs):
        project = Project.objects.get(slug=slug, project_name=name)
        form = ReviewForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid:
                review = form.save(commit=False)
                review.post = project
                review.author = request.user
                review.save()
                return redirect(project.get_url())
            else:
                return redirect(project.get_url())

def delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        project.delete()
        return redirect(project.get_url())

    context = {
        'project': project
    }
    return render(request, 'Projects/delete.html', context)
