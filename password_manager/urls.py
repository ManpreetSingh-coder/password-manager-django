from django.contrib import admin
from django.urls import path, include
from vault import views as vault_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vault_views.dashboard, name='dashboard'),
    path('add/', vault_views.add_password, name='add_password'),
    path('vault/', include('vault.urls')),
]
