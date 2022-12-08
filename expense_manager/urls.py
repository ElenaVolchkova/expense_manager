"""expense_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from owner.views import OwnerViewSet
from transaction.views import *
from сategory.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/transaction_delete/<int:pk>', TransactionAPIDestroy.as_view()),
    path('api/v1/transaction/', TransactionAPIList.as_view()),
    path('api/v1/transaction/<int:pk>', TransactionAPIUpdate.as_view()),
    path('api/v1/category/', CategoryAPIList.as_view()),
    path('api/v1/category/<int:pk>', CategoryAPIUpdate.as_view()),
    path('api/v1/category_delete/<int:pk>', CategoryAPIDestroy.as_view()),
    # path('api/v1/ownerslist/', OwnerViewSet.as_view({"get": "list"})),
    # path('api/v1/ownerslist/<int:pk>', OwnerViewSet.as_view({"put": "update"})),
    # path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/category/

]
