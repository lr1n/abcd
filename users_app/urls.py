from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from.views import get_profile


app_name = 'users_app'

urlpatterns = [
    path('login/', LogoutView.as_view(template_name='users_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('users_app:login')), name='logout'),
    path('get_profile/', get_profile, name='get_profile'),
]