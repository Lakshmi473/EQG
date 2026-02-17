from django.contrib import admin
from django.urls import path
from adilak import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),                # splash page
    path('select-items/', views.select_items, name='select_items'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/products/', views.api_products, name='api_products'),
    path('api/categories/', views.api_categories, name='api_categories'),
    path('api/companies/', views.api_companies, name='api_companies'),
    path('add-item/', views.add_item, name='add_item'),
   path('generate-excel/', views.generate_excel, name='generate_excel'),
    path('cart/save/', views.save_quotation, name='save_quotation'),      # optional
    path('cart/update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-labour/', views.update_labour, name='update_labour'),
]