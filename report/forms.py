from django.forms import *
from report.models import Report

class style(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})

class reportForm(style):
    class Meta:
        model = Report
        filed = '__all__'
        exclude = ['username']
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
            'location' : Select(choices = (
                ('exterior', 'exterior'),
                ('interior', 'interior'))),
            'branch' : Select(choices = (
                ('Lupisori', 'Lupisori'),
                ('Temerari', 'Temerari'),
                ('Exploratori', 'Exploratori'))),
            'date' : SelectDateWidget()
            }
        labels = {
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
