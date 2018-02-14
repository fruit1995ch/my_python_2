from django.conf.urls import url
from users import views


urlpatterns = [
    # 函数注册
    # url(r'^register$', views.register, name='register'),
    # 类视图实现注册
    url(r'^register$', views.RegisterView.as_view(), name='register')

  ]