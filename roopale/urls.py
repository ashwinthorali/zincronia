
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.views import changepw as cp
# from exam import views as auth_view
admin.site.site_header = 'Dashboard'                    # default: "Django Administration"
admin.site.index_title = 'Admin Panel'                 # default: "Site administration"
admin.site.site_title = 'Admin Panel' # default: "Django site admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blogs/', include('blog.urls')),
    path('products/', include('product.urls')),
    path('profile/', include('account.urls')),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('change-password/', cp, name='change_password'),
    # password reset
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm" ),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name= "password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

