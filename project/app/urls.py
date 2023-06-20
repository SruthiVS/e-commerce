# basic URL Configurations
from . import views
from django.urls import include, path
# import routers
from rest_framework import routers

  
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used

  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',CustomerReg.as_view()),
    path('api/cust/<int:pk>',CustomerDetails.as_view()),
    path('api/prod/',ProductList.as_view()),
    path('api/prod/<int:pk>',ProductDetails.as_view()),
    path('api/prodview/',ProdView.as_view()),
    
]

