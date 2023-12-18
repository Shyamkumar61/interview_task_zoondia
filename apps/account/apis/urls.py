from django.urls import path
from .views import UserAccountView, UsersListView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), 
    path('create-account/', UserAccountView.as_view(), name='create-account'),
    path('user-lists/', UsersListView.as_view(), name='user-lists')
]