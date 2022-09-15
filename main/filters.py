import django_filters

from .models import (
    Bitiruvchi,
    MaktabBitiruvchisi,
    KollejBitiruvchisi,
    UniversitetBitiruvchisi,
)
from .forms import (
    KollejFilterForm,
    MaktabFilterForm,
    UniversiterFilterForm,
) 
class MaktabFilter(django_filters.FilterSet):
    class Meta:
        model = MaktabBitiruvchisi
        fields = ('tuman', 'mahalla', 'maktab', 'sinf')
        form = MaktabFilterForm

class KollejFilter(django_filters.FilterSet):
    class Meta:
        model = KollejBitiruvchisi
        fields = ('tuman', 'mahalla', 'type', 'tuman_kj', 'kollej')
        form = KollejFilterForm

class UniversitetFilter(django_filters.FilterSet):
    class Meta:
        model = UniversitetBitiruvchisi
        fields = ('tuman', 'mahalla', 'vil', 'universitet')
        form = UniversiterFilterForm

class BitiruvchiFilter(django_filters.FilterSet):
    class Meta:
        model = Bitiruvchi
        fields = ('tuman', 'mahalla', 'maktabbitiruvchisi__maktab','maktabbitiruvchisi__sinf', 'kollejbitiruvchisi__kollej', 'kollejbitiruvchisi__type', 'kollejbitiruvchisi__tuman_kj', 'universitetbitiruvchisi__vil','universitetbitiruvchisi__universitet')