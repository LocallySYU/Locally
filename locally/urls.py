from django.contrib import admin
from django.urls import path
import main.views
import introduction.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name="index"),
    path('introductions/', introduction.views.intro, name="intro"),
    path('register/', main.views.register, name="register"),
<<<<<<< HEAD
=======

>>>>>>> 85db969e7ae19025a3c3ec7abca75d601882eb83
]
