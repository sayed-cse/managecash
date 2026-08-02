from django.contrib import admin
from .models import Cash


@admin.register(Cash)
class CashAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "amount",
        "transaction_type",
        "user",
        "date",
    )

    list_filter = (
        "transaction_type",
        "date",
    )

    search_fields = (
        "title",
        "user__username",
    )