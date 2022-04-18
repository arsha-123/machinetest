from .import views
from django.urls import path

urlpatterns=[
    path('mtlogin',views.mtlogin,name="mtlogin"),
    path('mtsignup',views.mtsignup,name="mtsignup"),
    path('mthome',views.mthome,name="mthome"),
]