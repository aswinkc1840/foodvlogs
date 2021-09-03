from django.urls import path, include

from shop import views

urlpatterns = [

    path('search', views.searhing, name='search'),
    path('details',views.details,name='details'),
    path('<slug:c_slug>/',views.details,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.single,name='single'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('', views.home, name='index'),

]