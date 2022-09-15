from django import forms

class DatePicker(forms.DateInput):
    input_type = 'date'
    