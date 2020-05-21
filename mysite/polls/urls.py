from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
#나한테 위임한 게 있을텐데 아무것도 없으면 view.index를 불러달라.