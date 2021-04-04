from django.urls import path

from .views import CustomUserCreateView, CustomUserListView

app_name = 'users'

urlpatterns = [
    path('customuser/create', CustomUserCreateView.as_view()),
    path('customuser/list/', CustomUserListView.as_view()),
]