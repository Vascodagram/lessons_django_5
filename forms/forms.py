from django import forms
from .models import FormCompany


class MyForms(forms.Form):
    name = forms.CharField(label='Name')
    surname = forms.CharField()
    age = forms.IntegerField(max_value=100)
    company = forms.CharField(initial='EPAM')
    salary = forms.IntegerField(required=False)


class FormCompanyModels(forms.ModelForm):
    class Meta:
        model = FormCompany
        fields = ['name', 'surname', 'age', 'company', 'salary']