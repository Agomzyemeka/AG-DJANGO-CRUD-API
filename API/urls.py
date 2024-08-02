from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name="bogpost-view-create"),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name= "update"),
    path('blogposts/List/', views.BlogPostList.as_view(), name= "Query")
]