"""newshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from user import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("registion/",views.registion,name="register"),
    path("forget/",views.forget,name="forget"),
    path("logout/",views.logoutreg,name="logout"),
    path("profile/",views.profile,name="profile"),
    
    path("edit/",views.edit,name="edit"),
    path("verify/",views.verify,name="verify"),
    path("refile/<slug:token>",views.refile,name="refile"),
    path("product/",views.product,name="product"),
   
    path("display/<slug:strg>",views.display,name="display"),
    path("card/<slug:strgs>",views.card,name="card"),
    path("cardwoman/<slug:strgs>",views.cardwoman,name="cardwoman"),
    path("cardkid/<slug:strgs>",views.cardkid,name="cardkid"),
    path("cardElect/<slug:strgs>",views.cardElect,name="cardElect"),
    path("showcart/",views.Show_card,name="show"),
    path("kid/",views.Kid,name="kid"),
    path("woman/",views.Women,name="woman"),
    path("elect/",views.Electroic,name="elect"),
    
    path('address/',views.Add,name="address"),
    path('updata/<int:pk>',views.update,name="updata"),
    path('order/<slug:strgs>',views.order,name="order"),
    path('trak/<slug:strgs>',views.trak,name="trak"),
    path('ordershow/',views.ordershow,name="ordershow"),
    path('itemmove/<int:id>',views.cart_delete,name="remove"),
    path("woman/<slug:strgs>",views.fwoman,name="fwoman"),
    path("man/<slug:strgs>",views.fman,name="fwoman"),
    path("kid/<slug:strgs>",views.fkidd,name="fwoman"),
    path("elect/<slug:strgs>",views.fElect,name="fwoman"),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
