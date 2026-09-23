from django.urls import path
from  . import views

urlpatterns=[
    path('api/create_analyzer/',views.create_analyzer_api,name="create_analyzer_api"),
    path('api/list_analyzer/',views.list_analyzer_api,name="list_analyzer_api"),
    path('api/detail_analyzer/<int:id>/',views.detail_analyzer_api,name="detail_analyzer_api"),
    path('api/update_analyzer/<int:id>/',views.update_analyzer_api,name="update_analyzer_api"),
    path('api/delete_analyzer/<int:id>/',views.delete_analyzer_api,name="delete_analyzer_api"),
]