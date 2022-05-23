from django.urls import path,include
from django.conf import settings
from .import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:proid>/', views.productdetails, name='detail'),
    path('cat/<int:categoryid>/', views.presscatagory, name='cate'),
    path('add/<int:proid>/', views.add, name='add'),
    path('cartitem/', views.cartitem, name='cartitem'),
    path('delet/<int:proid>/', views.delet, name='delet'),
    
    
]

 