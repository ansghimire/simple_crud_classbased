from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.Create.as_view(), name="create"),
    path('list/', views.List.as_view(), name="list"),
    path('details/<uuid:pk>', views.Detail.as_view(), name="details"),
    path('delete/<uuid:pk>', views.Delete.as_view(), name="delete"),
    path('update/<uuid:pk>', views.Update.as_view(), name="update"),
]