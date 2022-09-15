
from main.models import TumanVaShahar
from .filters import MaktabFilter

def data_avalible(request):
    all_tumanlar = TumanVaShahar.objects.all().order_by('name')

    context = {
        'all_tumanlar':all_tumanlar,    
    }
    return context