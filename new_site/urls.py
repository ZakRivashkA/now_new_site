from django.urls import path
from .views import main_page, category_sort, product_detail, less_forms, category_form, product_form, \
    shop_form, form_category, form_model

app_name = 'new_site'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('<int:id>/', category_sort, name="category_sort"),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('less_forms/', less_forms, name='less_forms'),
    path('category_form/', category_form, name='category_form'),
    path('product_form/', product_form, name='product_form'),
    path('shop_form/', shop_form, name='shop_form'),
    path('form_category/', form_category, name='form_category'),
    path('form_model/', form_model, name='form_model'),
]
