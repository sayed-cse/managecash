from django.db import models
from django.contrib.auth.models import User


class Cash(models.Model):
    TRANSACTION_TYPES = (
        ("Income", "Income"),
        ("Expense", "Expense"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cash_transactions"
    )

    title = models.CharField(max_length=100)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    date = models.DateField(auto_now_add=True)

    note = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.title} - {self.amount}"