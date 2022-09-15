from django.urls import path
from .views import (
    Home,
    Table,
    Resume,
    Maktab,
    Kollej,
    KollejD,
    Schools,
    DataAdd,
    TableList,
    load_otm,
    MaktabADD, 
    OTM_Enter,
    Districts,
    KollejAdd,
    OTM_Finish,
    OTM_all_stu,
    load_kollej,
    load_maktab,
    load_mahalla,
    UniversitetB,
    AllDistricts,
    AllKollejBit,
    UniversitetAdd,
    VilNameAddView,
    SportNameAddView, 
    SearchAllStudents,
    DeleteBitiruvchi,
    load_type_kollej,
    MaktabNameAddView,
    KollejNameAddView,
    EditOTMBitiruvchi,
    MahallaNameAddView,
    QiziqishNameAddView,
    ChetTiliNameAddView,
    ImkonyatNameAddView,
    EditMaktabBitiruvchi,
    EditKollejBitiruvchi,
    UniversitetNameAddView,
    TumanVaShaharNameAddView,
    simple,
    export_excel_table
)
urlpatterns = [

    path("", Home, name="H"),
    path("table/", Table, name="T"),
    path("table/list/", TableList.as_view(), name="Tt"),
    path("maktab/", Maktab, name="M"),
    path("kollej/", Kollej, name="K"),
    path("enter/", OTM_Enter, name="E"),
    path("finish/", OTM_Finish, name="F"),
    path("tuman/<pk>/", Districts, name="D"),
    path("data/new/add/", DataAdd, name="DA"),
    path("tumanlar/all/", AllDistricts, name="AD"),
    path("search/", SearchAllStudents, name="SEA"),
    path("tumanlar/maktablar/<pk>/", Schools, name="S"),
    path("tumanlar/kollejlar/<pk>/", KollejD, name="KD"),
    
# ajax section
    path("ajax/load/otm/list", load_otm, name="ALO"),
    path("ajax/load/kollej/list", load_kollej, name="ALK"),
    path("ajax/load/maktab/list", load_maktab, name="ALMa"),
    path("ajax/load/mahalla/list", load_mahalla, name="ALM"),
    path("ajax/load/type/kollej/list", load_type_kollej, name="ALTK"),
# end ajax section

    path("bitiruvchilar/resume/<pk>/", Resume, name="RE"),
    path("tumanlar/universitet/<pk>/", UniversitetB, name="UB"),
    path("data/new/add/vil/", VilNameAddView.as_view(), name="VNAV"),
    path("bitiruvchilar/tumanlar/otm/<pk>/", OTM_all_stu, name="AOB"),
    path("bitiruvchi/kollej/new/add/", KollejAdd.as_view(), name="KBA"),
    path("bitiruvchi/universitet/new/add/", UniversitetAdd, name="UBA"),
    path("bitiruvchi/maktab/new/add/", MaktabADD.as_view(), name="MBA"),
    path("data/new/add/sport/", SportNameAddView.as_view(), name="SNAV"),
    path("bitiruvchilar/tumanlar/kollej/<pk>/", AllKollejBit, name="AKB"),
    path("data/new/add/kollej/", KollejNameAddView.as_view(), name="KNAV"),
    path("data/new/add/maktab/", MaktabNameAddView.as_view(), name="MaNAV"),
    path("data/new/add/mahalla/", MahallaNameAddView.as_view(), name="MNAV"),
    path("data/new/add/qiziqish/", QiziqishNameAddView.as_view(), name="QNAV"),
    path("data/new/add/imkonyat/", ImkonyatNameAddView.as_view(), name="INAV"),
    path("data/new/add/chettili/", ChetTiliNameAddView.as_view(), name="FNAV"),
    path("data/new/add/universitet/", UniversitetNameAddView.as_view(), name="UNAV"),
    path("data/new/add/tumanvashahar/", TumanVaShaharNameAddView.as_view(), name="TvSNAV"),

    # EDIT 
    path("bitiruvchilar/delete/<pk>/", DeleteBitiruvchi.as_view(), name="DB"),
    path("bitiruvchilar/otm/taxrirlash/<pk>/", EditOTMBitiruvchi.as_view(), name="EOB"),
    path("bitiruvchilar/maktab/taxrirlash/<pk>/", EditMaktabBitiruvchi.as_view(), name="EMB"),
    path("bitiruvchilar/kollej/taxrirlash/<pk>/", EditKollejBitiruvchi.as_view(), name="EKB"),
    
    path("bitiruvchilar/simple/", simple, name="SIMPLE"),

    # export section
    path("bitiruvchilar/export/excel/all", export_excel_table, name="export_table"),

]