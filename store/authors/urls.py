


from django.urls import path
from .views import authors_create_form , authors_list, authors_detail, authors_delete, authors_update
urlpatterns = [

    path('forms/create/', authors_create_form, name='authors_create_form'),
    path('list/', authors_list, name='authors_list'),
    path('detail/<int:id>/', authors_detail, name='authors_detail'),
    path('delete/<int:id>/', authors_delete, name='authors_delete'),
    path('update/<int:id>/', authors_update, name='authors_update'),

]