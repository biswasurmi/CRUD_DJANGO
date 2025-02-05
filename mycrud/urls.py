from django.urls import path
from .views import StudentListView,StudentCreateView,StudentUpdateView,StudentDeleteView

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('add/', StudentCreateView.as_view(), name='add'),
    path('edit/', StudentUpdateView.as_view(), name='edit'),
    path('update/<int:pk>', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='delete'),
]
# urlpatterns = [
#     path('', views.INDEX, name='index'),
#     path('add/', views.Add, name='add'),
#     path('edit/', views.Edit, name='edit'),
#     path('update/<str:id>', views.Update, name='update'),
#     path('delete/<str:id>', views.Delete, name='delete'),
# ]