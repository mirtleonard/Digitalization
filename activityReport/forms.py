from django.forms import *
from activityReport.models import ActivityReport

class ActivityReportForm(ModelForm):
    username = CharField(widget=HiddenInput())
    class Meta:
        model = ActivityReport
        fields = '__all__'
        widgets = {
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
            'date' :  DateInput(attrs={'type' : 'date'})
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
