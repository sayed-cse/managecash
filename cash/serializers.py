from rest_framework import serializers
from .models import Cash


class CashSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cash

        fields = [
            "id",
            "title",
            "amount",
            "transaction_type",
            "date",
            "note",
        ]