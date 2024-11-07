from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import EmployeeViewSet, employee_list, employee_listview

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/', employee_list, name='employee_list'),
    path('employee_listview/', employee_listview, name='employee_listview'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employee/<int:employee_id>/update/', views.employee_update, name='employee_update'),
    path('employee/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),
]