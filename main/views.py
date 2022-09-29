from datetime import datetime
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import (
    Vil,
    Sport,
    Mahalla,
    ChetTili,
    Imkonyat,
    Qiziqish,
    Bitiruvchi,
    TypeKollej, 
    Universitet,
    TumanVaShahar, 
    MaktabBitiruvchisi, 
    KollejBitiruvchisi, 
    UniversitetBitiruvchisi,
    )

from .models import Maktab as MK
from .models import Kollej as KJ
from .forms import (
    KollejNameForm,
    MaktabForm,
    KollejForm,
    MaktabNameForm,
    UniversitetForm,
    UniversitetNameForm,
)

from .filters import (
    BitiruvchiFilter,
    KollejFilter,
    MaktabFilter,
    UniversitetFilter,
)

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views.generic.list import ListView

from django.db.models import Q
users = get_user_model()

import pandas as p

from .dataframe import database

this_year = datetime.now().year
# Create your views here.

def simple(request):
    all = Bitiruvchi.objects.filter(add_time__year=this_year)
    page = request.GET.get('page', 1)
    paginator = Paginator(all, 200)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'simple.html', context={
        'object_list': post,
    })

# class simple(ListView):
#     model = Bitiruvchi
#     paginate_by = 100
#     ordering = '-add_time'
#     template_name = 'simple.html'

# diagramm section
def Home(request):
    mkb = MaktabBitiruvchisi.objects.filter(add_time__year=this_year).count()
    kjb = KollejBitiruvchisi.objects.filter(add_time__year=this_year).count()
    unb = UniversitetBitiruvchisi.objects.filter(add_time__year=this_year).count()
    return render(request, 'base.html', {
        'mkb':mkb,
        'kjb':kjb,
        'unb':unb,
    })
def SearchAllStudents(request):
    mkb = MaktabBitiruvchisi.objects.filter(add_time__year=this_year).count()
    kjb = KollejBitiruvchisi.objects.filter(add_time__year=this_year).count()
    unb = UniversitetBitiruvchisi.objects.filter(add_time__year=this_year).count()
    query = request.GET.get('searchHome')
    if query:
        queryset = Bitiruvchi.objects.filter(
            Q(f_name__icontains=query) |
            Q(tuman__name__icontains=query) |
            Q(mahalla__name__icontains=query) |
            Q(phone__icontains=query) |
            Q(jins__icontains=query) |
            Q(maktabbitiruvchisi__sinf__icontains=query) |
            Q(maktabbitiruvchisi__maktab__name__icontains=query) |
            Q(kollejbitiruvchisi__stu_way__icontains=query) |
            Q(universitetbitiruvchisi__stu_way__icontains=query) 
        ).order_by("f_name")
    else:
        queryset = Bitiruvchi.objects.filter(add_time__year=this_year).order_by('f_name') 
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 100)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages) 
    return render(request, 'pages/search.html', {
        'mkb':mkb,
        'kjb':kjb,
        'unb':unb,
        'object_list':post,
    })

def Districts(request, pk):
    d = TumanVaShahar.objects.get(pk=pk)
    maktab = MK.objects.filter(tuman=pk).all()
    kollej_all = KJ.objects.filter(tuman_id=pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    typeKol = TypeKollej.objects.all()
    mkb = MaktabBitiruvchisi.objects.filter(tuman_id=pk, add_time__year=this_year).count()
    kjb = KollejBitiruvchisi.objects.filter(tuman_id=pk, add_time__year=this_year).count()
    unb = UniversitetBitiruvchisi.objects.filter(tuman_id=pk, add_time__year=this_year).count()
    btr = Bitiruvchi.objects.filter(tuman_id=pk, add_time__year=this_year) 
    page = request.GET.get('page', 1)
    paginator = Paginator(btr, 100)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "pages2/tumanlar.html", {
        'd':d,
        'pk':pk,
        'mkb':mkb,
        'unb':unb,
        'kjb':kjb,
        'object_list':post,
        'all_d':all_d,
        'maktab':maktab,
        'typeK': typeKol,
        'all_kj':kollej_all,
    })    

def Schools(request, pk):
    maktab = MK.objects.get(pk=pk)
    tuman_pk = MK.objects.get(pk=pk).tuman.pk
    maktab_all = MK.objects.filter(tuman_id=tuman_pk)
    kollej_all = KJ.objects.filter(tuman_id=tuman_pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    student = MaktabBitiruvchisi.objects.filter(maktab=maktab.pk, add_time__year=this_year)
    gra_9 = MaktabBitiruvchisi.objects.filter(maktab=pk, sinf="9-sinf", add_time__year=this_year).count()
    gra_11 = MaktabBitiruvchisi.objects.filter(maktab=pk, sinf="11-sinf", add_time__year=this_year).count()
    grils = MaktabBitiruvchisi.objects.filter(maktab=pk, jins="qiz bola", add_time__year=this_year).count()
    boys = MaktabBitiruvchisi.objects.filter(maktab=pk, jins="o'g'il bola", add_time__year=this_year).count()
    page = request.GET.get('page', 1)
    paginator = Paginator(student, 100)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "pages2/maktab/maktab.html",{
        'pk':pk,
        'mk':maktab,
        'boys': boys,
        'grils': grils,
        'all_d': all_d,
        'gra_9': gra_9,
        'gra_11': gra_11,
        'object_list':post,
        'all_mk':maktab_all,
        'all_kj': kollej_all,
    }) 

def AllKollejBit(request, pk):
    all_types = TypeKollej.objects.all()
    kollej_all_stu = KollejBitiruvchisi.objects.filter(tuman=pk, add_time__year=this_year)
    tuman_id = kollej_all_stu[0].tuman.pk
    kj = KJ.objects.filter(tuman_id=tuman_id)
    maktab_all = MK.objects.filter(tuman_id=tuman_id)
    all_d = TumanVaShahar.objects.all().order_by('name')
    student = KollejBitiruvchisi.objects.filter(tuman=pk, add_time__year=this_year)
    grils = KollejBitiruvchisi.objects.filter(tuman_id=tuman_id, jins="qiz bola", add_time__year=this_year).count()
    boys = KollejBitiruvchisi.objects.filter(tuman_id=tuman_id, jins="o'g'il bola", add_time__year=this_year).count()
    list_p_t = []
    for i in all_types:
        list_p_t.append(kollej_all_stu.filter(type=i.pk).count())
        print(kollej_all_stu.filter(type=i.pk).count())
    page = request.GET.get('page', 1)
    paginator = Paginator(student, 100)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "pages2/maktab/all_kollej_stu.html",{
        'pk':pk,
        'kjt': kj,
        'boys': boys,
        'grils': grils,
        'all_d': all_d,
        'object_list':post,
        'tuman_id':tuman_id,
        'all_mk':maktab_all,
        'kas':kollej_all_stu,
        'all_type':all_types,
        'count_0': list_p_t[0],
        'count_1': list_p_t[1],
        'count_2': list_p_t[2],
    }) 

def OTM_all_stu(request, pk):
    otm_all_stu = UniversitetBitiruvchisi.objects.filter(tuman=pk, add_time__year=this_year)
    tuman_id = otm_all_stu[0].tuman.pk
    maktab_all = MK.objects.filter(tuman_id=tuman_id)
    all_d = TumanVaShahar.objects.all().order_by('name')
    student = UniversitetBitiruvchisi.objects.filter(tuman=pk, add_time__year=this_year)
    grils = UniversitetBitiruvchisi.objects.filter(tuman_id=tuman_id, jins="qiz bola", add_time__year=this_year).count()
    boys = UniversitetBitiruvchisi.objects.filter(tuman_id=tuman_id, jins="o'g'il bola", add_time__year=this_year).count()
    page = request.GET.get('page', 1)
    paginator = Paginator(student, 100)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "pages2/maktab/all_otm_stu.html",{
        'pk':pk,
        'boys': boys,
        'grils': grils,
        'all_d': all_d,
        'kas':otm_all_stu,
        'object_list':post,
        'all_mk':maktab_all,
        'tuman_id':tuman_id,
    }) 

def KollejD(request, pk):
    all_types = TypeKollej.objects.all()
    kollej = KJ.objects.get(pk=pk)
    tuman_pk = kollej.tuman.pk
    kj = KJ.objects.filter(tuman_id=tuman_pk)
    maktab_all = MK.objects.filter(tuman_id=tuman_pk)
    kollej_all = KJ.objects.filter(tuman_id=tuman_pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    student = KollejBitiruvchisi.objects.filter(kollej=kollej.pk)
    grils = KollejBitiruvchisi.objects.filter(kollej=pk, jins="qiz bola").count()
    boys = KollejBitiruvchisi.objects.filter(kollej=pk, jins="o'g'il bola").count()
    page = request.GET.get('page', 1)
    paginator = Paginator(student, 100)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'pages2/maktab/kollej.html', {
        'pk':pk,
        'kjt':kj,
        'kj':kollej,
        'boys':boys,
        'all_d':all_d,
        'grils': grils,
        'object_list':post,
        'all_mk':maktab_all,
        'all_kj':kollej_all,
        'all_type':all_types,

    })

def UniversitetB(request, pk):
    un = Universitet.objects.get(pk=pk)
    tuman_pk = un.tuman.pk
    all_d = TumanVaShahar.objects.all().order_by('name')
    maktab_all = MK.objects.filter(tuman_id=tuman_pk)
    kollej_all = KJ.objects.filter(tuman_id=tuman_pk)
    students = UniversitetBitiruvchisi.objects.filter(universitet=un.pk, add_time__year=this_year)
    grils = UniversitetBitiruvchisi.objects.filter(universitet=pk, jins="qiz bola", add_time__year=this_year).count()
    boys = UniversitetBitiruvchisi.objects.filter(universitet=pk, jins="o'g'il bola", add_time__year=this_year).count()
    page = request.GET.get('page', 1)
    paginator = Paginator(students, 100)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, 'pages2/universitet.html', {
        'pk':pk,
        'un':un,
        'boys':boys,
        'grils':grils,
        'all_d':all_d,
        'object_list':post,
        'all_mk':maktab_all,
        'all_kj':kollej_all,

    })

# RESUME SECTIONS

def Resume(request, pk):
    object = Bitiruvchi.objects.get(pk=pk, add_time__year=this_year)
    return render(request, 'cv/resume.html', context={
        'pk' : pk,
        'object' : object,
    })

# tables section

def Table(request):
    global return_data
    all_students = Bitiruvchi.objects.filter(add_time__year=this_year).order_by('f_name')
    all_student_filter = BitiruvchiFilter(request.GET, queryset=all_students)
    all_students = all_student_filter.qs 
    page = request.GET.get('page', 1)
    paginator = Paginator(all_students, 50)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    def return_data():
        return all_students[:200]
    return render(request, 'index.html', {
        'object_list':post,
        'mkFil':all_student_filter,
    })

class TableList(ListView):
    model = Bitiruvchi
    paginate_by = 50
    ordering = '-id'
    template_name = 'index2.html'

def Maktab(request):
    mk = MaktabBitiruvchisi.objects.filter(add_time__year=this_year)
    mkFilter = MaktabFilter(request.GET, queryset=mk)
    mk = mkFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(mk, 50)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "pages/maktab.html", {
        'object_list':post,
        'mkFil':mkFilter,
    })

def Kollej(request):
    kj = KollejBitiruvchisi.objects.filter(add_time__year=this_year)
    kjFilter = KollejFilter(request.GET, queryset=kj)
    kj=kjFilter.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(kj, 100)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "pages/kollej.html", {
        'object_list':post,
        'mkFil':kjFilter,
    })

def OTM_Finish(request):
    un = UniversitetBitiruvchisi.objects.filter(add_time__year=this_year)
    unFilters = UniversitetFilter(request.GET, queryset=un)
    un = unFilters.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(un, 100)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "pages/otm_bitiruvchilari.html", {
        'object_list':post,
        'mkFil':unFilters,
    })


def OTM_Enter(request):
    all_graduents = Bitiruvchi.objects.filter(add_time__year=this_year)
    otm_fil = BitiruvchiFilter(request.GET, queryset=all_graduents)
    all_graduents = otm_fil.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(all_graduents, 100)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "pages/otm_topshirganlar.html", context={
        'object_list':post,
        'mkFil':otm_fil,
    })
    
def AllDistricts(request):
    all_d = TumanVaShahar.objects.filter(add_time__year=this_year).order_by('name')
    return render(request, 'pages2/all_tumanlar.html', {"all_d": all_d })


def Ish(request):
    return render(request, "pages/ish_.html")

def Other(request):
    return render(request, "pages/boshqa.html")


# Add Sections

def DataAdd(request):
    return render(request, 'pages/data-add.html')

def MaktabAdd(request):
    if request.method == "POST":
        form = MaktabForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Maktab Muafaqiyatli qo'shildi")
            return redirect("MBA")
        messages.error(request, "Malumot kiritishda xatolik")
        
    form = MaktabForm
    imk = Imkonyat.objects.all()
    return render(request, 'forms/add/maktabAdd.html', {
        "form":form,
        'imk':imk,
    })
 
class MaktabADD(SuccessMessageMixin, CreateView):
    model = MaktabBitiruvchisi
    form_class = MaktabForm
    template_name = 'forms/add/maktabAdd.html'
    success_url = reverse_lazy("MBA")
    success_message = 'Maktab muaffaqiyatli qo\'shildi'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class KollejAdd(SuccessMessageMixin, CreateView):
    model = KollejBitiruvchisi
    form_class = KollejForm
    template_name = 'forms/add/kollejAdd.html'
    success_url = reverse_lazy("KBA")
    success_message = 'Kollej muaffaqiyatli qo\'shildi!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def UniversitetAdd(request):
    if request.method == "POST":
        form = UniversitetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Universitet Muafaqiyatli qo'shildi")
            return redirect("UBA")
        messages.error(request, "Malumot kiritishda xatolik")
        
    form = UniversitetForm
    return render(request, 'forms/add/universitetAdd.html', {"form":form})

#C:\Users\MarkazPC\Desktop\Zohidillo\3_\demo_site\main\views.py    

class MaktabNameAddView(SuccessMessageMixin, CreateView):
    model = MK 
    template_name = 'forms/sections/add/maktabnameadd.html'
    form_class = MaktabNameForm
    success_message = 'Yangi maktab muaffaqiyatli qo\'shildi!'
    success_url = reverse_lazy("MaNAV")

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = MK.objects.all().order_by('tuman__name')
        return super().get_context_data(**kwargs)

        
class KollejNameAddView(SuccessMessageMixin, CreateView):
    model = KJ
    template_name = 'forms/sections/add/kollejnameadd.html'
    form_class = KollejNameForm
    success_url = reverse_lazy("KNAV")
    success_message = 'Yangi kollej muaffaqiyatli qo\'shildi!'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = KJ.objects.all().order_by('name')
        return super().get_context_data(**kwargs)

class UniversitetNameAddView(SuccessMessageMixin, CreateView):
    model = Universitet
    template_name = 'forms/sections/add/universitetnameadd.html'
    form_class = UniversitetNameForm
    success_url = reverse_lazy("UNAV")
    success_message = 'Yangi universitet muaffaqiyatli qo\'shildi!'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Universitet.objects.all().order_by('name')
        return super().get_context_data(**kwargs)

class QiziqishNameAddView(SuccessMessageMixin, CreateView):
    model = Qiziqish
    fields = '__all__'
    success_url = reverse_lazy("QNAV")
    template_name = 'forms/sections/add/qiziqishnameadd.html'
    success_message = 'Yangi qiziqish muaffaqiyatli qo\'shildi!'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Qiziqish.objects.all().order_by('name')
        return super().get_context_data(**kwargs)

class ImkonyatNameAddView(SuccessMessageMixin, CreateView):
    model = Imkonyat
    fields = '__all__'
    success_url = reverse_lazy("INAV")
    template_name = 'forms/sections/add/imkonyatnameadd.html'
    success_message = 'Yangi imkonyat muaffaqiyatli qo\'shildi!'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Imkonyat.objects.all().order_by('name')
        return super().get_context_data(**kwargs)

class ChetTiliNameAddView(SuccessMessageMixin, CreateView):
    model = ChetTili
    fields = '__all__'
    success_url = reverse_lazy("FNAV")
    template_name = 'forms/sections/add/f_langnameadd.html'
    success_message = 'Yangi chet tili muaffaqiyatli qo\'shildi!'
    
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = ChetTili.objects.all().order_by('name')
        return super().get_context_data(**kwargs)

class SportNameAddView(SuccessMessageMixin, CreateView):
    model = Sport
    fields = '__all__'
    success_url = reverse_lazy("SNAV")
    template_name = 'forms/sections/add/sportnameadd.html'
    success_message = 'Yangi sport turi muaffaqiyatli qo\'shildi!'
    
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Sport.objects.all().order_by('name')
        return super().get_context_data(**kwargs)

class MahallaNameAddView(SuccessMessageMixin, CreateView):
    model = Mahalla
    fields = '__all__'
    success_url = reverse_lazy("MNAV")
    template_name = 'forms/sections/add/mahallanameadd.html'
    success_message = 'Yangi mahalla muaffaqiyatli qo\'shildi!'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Mahalla.objects.all().order_by('tuman__name')
        return super().get_context_data(**kwargs)

class TumanVaShaharNameAddView(SuccessMessageMixin, CreateView):
    model = TumanVaShahar
    fields = '__all__'
    success_url = reverse_lazy("TvSNAV")
    template_name = 'forms/sections/add/tumannameadd.html'
    success_message = 'Yangi Malumot muaffaqiyatli qo\'shildi!'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = TumanVaShahar.objects.all().order_by('name')
        return super().get_context_data(**kwargs)

class VilNameAddView(SuccessMessageMixin, CreateView):
    model = Vil
    fields = '__all__'
    success_url = reverse_lazy("VNAV")
    template_name = 'forms/sections/add/vilnameadd.html'
    success_message = 'Yangi Malumot muaffaqiyatli qo\'shildi!'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Vil.objects.all().order_by('name')
        return super().get_context_data(**kwargs)

# AJAX SECTION

def load_kollej(request):
    tuman_id = request.GET.get("tuman_kj")
    kollej = KJ.objects.filter(tuman_id=tuman_id).order_by('name')
    return render(request, 'loads/load_kollej_list.html', {"kollej" : kollej})

def load_type_kollej(request):
    tuman_id = request.GET.get("tuman_kj")
    type = request.GET.get("type")
    kollej = KJ.objects.filter(tuman=tuman_id, type=type).order_by("name")
    return render(request, 'loads/load_type_kollej_list.html', {"kollej" : kollej})

def load_mahalla(request):
    tuman_id = request.GET.get('tuman_id')
    mahalla = Mahalla.objects.filter(tuman_id=tuman_id).order_by('name')
    return render(request, 'loads/load_mahalla_list.html', {"mahalla":mahalla})

def load_maktab(request):
    tuman_id = request.GET.get('tuman_id')
    maktab = MK.objects.filter(tuman_id=tuman_id).order_by("name")
    return render(request, 'loads/load_maktab_list.html', {"maktab" : maktab})

def load_otm(request):
    vil_id = request.GET.get("viloyat")
    otm = Universitet.objects.filter(viloyat_id=vil_id).order_by("name")
    return render(request, 'loads/load_otm_list.html', {"otm" : otm})

# EDIT // DELETE section

class EditMaktabBitiruvchi(UpdateView, SuccessMessageMixin):
    model = MaktabBitiruvchisi
    form_class = MaktabForm
    template_name = 'forms/edit/maktab.html'
    success_message = 'Taxrirlash muaffaqiyatli bajarildi!'
    success_url = reverse_lazy("T")

class EditKollejBitiruvchi(UpdateView, SuccessMessageMixin):
    model = KollejBitiruvchisi
    form_class = KollejForm
    template_name = 'forms/edit/kollej.html'
    success_message = 'Taxrirlash muaffaqiyatli bajarildi!'
    success_url = reverse_lazy("T")


class EditOTMBitiruvchi(UpdateView, SuccessMessageMixin):
    form_class = UniversitetForm
    model = UniversitetBitiruvchisi
    template_name = 'forms/edit/otm.html'
    success_message = 'Taxrirlash muaffaqiyatli bajarildi!'
    success_url = reverse_lazy("T")

class DeleteBitiruvchi(DeleteView, SuccessMessageMixin):
    model = Bitiruvchi
    success_message = 'O\'chirish muaffaqiyatli bajarildi!'
    success_url = reverse_lazy("T")


# EXPORT SECTION
def export_excel_table(request): 
    table = return_data()
    data = database(table)
    df = p.DataFrame(data) 
    # print(df) 
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') 
    response['Content-Disposition'] = f'attachment; filename="Bitiruvchilar -- {str(datetime.now())}.xls"' 
    df.to_excel(response, sheet_name="Barcha talabalar", index_label='№', index=True) 
    return response
    
