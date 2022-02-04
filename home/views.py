from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import SingleObjectMixin

from .models import Content, PagesModel
# from .models import Pages, Slide, Content

from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView


class HomePage(ListView):
    model = Content
    template_name = 'base.html'
    context_object_name = 'homepage'

    @staticmethod
    def all_settings():
        return Content.objects.all()


def product_detail_single_page(request, slug):
    product = get_object_or_404(PagesModel, slug=slug, available=True)
    template = product.shablon

    return render(request, template, {'product': product, 'slug': slug})



