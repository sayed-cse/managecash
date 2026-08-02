# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm, CashForm
from .models import Cash

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("dashboard")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = "login"
    template_name = "dashboard.html"


class CashListView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Cash
    template_name = "cash_list.html"
    context_object_name = "cash_list"

    def get_queryset(self):
        return Cash.objects.filter(
            user=self.request.user
        ).order_by("-date", "-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        income = Cash.objects.filter(user=self.request.user, transaction_type="Income")

        expense = Cash.objects.filter(user=self.request.user, transaction_type="Expense")

        total_income = sum(item.amount for item in income)
        total_expense = sum(item.amount for item in expense)

        context["total_income"] = total_income
        context["total_expense"] = total_expense
        context["balance"] = total_income - total_expense

        return context

class CashCreateView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Cash
    form_class = CashForm
    template_name = "cash_form.html"
    success_url = reverse_lazy("cash_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CashUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "login"
    model = Cash
    form_class = CashForm
    template_name = "cash_form.html"
    success_url = reverse_lazy("cash_list")

    def get_queryset(self):
        return Cash.objects.filter(user=self.request.user)


class CashDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "login"
    model = Cash
    template_name = "cash_confirm_delete.html"
    success_url = reverse_lazy("cash_list")

    def get_queryset(self):
        return Cash.objects.filter(user=self.request.user)



        







