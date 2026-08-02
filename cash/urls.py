from django.urls import path

from .views import (
    RegisterView,
    UserLoginView,
    UserLogoutView,
    DashboardView,
    CashListView,
    CashCreateView,
    CashUpdateView,
    CashDeleteView,
)

urlpatterns = [
    path("", UserLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    
    path("dashboard/", DashboardView.as_view(), name="dashboard"),

    path("cash/", CashListView.as_view(), name="cash_list"),
    path("cash/add/", CashCreateView.as_view(), name="cash_add"),

    path("cash/<int:pk>/edit/", CashUpdateView.as_view(), name="cash_edit"),
    path("cash/<int:pk>/delete/", CashDeleteView.as_view(), name="cash_delete"),
]