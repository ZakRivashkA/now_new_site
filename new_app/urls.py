from django.urls import path
from .views import index, form_save

app_name = 'new_app'

urlpatterns = [
    path('', index, name='index'),
    path('form_1/', form_save, name='form_save')
]
