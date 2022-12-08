import django_filters

from transaction.models import Transaction


class TransactionFilter(django_filters.FilterSet):
    date = django_filters.IsoDateTimeFromToRangeFilter()
    amount = django_filters.RangeFilter()

    class Meta:
        model = Transaction
        fields = ['amount', 'date']