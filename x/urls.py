from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.xlistview, name='post1'),
    path('add/', views.xaddview, name='x_add'),
    path('edit/<int:x_id>/', views.xedit, name='x_edit'),
    path('delete/<int:x_id>/', views.xdelete, name='x_delete'),
    path('like/<int:x_id>/', views.xlikeadd, name='x_like'),
    path('unlike/<int:x_id>/', views.xlikesubtract, name='x_unlike'),
]
