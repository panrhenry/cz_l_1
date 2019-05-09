from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from student.views import indexview

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', indexview.as_view(), name='index')  # as_view() 是对get和post方法的包装，及判断method方法类型
]
