from django.shortcuts import render
from main.models import Bitiruvchi
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import BitiruvchiSerializer 
# Create your views here.

class BitiruvchiListView(ListAPIView):
    queryset = Bitiruvchi.objects.all()
    serializer_class = BitiruvchiSerializer

class BitiruvchiView(ModelViewSet):
    queryset = Bitiruvchi.objects.all().order_by('id')
    serializer_class = BitiruvchiSerializer

    # def get_options(self):
    #     return "options", {
    #         "artist": [{'label': obj.name, 'value': obj.pk} for obj in Artist.objects.all()],
    #         "genre": [{'label': obj.name, 'value': obj.pk} for obj in Genre.objects.all()]
    #     }

    # class Meta:
    #     datatables_extra_json = ('get_options',)
