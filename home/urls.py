from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import HomePage, product_detail_single_page


app_name = 'pages'
urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('<slug:slug>/', views.product_detail_single_page, name='product_detail_page_single'),

    # path('<slug:slug>/', PagesView.as_view(), name='single_page'),
]
