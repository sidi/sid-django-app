from django.urls import path

from . import views

urlpatterns = [
    path('', views.ModuleListView.as_view(), name='module_list'),
    path('view/<slug:pk>', views.ModuleDetailView.as_view(), name='module_detail'),
    path('add', views.ModuleCreateView.as_view(), name='module_create'),
    path('del/<slug:pk>', views.ModuleDeleteView.as_view(), name='module_delete'),
    path('put/<slug:pk>', views.ModuleUpdateView.as_view(), name='module_update'),
]