# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [

    # # path for registration
    path(route='register', view=views.registration, name='register'),
    path(route='register/', view=views.registration, name='register_slash'),

    # path for login
    path(route='login', view=views.login_user, name='login'),
    path(route='login/', view=views.login_user, name='login_slash'),
    
    # Path cho logout 
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='logout/', view=views.logout_request, name='logout_slash'),
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
