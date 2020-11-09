from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    
    # products
    path('products/', views.products,name='products'),
    path('create_product/',views.CreateProduct,name='create_product'),
    path('update_product/<str:pk>',views.UpdateProduct,name='update_product'),
    path('category',views.category,name='category'),
    path('create-category',views.createCategory,name='createcategory'),
    path('update-category/<str:pk>',views.updateCategory,name='updatecategory'),
    path('brand',views.brand,name='brand'),
    path('create-brand',views.createBrand,name='createbrand'),
    path('update-brand/<str:pk>',views.updateBrand,name='updatebrand'),


    
    # customer
    path('customer/',views.customers,name='customer'),

    path('customer/<str:pk>/', views.CustomerPage,name='customerpage'),
    path('create-customer/',views.CreateCustomer,name='create_customer'),
    path('update-customer/<str:pk>',views.UpdateCustomer,name='update_customer'),



    path('create_order/',views.createOrder,name='sell'),
    path('update_order/<str:pk>',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>',views.deleteOrder,name='delete_order'),


    path('expense',views.expense,name='expense'),


    # Software Settings
    path('settings',views.appConfig,name='appconfig'),
]
