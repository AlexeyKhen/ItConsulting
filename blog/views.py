from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import PostForm, FilterForm
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(author=self.request.user).order_by("-created")
        return None

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=None, **kwargs)
        context['form'] = FilterForm
        return context


class AllPosts(ListView):
    model = Post
    template_name = 'allposts.html'


class DetailViewPost(DetailView):
    model = Post
    template_name = 'detailView.html'


class CreateViewPost(CreateView):
    form_class = PostForm
    success_url = reverse_lazy('home')
    template_name = 'create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super().form_valid(form)


class DeletePost(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('home')


class PostUpdate(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = PostForm
    success_url = reverse_lazy('home')


def exportPdf(request):
    first_data = f"{request.GET['first_data_year']}-{request.GET['first_data_month']}-{request.GET['first_data_day']} 00:00:00"
    second_data = f"{request.GET['second_data_year']}-{request.GET['second_data_month']}-{request.GET['second_data_day']} 23:59:59"
    object_list = Post.objects.filter(created__range=[first_data, second_data]).filter(author=request.GET['user'])

    if object_list.exists():
        template_path = 'exportpdf.html'
        context = {'object_list': object_list}
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="report.pdf"'
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    context = {"message": "Постов в данном промежутке, от данного пользователь нет. Попробуйте выбрать другую дату"}
    return render(request, 'exportpdf.html', context)
