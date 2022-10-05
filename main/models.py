
from django.db import models
from django.contrib.auth import get_user_model

Users = get_user_model()
# Create your models here.


l = 300

t_sh = (
    ("tuman", "tuman"),
    ("shahar", "shahar"),
)

yesNo = (
    ("Bor", "Bor"),
    ("Yoq", "Yoq"),
)

sinf = (
    ("9-sinf", "9-sinf"),
    ("11-sinf", "11-sinf"),
)

jins = (
    ("o'g'il bola", "o'g'il bola"),
    ("qiz bola", "qiz bola"),
)
aim = (
    ("O'qishni davom etirmoqchi", "O'qishni davom etirmoqchi"),
    ("Ishlamoqchi", "Ishlamoqchi"),
)

type_school = (
    ("O'rta ta'lim maktabi", "O'rta ta'lim maktabi"),
    ("Ixtisoslashgan maktablar", "Ixtisoslashgan maktablar"),
)
vil_status = (
    ("shaxar", "shaxar"),
    ("viloyati", "viloyati"),
    ("respublikasi", "respublikasi")
)

class AutoTime(models.Model):
    """ Barcha classlarda bor asosiy xususiyatlar """
    name = models.CharField(max_length=l, verbose_name="Nomi")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TypeKollej(AutoTime):
    """ Professalan ta'lim turlari """

    def __str__(self):
        return super().__str__()

class TumanVaShahar(AutoTime):
    """ Toshketn vil dagi barcha tuman va shaxarlar nomlar """
    status = models.CharField(max_length=l, choices=t_sh, default="shaxar") # return tuman yoki shaxar 

    def __str__(self):
        return f"{super().name} {self.status}"
    
    def all_maktab(self):
        return self.maktab_set.all()

class Mahalla(AutoTime):
    """ Hududlardagi mahallalar nomi """
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Qaysi tuman") #tuman yoki shaxar nomi

    def __str__(self):
        return f"{super().__str__()} MFY"

class Maktab(AutoTime):
    """ Hududlardagi Maktablar """
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Qaysi tuman")
    status = models.CharField(max_length=l, default="O'rta ta'lim maktabi", choices=type_school, blank=True, null=True)

    def __str__(self):
        return f"{super().name}-{self.status}"

class Kollej(AutoTime):
    """ Professionalal ta'lim nomlari """
    type = models.ForeignKey(TypeKollej, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ta'lim muassasasi turi")
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Qaysi tuman")

    def __str__(self):
        return super().__str__()

class Vil(AutoTime):
    """ Viloyatlar nomi """
    status = models.CharField(max_length=l, default="viloyati", choices=vil_status, blank=True, null=True)
    
    def __str__(self):
        return f"{super().__str__()} {self.status}"

class Universitet(AutoTime):
    """ Yangi OTM nomi qo'shish """

    viloyat = models.ForeignKey(Vil, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="viloyat nomi")    
    def __str__(self):
        return super().__str__() 

class Qiziqish(AutoTime):
    """ Bitiruvchini qiziqishlari """
    
    def __str__(self):
        return super().__str__()

class Imkonyat(AutoTime):
    """ Kompyuter Bilimlari """

    def __str__(self):
        return super().__str__()

class ChetTili(AutoTime):
    """ Chet tili """
    def __str__(self):
        return super().__str__()

class Sport(AutoTime):
    """ Sport Turlari """
    def __str__(self):
        return super().__str__()

class DriverLicense(AutoTime):
    """ Haydovchilik guvohnomasi turlari """
    def __str__(self):
        return super().__str__()

class Bitiruvchi(models.Model):
    """ Bitiruvchi xaqidagi toplanadigan umumiy malumotlar """
    author = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)
    f_name = models.CharField(max_length=l, verbose_name="F.I.Sh")
    img  = models.ImageField(default='default/default.png', upload_to='bitiruvchilar-foto/', verbose_name="Rasm")
    t_sana = models.DateField(verbose_name="Tug'ulgan sana", null=True, blank=True)
    jins = models.CharField(max_length=l, choices=jins, verbose_name="Jinsi", default="o'g'il bola")
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Yashaydigan tuman(shahar)")
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, verbose_name="Mahalla Nomi")
    uy = models.CharField(max_length=l, null=True, blank=True, verbose_name="Ko'cha nomi 45uy")
    phone = models.CharField(max_length=9, verbose_name="Telefon raqam (+998) ", null=True, blank=True)
    email = models.EmailField(max_length=l, verbose_name="E-Pochta", null=True, blank=True)
    imkonyat = models.ManyToManyField(Imkonyat, related_name="abilty", verbose_name="Kompyuter bilimi")
    qiziqish = models.ManyToManyField(Qiziqish, related_name="interest", verbose_name="Qiziqish")
    sport = models.ManyToManyField(Sport, related_name="sport", verbose_name="Qiziqadigan sport turi")
    chettili = models.ManyToManyField(ChetTili, related_name="f_lang")
    idea = models.CharField(verbose_name="Biznes g'oya", max_length=l, choices=yesNo, default="Yoq")
    short_f = models.CharField(max_length=10000, verbose_name="Bizness g'oya haqqida qisqacha (agar bor bo'lsa)", null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name    

class MaktabBitiruvchisi(Bitiruvchi):
    """ Maktab Bitiruvchisi """
    tuman_mk = models.ForeignKey(TumanVaShahar, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Maktab manzili")
    maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE, verbose_name="Bitirayotgan maktab")
    sinf = models.CharField(max_length=l, choices=sinf, default='9-sinf', verbose_name="Sinf")
    # topshirgan otm nomi
    vil = models.ForeignKey(Vil, related_name="mk_vil", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="OTM manzili")
    otm_name = models.ForeignKey(Universitet, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Topshirmoqchi bo'lgan OTM Nomi")
    stu_way_un = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    # chet el otm si uchun
    other_un = models.CharField(max_length=l, verbose_name="ChetEl OTM nomi", null=True, blank=True)
    stu_way_ch = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    
    def __str__(self):
        return super().__str__()


class KollejBitiruvchisi(Bitiruvchi):
    """ Professanal ta'lim bitiruvchisi """
    type = models.ForeignKey(TypeKollej, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Professional ta'lim")
    tuman_kj = models.ForeignKey(TumanVaShahar, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kollej manzili")
    kollej = models.ForeignKey(Kollej, on_delete=models.SET_NULL, verbose_name="Bitirayotgan Kollej", null=True, blank=True)
    stu_way = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    maqsad = models.CharField(max_length=l, choices=aim, default="Ishlamoqchi", verbose_name="Maqsadi")
    guvohnoma = models.ManyToManyField(DriverLicense, related_name="guvohnomaK", verbose_name="Haydovchilik Guvohnomasi")
    #topshirgan otm nomi
    vil = models.ForeignKey(Vil, on_delete=models.SET_NULL, null=True, blank=True, related_name="kj_vil",)
    otm_name = models.ForeignKey(Universitet, on_delete=models.SET_NULL, null=True, blank=True)
    stu_way_un = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    #chet el otm uchun
    other_un = models.CharField(max_length=l, null=True, blank=True, verbose_name="chetel otm")
    stu_way_ch = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
  
    def __str__(self):
        return super().__str__()

class UniversitetBitiruvchisi(Bitiruvchi):
    """ OTM bitiruvchisi"""
    vil = models.ForeignKey(Vil, on_delete=models.SET_NULL, null=True, blank=True)
    universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE, verbose_name="Bitirayotgan OTM", null=True, blank=True)
    stu_way = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    #chet el uchun 
    other_un = models.CharField(max_length=l, null=True, blank=True, verbose_name="ChetEl OTM")
    stu_way_ch = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    maqsad = models.CharField(max_length=l, choices=aim, default="Ishlamoqchi", verbose_name="Maqsadi")
    guvohnoma = models.ManyToManyField(DriverLicense, related_name="guvohnomaU", verbose_name="Haydovchilik Guvohnomasi")
    
    def __str__(self):
        return super().__str__()


