from django.urls import path
from. import views


urlpatterns=[
    path('',views.home,name='home'),
    path('makepizza',views.makepizza,name='makepizza'),
    path('show',views.show,name='show'),
    path('edit',views.edit,name='edit'),
    path('delete',views.delete,name='delete'),

]