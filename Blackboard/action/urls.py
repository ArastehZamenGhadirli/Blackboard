from django.urls import path 
from .views import get_blackboard,add_content,delete_content,clear_blackboard


urlpatterns = [
    path('blackboard/<str:username>/' , get_blackboard ),
    path('add-content/<str:username>' , add_content),
    path('delete/<str:content_type>/<int:content_id>/' , delete_content),
    path('clear/<str:username>/' ,clear_blackboard)
]
