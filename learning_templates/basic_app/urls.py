from django.conf.urls import url
from basic_app import views
from django.urls import path

# TEMPLATE TAGGING (Use template tagging to make URL navigation easier in the HTML files/ web pages
# 'app_name' is standard naming convention for django to reference - ALWAYS use this name for template tagging
app_name = 'basic_app'

urlpatterns =[
    path('relative/',views.relative,name='relative'),
    path('other/', views.other,name='other')
]
