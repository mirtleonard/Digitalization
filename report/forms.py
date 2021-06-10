from django.forms import *
from report.models import Report

class DateInput(DateInput):
    input_type = 'date'

class Style(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})

class reportForm(Style):
    username = CharField(widget=HiddenInput())
    class Meta:
        model = Report
        fileds = '__all__'
        exclude = ()
        widgets = {
            'description' : Textarea(
                attrs = {'class':'form-control'}),
            'areas' : Select(choices = (
                ('intelectuala', 'intelectuala'),
                ('spirituala', 'spirituala'),
                ('caracter', 'caracter'),
                ('afectiva', 'afectiva'),
                ('sociala', 'sociala'),
                ('fizica', 'fizica'))),
            'branch' : Select(choices = (
                ('Lupisori', 'Lupisori'),
                ('Temerari', 'Temerari'),
                ('Exploratori', 'Exploratori'))),
            'date' : DateInput()
            }
        labels = {
            'materials' : 'Materiale necesare',
            'title' : 'Titlu',
            'description' : 'Descriere',
            'areas' : 'Arie de dezvoltare',
            'location' : 'Locație',
            'branch' : 'Ramură',
            'date' : 'Dată',
            'goals' : 'Obiective',
            'improvements' : 'Imbunătățiri',
            'strengths' : 'Puncte tari',
            'weaknesses' : 'Puncte slabe',
            'duration' : 'Durată',
            'participants' : 'Participanți'
        }

class reportFilter(reportForm):
    class Meta:
        exclude = ()
