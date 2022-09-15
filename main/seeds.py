import random
from unicodedata import name

from .models import (
    Vil, 
    Sport as Sp,
    Kollej as KJ,
    Maktab as MK,
    Mahalla as Mh,
    ChetTili as Fl,
    Qiziqish as Qz,
    Imkonyat as Im,
    TypeKollej as TK,
    Universitet as OTM,
    DriverLicense as DL,
    TumanVaShahar as TS,
    KollejBitiruvchisi as KB,
    MaktabBitiruvchisi as MB,
    UniversitetBitiruvchisi as UB
)

from faker import Faker as FK
from django.contrib.auth import get_user_model

Users = get_user_model()

data_add = Users.objects.filter(data_add=True).all()

fk = FK()
qz = Qz.objects.all()
tk = TK.objects.all()
otm = OTM.objects.all()
vil_ = Vil.objects.all()
tuman = TS.objects.all()
maktab = MK.objects.all()
kollej = KJ.objects.all()
mahalla = Mh.objects.all()
imkonyat = Im.objects.all()

def generater(obj):
    list = [obj.get(id=i.id) for i in obj]
    return random.choice(list)

def maktab_db(n):
    """ Tumanlarga fake maktablar qo'shish test uchun """
    for i in tuman:
        for r in range(0, n):
            MK.objects.create(
                name = random.randint(1, 90),
                tuman = TS.objects.get(id=i.id),
                status = random.choice(["O'rta ta'lim maktabi", "O'rta ta'lim maktabi", "O'rta ta'lim maktabi", "Ixtisoslashgan maktablar"])
            )

def kollej_db(n):
    for i in tuman:
        for k in range(0, n):
            KJ.objects.create(
                name = f"{random.randint(0, 15)}-sonli professanal ta'lim",
                type = generater(tk),
                tuman = tuman.get(id=i.id)
            )

def mahalla_db(n):
    for i in tuman:
        for _ in range(0, n):
            Mh.objects.create(
                name = fk.city(),
                tuman = TS.objects.get(id=i.id)
            )

def mk_db(n):
    for _ in range(0, n):
        for t in tuman:
            for m in maktab.filter(tuman=t.id):
                instance = MB.objects.create(
                    author = random.choice(data_add),
                    f_name = fk.name(),
                    t_sana = fk.date_of_birth(minimum_age=18, maximum_age=25),
                    jins = random.choice(["o'g'il bola", "o'g'il bola", "qiz bola"]),
                    tuman = tuman.get(id=t.id),
                    mahalla = random.choice(mahalla.filter(tuman=t.id)),
                    uy = fk.building_number(),
                    phone = f"{fk.msisdn()[:8]}",
                    email = fk.ascii_safe_email(),
                    qiziqish = generater(qz),
                    tuman_mk = tuman.get(id=m.tuman.id),
                    maktab = maktab.get(id=m.id),
                    sinf = random.choice(['9-sinf', '11-sinf', '11-sinf']),
                    vil = generater(vil_),
                    otm_name = generater(otm),
                    stu_way_un = fk.job(),
                )
                instance.imkonyat.set(imkonyat)
                instance.sport.set(Sp.objects.all())
                instance.chettili.set(Fl.objects.all())

def kj_db(n):
    for _ in range(0, n):
        for t in tuman:
            for m in kollej.filter(tuman=t.id):
                instance = KB.objects.create(
                    author = random.choice(data_add),
                    f_name = fk.name(),
                    t_sana = fk.date_of_birth(minimum_age=18, maximum_age=25),
                    jins = random.choice(["o'g'il bola", "o'g'il bola", "qiz bola"]),
                    tuman = tuman.get(id=t.id),
                    mahalla = random.choice(mahalla.filter(tuman=t.id)),
                    uy = fk.building_number(),
                    phone = f"{fk.msisdn()[:8]}",
                    email = fk.ascii_safe_email(),
                    qiziqish = generater(qz),
                    maqsad = random.choice(["O'qishni davom etirmoqchi", "O'qishni davom etirmoqchi", "Ishlamoqchi"]),
                    type = generater(tk),
                    tuman_kj = tuman.get(id=m.tuman.id),
                    kollej = kollej.get(id=m.id),
                    stu_way = fk.job(),
                )
                instance.imkonyat.set(imkonyat)
                instance.sport.set(Sp.objects.all())
                instance.chettili.set(Fl.objects.all())
                instance.guvohnoma.set(DL.objects.all())

def un_db(n):
    for _ in range(0, n):
        for t in tuman:
            for v in vil_:
                for m in otm.filter(viloyat=v.id):
                    instance = UB.objects.create(
                        author = random.choice(data_add),
                        f_name = fk.name(),
                        t_sana = fk.date_of_birth(minimum_age=18, maximum_age=25),
                        jins = random.choice(["o'g'il bola", "o'g'il bola", "qiz bola"]),
                        tuman = tuman.get(id=t.id),
                        mahalla = random.choice(mahalla.filter(tuman=t.id)),
                        uy = fk.building_number(),
                        phone = f"{fk.msisdn()[:8]}",
                        email = fk.ascii_safe_email(),
                        qiziqish = generater(qz),
                        maqsad = random.choice(["O'qishni davom etirmoqchi", "O'qishni davom etirmoqchi", "Ishlamoqchi"]),
                        vil = vil_.get(id=m.viloyat.id),
                        universitet = otm.get(id=m.id),
                        stu_way = fk.job(),
                    )
                    instance.imkonyat.set(imkonyat)
                    instance.sport.set(Sp.objects.all())
                    instance.chettili.set(Fl.objects.all())
                    instance.guvohnoma.set(DL.objects.all())

def generate_db(mk, kj, un):
    mk_db(mk)
    kj_db(kj)
    un_db(un)