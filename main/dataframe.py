
"""
    example
    data = { 
            'id': [i.id for i in Test.h], 
            'Full Name': [i.name for i in Test.h], 
            'Age': [i.age for i in Test.h], 
            'Address': [i.address for i in Test.h], 
            'Birth Day': [i.birth_day for i in Test.h], 
            'Thing Name': [i.thing.name for i in Test.h], 
            'MoreThing Name': [str([a.name for a in i.morething.all()])[1:-1] for i in Test.h], 
            'MoreThing 2 Name': [str([a.name for a in i.morething2.all()])[1:-1] for i in Test.h] , 
        } 
"""
def database(table):
    data_table = {
        # 'id': [i.id for i in table],
        # 'F.I.SH': [i.f_name for i in table],
        # 'Tug\'ulgan san': [i.t_sana for i in table],
        # 'Jins': [i.jins for i in table],
        # 'Yashash manzili': f"{[i.tuman.name for i in table]} {[i.mahalla.name for i in table]} {[i.uy for i in table]}",
        # 'Aloqa': f"{[i.phone for i in table]} n\ {[i.email for i in table]}",
        # 'Kompyuter bilimi': [str([a.name for a in i.imkonyat.all()])[1:-1] for i in table],
        # 'Qiziqishlari': [i.qiziqish for i in table],
        # 'Yoqtirgan sport turi': [i.sport for i in table],
        # 'Chet el tili': [str([a.name for a in i.chettili.all()])[1:-1] for i in table],
        # 'Bizness G\'oya': [i.idea for i in table],
        # 'Bizness G\'oya xaqida': [i.short_f for i in table],
        # 'Maqsadi': ,
        # 'Guvohnoma': ,
        # 'Tugatayotgan ta\'lim muassasi manzili':[i.maktabbitiruvchisi.tuman_mk if i.maktabbitiruvchisi.tuman_mk else i.kollejbitiruvchisi.tuman_kj if i.kollejbitiruvchisi.tuman_kj else i.universitetbitiruvchisi.vil for i in table ],
        # 'Tugatayotgan ta\'lim muassasi turi':[i.maktabbitiruvchisi.status for i in table] if table.maktabbitiruvchisi else [i.kollejbitiruvchisi.type for i in table] if table.kollejbitiruvchisi else 'OTM',
        # 'Tugatayotgan ta\'lim muassasi ':[i.maktabbitiruvchisi.maktab for i in table] if table.maktabbitiruvchisi else [i.kollejbitiruvchisi.kollej for i in table] if table.kollejbitiruvchisi else [i.universitetbitiruvchisi.universitet for i in table] if table.universitetbitiruvchisi else [i.universitetbitiruvchisi.other_un for i in table],
        # 'Mutaxasisligi/Sinf ':[i.maktabbitiruvchisi.sinf for i in table] if table.maktabbitiruvchisi else [i.kollejbitiruvchisi.stu_way for i in table] if table.kollejbitiruvchisi else [i.universitetbitiruvchisi.stu_way for i in table] if table.universitetbitiruvchisi else [i.universitetbitiruvchisi.stu_way_ch for i in table],
        # 'Topshirmoqchi bo\'lgan OTM manzili' : [i.maktabbitiruvchisi.vil for i in table] if table.maktabbitiruvchisi else [i.kollejbitiruvchisi.vil for i in table],
        # 'Topshirmoqchi bo\'lgan OTM nomi' : [i.maktabbitiruvchisi.otm_name for i in table] if table.maktabbitiruvchisi.otm_name else [i.maktabbitiruvchisi.other_un for i in table] if table.maktabbitiruvchisi.other_un else [i.kollejbitiruvchisi.otm_name for i in table] if table.kollejbitiruvchisi.otm_name else [i.kollejbitiruvchisi.other_un for i in table],
        # 'Topshirmoqchi bo\'lgan OTM mutaxasisligi' : [i.maktabbitiruvchisi.stu_way_un for i in table] if table.maktabbitiruvchisi.otm_name else [i.maktabbitiruvchisi.stu_way_ch for i in table] if table.maktabbitiruvchisi.other_un else [i.kollejbitiruvchisi.stu_way_un for i in table] if table.kollejbitiruvchisi.stu_way_ch else [i.kollejbitiruvchisi.other_un for i in table],
    }
    # data_table['Maqsadi'] = [i.kollejbitiruvchisi.maqsad for i in table] if table.kollejbitiruvchisi else [i.universitetbitiruvchisi.maqsad for i in table]
    # data_table['Guvohnoma'] = [str([a.name for a in i.kollejbitiruvchisi.all()]) for i in table] if table.kollejbitiruvchisi else [str([a.name for a in i.kollejbitiruvchisi.all()]) for i in table]
    for i in table:
        data_table["id"] = i.id
        data_table["F.I.SH"] = i.f_name
        data_table["Tug'ulgan san"] = i.t_sana
        data_table["Jins"] = i.jins
        data_table["Yashaydigan tuman"] = i.tuman.name
        data_table["Yashaydigan mahalla"] = i.mahalla.name
        data_table["Yashaydigan xonodon"] = i.uy
        data_table["Telefon raqam"] = i.phone
        data_table["E-Pochta"] = i.email
        data_table["Kompyuter bilmi"] = [a.name for a in i.imkonyat.all()][1:-1]
        data_table["Qiziqish"] = i.qiziqish
        data_table["Yoqtirgan sport turi"] = [a.name for a in i.sport.all()][1:-1]
        data_table["ChetEl tili"] = [a.name for a in i.chettili.all()][1:-1]
        data_table["Bizness go'ya"] = i.idea
        data_table["Bizness go'ya xaqida"] = i.short_f
        
    return data_table