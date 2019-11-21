from django.contrib import admin
from django.urls import path, include
import main.views
import introduction.views
import community.urls
import community.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 시작 페이지
    path('', introduction.views.intro, name="intro"),
    path('register/', main.views.register, name="register"),
    # 메인 페이지
    path('locally/', main.views.index, name="index"),
    # 커뮤니티
    path('community/', include(community.urls)),
    path('summernote/', include('django_summernote.urls')),
    # 소셜 로그인
    path('accounts/', include('allauth.urls')),
]
