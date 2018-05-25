from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # login / logout
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'),
    path("logout-then-login/", auth_views.logout_then_login,
        name='logout_then_login'),
    # password change
    path("password-change/", auth_views.PasswordChangeView.as_view(
            template_name='users/password_change_form.html'),
        name='password_change'),
    path("password-change-done/", auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'),
        name='password_change_done'),
    # password reset
    path("password-reset/", auth_views.PasswordResetView.as_view(
            template_name='users/password_reset_form.html',
            email_template_name='users/password_reset_email.html',
            subject_template_name='users/password_reset_subject.txt'),
        name='password_reset'),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path("password-reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
]
