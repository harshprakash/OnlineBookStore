

from django.contrib import admin
from django.urls import path,include
from User import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="User/login.html"),name="Login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="User/logout.html"),name="Logout"),
    path('register/',user_views.register,name="register"),
    path('admin/', admin.site.urls),
    path('', include('Book.urls')),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="User/password_reset.html"),name="password-reset"),
    
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='User/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='User/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='User/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    #path('cart/',include('cart.urls')),
    path('',include('Cart.urls'))
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)