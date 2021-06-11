from django.urls import path
from . import views
# from django.urls import path, include
from django.contrib.auth import views as auth_views
# from django_email_verification import urls as email_urls


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
        name="password_reset_complete"),
    # path('email/', include(email_urls)),
    path('otp',views.otp, name='otp')
]
