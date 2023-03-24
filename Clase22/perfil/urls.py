from django.urls import path
from django.contrib.auth.views import LogoutView
from perfil.views import login_request, register

# URL's de vistas basadas en Clase
urlpatterns = [
    path('login/', login_request, name="login"),
    path('register/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name='perfil/logout.html'), name="Logout"),
]
