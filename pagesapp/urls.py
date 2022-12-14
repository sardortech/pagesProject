from django.urls import path
from.views import HomePageView, AboutPageView, ContactPageView, NewsPageView

urlpatterns = [
    path('news/', NewsPageView.as_view(), name='news'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(),name='home'),
]