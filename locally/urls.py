from django.contrib import admin
from django.urls import path, include
import main.views
import introduction.views
import community.urls
import community.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name="index"),
    path('introductions/', introduction.views.intro, name="intro"),
    path('register/', main.views.register, name="register"),
    path('community/', include(community.urls)),
]
