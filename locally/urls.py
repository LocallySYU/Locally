from django.contrib import admin
from django.urls import path
import main.views
import introduction.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name="index"),
    path('introductions/', introduction.views.intro, name="intro"),
    path('register/', main.views.register, name="register"),

]
