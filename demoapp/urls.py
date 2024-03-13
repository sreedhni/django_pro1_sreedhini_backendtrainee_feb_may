from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("first/view/",views.FirstView.as_view()),
    path("second/view/",views.my_view)

]
