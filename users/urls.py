from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path("logout-then-login/", auth_views.logout_then_login, name='logout_then_login'),
    # path("password_change/", auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='logout')
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
]
