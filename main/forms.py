from django import forms
from .widget import DatePicker
from django.urls import reverse_lazy

from .models import (
    Kollej,
    Maktab, 
    Mahalla, 
    Imkonyat, 
    Bitiruvchi,
    Universitet,
    KollejBitiruvchisi, 
    MaktabBitiruvchisi, 
    UniversitetBitiruvchisi,
) 

imk = Imkonyat.objects.all()

class MaktabForm(forms.ModelForm):
    class Meta:
        model = MaktabBitiruvchisi
        fields = '__all__'

        widgets = {
            'f_name': forms.TextInput(attrs={
                'class':'form-control w-50',
                'placeholder':'Turg\'unov Zohidillo Muhammad o\'g\'li'
            }),
            'img': forms.FileInput(attrs={
                'display':"none"
            }),
            'tuman_mk':forms.Select(attrs={
                'id':'tuman_mk',
                'class':'form-select',
            }),
            'tuman':forms.Select(attrs={
                'class':'form-select',
            }),
            'uy':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Guldiyor ko\'chasi 204uy'
            }),
            'mahalla': forms.Select(attrs={
                "id":"mahalla",
                'class':'form-select',
                'mahalla-queries-url':reverse_lazy("ALM"),
            }),
            'maktab': forms.Select(attrs={
                "id":"maktab",
                'class':'form-select',
                'maktab-queries-url':reverse_lazy("ALMa"),
            }),
            'imkonyat':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'qiziqish':forms.Select(attrs={
                'class':'form-control',
            }),
            'chettili':forms.SelectMultiple(),
            't_sana': forms.SelectDateWidget(attrs={
                'id':"datepicker",
                'class':'form-control'
            },years=range(1950, 2023)),
            'phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'332300701'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'example@domain.com'
            }),
            'sport':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'chettili':forms.SelectMultiple(attrs={
                "class":'form-control',
            }),
            'idea':forms.Select(attrs={
                'class':'form-control',
            }),
            'short_f':forms.TextInput(attrs={
                'placeholder':"Misol: 'ishlab chiqarish'",
                'class':'form-control w-75',
                'disabled':'true'
            }),
            'univer_sity':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Toshkent axborot texnologiyalar universiteti'
            }),
            'jins':forms.Select(attrs={
                'class':'form-select'
            }),
            'vil':forms.Select(attrs={
                'id':'vil',
                'class':'form-select',
            }),
            'otm_name':forms.Select(attrs={
                'id':'otm_name',
                'class':'form-select',
                'otm-queries-url':reverse_lazy("ALO"),
            }),
            'stu_way_un':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Misol: Dasturchi**'
            }),
            'stu_way_ch':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Mutaxasisligi'
            }),
            'other_un':forms.TextInput(attrs={
                'class':'form-control w-50',
                'placeholder':'Boshqa OTM'
            }),
            'maqsad':forms.Select(attrs={
                'class':'form-select'
            }),
            'sinf':forms.Select(attrs={
                'class':'form-select'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()
        self.fields['maktab'].queryset = Maktab.objects.none()
        self.fields['otm_name'].queryset = Universitet.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
                # self.fields['maktab'].queryset = Maktab.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['mahalla'].queryset = self.instance.tuman.mahalla_set.all() 
            # self.fields['maktab'].queryset = self.instance.tuman.maktab_set.all() 
        
        if 'tuman_mk' in self.data:
            try:
                tuman_id = int(self.data.get('tuman_mk'))
                self.fields['maktab'].queryset = Maktab.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['maktab'].queryset = self.instance.tuman.maktab_set.all()

        # if 'vil' in self.data:
        #     try: 
        #         vil_id = int(self.data.get('vil'))
        #         print("forms.py ", vil_id)
        #         self.fields['otm_name'].queryset = Universitet.objects.filter(viloyat_id=vil_id).all()
        #     except (ValueError, TypeError):
        #         pass
        # elif self.instance.pk:
        #     self.fields['otm_name'].queryset = self.instance.vil.universitet_set.all()



class KollejForm(forms.ModelForm):
    class Meta:
        model = KollejBitiruvchisi
        fields = '__all__'

        widgets = {
            'f_name': forms.TextInput(attrs={
                'class':'form-control w-50',
                'placeholder':'Turg\'unov Zohidillo Muhammad o\'g\'li'
            }),
            'img': forms.FileInput(attrs={
                'display':"none"
            }),
            'tuman':forms.Select(attrs={
                'class':'form-select',
            }),
            'uy':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Guldiyor ko\'chasi 204uy'
            }),
            'mahalla': forms.Select(attrs={
                "id":"mahalla",
                'class':'form-select',
                'mahalla-queries-url':reverse_lazy("ALM"),
            }),
            'kollej': forms.Select(attrs={
                "id":"kollej",
                'class':'form-select',
                # 'kollej-queries-url': reverse_lazy("ALK"),
                'typekollej-queries-url': reverse_lazy("ALTK"),
            }),
            'imkonyat':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'qiziqish':forms.Select(attrs={
                'class':'form-control',
            }),
            'chettili':forms.CheckboxSelectMultiple(),
            't_sana': forms.SelectDateWidget(attrs={
                'id':"datepicker",
                'class':'form-control'
            },years=range(1950, 2023)),
            'phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'332300701'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'example@domain.com'
            }),
            'sport':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'chettili':forms.SelectMultiple(attrs={
                "class":'form-control',
            }),
            'idea':forms.Select(attrs={
                'class':'form-control',
            }),
            'short_f':forms.TextInput(attrs={
                'placeholder':"Misol: 'ishlab chiqarish'",
                'class':'form-control w-75',
                'disabled':'true'
            }),
            'univer_sity':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Toshkent axborot texnologiyalar universiteti'
            }),
            'guvohnoma':forms.SelectMultiple(attrs={
                'class':'form-select',
            }),
            'tuman_kj': forms.Select(attrs={
                'id':'tuman_kj',
                'class':'form-select',
            }),
            'stu_way':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Kompyuter injenering',
            }),
            'type':forms.Select(attrs={
                'id':'type',
                'class':'form-select',    
            }),
            'maqsad':forms.Select(attrs={
                'class':'form-select'
            }),
            'jins':forms.Select(attrs={
                'class':'form-select'
            }),
            'other_un':forms.TextInput(attrs={
                'placeholder':'Boshqa OTM nomi',
                'class':'w-75'
            }),
            'stu_way_un':forms.TextInput(attrs={
                'placeholder':'Mutaxasisligi'
            }),
            'stu_way_ch':forms.TextInput(attrs={
                'placeholder':'Mutaxasisligi'
            }),
            'vil':forms.Select(attrs={
                'id':'vil',
            }),
            'otm_name':forms.Select(attrs={
                'id':'otm_name',
                'otm-queries-url':reverse_lazy("ALO"),
            })

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()
        self.fields['kollej'].queryset = Kollej.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get("tuman"))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['mahalla'].queryset = self.instance.tuman.mahalla_set.all()
        
        if 'tuman_kj' in self.data:
            try:
                tuman_id = int(self.data.get("tuman_kj"))
                self.fields['kollej'].queryset = Kollej.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['kollej'].queryset = self.instance.tuman.kollej_set.all()
        
class UniversitetForm(forms.ModelForm):
    class Meta:
        model = UniversitetBitiruvchisi
        fields = '__all__'

        widgets = {
            'mahalla': forms.Select(attrs={
                'id':'mahalla',
                'mahalla-queries-url':reverse_lazy("ALM")
            }),
            'universitet':forms.Select(attrs={
                'id':'otm_name',
                'otm-queries-url':reverse_lazy("ALO"),
            }),
            'imkonyat':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'qiziqish':forms.Select(attrs={
                'class':'form-control',
            }),
            'chettili':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'sport':forms.SelectMultiple(attrs={
                'class':'form-control'
            }),
            't_sana':forms.SelectDateWidget(years=range(1950, 2023)),
            'f_name':forms.TextInput(attrs={
                'placeholder':"Turg'unov Zohidillo Muhammad o'g'li",
                'class':'w-50',
            }),
            'uy':forms.TextInput(attrs={
                'placeholder':'Guldiyor ko\'chasi 204uy',
            }),
            'short_f':forms.TextInput(attrs={
                'placeholder':"Misol: 'ishlab chiqarish'",
                'class':'form-control w-75',
                'disabled':'true'
            }),
            'other_un':forms.TextInput(attrs={
                'placeholder':'Boshqa OTM nomi',
                'class':'w-75'

            }),
            'stu_way':forms.TextInput(attrs={
                'placeholder':'Mutaxasisligi'
            }),
            'stu_way_ch':forms.TextInput(attrs={
                'placeholder':'Mutaxasisligi'
            }),
            'phone':forms.TextInput(attrs={
                'placeholder':'332300701'
            }),
            'email':forms.TextInput(attrs={
                'placeholder':'example@domain.com'
            }),
            'vil':forms.Select(attrs={
                'id':'vil',
            }),
            'guvohnoma':forms.SelectMultiple(attrs={
                'class':'form-select'
            }),
            'img': forms.FileInput(attrs={
                'display':"none"
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get("tuman"))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['mahalla'].queryset = self.instance.tuman.mahalla_set.all()

class BitiruvchiForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()
        self.fields['maktabbitiruvchisi__maktab'].queryset = Maktab.objects.none()
        self.fields['kollejbitiruvchisi__kollej'].queryset = Kollej.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id)
            except (TypeError, ValueError):
                pass

class MaktabFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()
        self.fields['maktab'].queryset = Maktab.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
                self.fields['maktab'].queryset = Maktab.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass


class KollejFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass

class UniversiterFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get("tuman"))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass

class MaktabNameForm(forms.ModelForm):
    class Meta:
        model = Maktab
        fields = '__all__'

class KollejNameForm(forms.ModelForm):
    class Meta:
        model = Kollej
        fields = '__all__'

class UniversitetNameForm(forms.ModelForm):
    class Meta:
        model = Universitet
        fields = '__all__'

class BitiruvchiFilterForm(forms.ModelForm):
    pass