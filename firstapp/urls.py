from django.urls import path, include
from .import views

urlpatterns = [
    path('signupForm_view', views.signupForm_view, name="signupForm_view"),
    path('login_view', views.login_view, name="login_view"),
    path('', views.dashboard_view, name="dashboard_view"),
    path('dashboard_view/', views.dashboard_view, name="dashboard_view"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('page<int:page_number>/', views.page, name='page'),
    path('gifts_view', views.gifts_view, name="gifts_view"),
    path('save_upi', views.save_upi, name="save_upi"),

]