from django.forms import *
from activityReport.models import ActivityReport

class ActivityReportForm(ModelForm):
    username = CharField(widget=HiddenInput())
    photos = FileField(required=False, widget=FileInput(attrs = {'multiple' : True}), label="Imagini")
    class Meta:
        model = ActivityReport
        fields = '__all__'
        widgets = {
            'areas' : Select(choices = (
                ('intelectuală', 'intelectuală'),
                ('spirituală', 'spirituală'),
                ('caracter', 'caracter'),
                ('afectivă', 'afectivă'),
                ('socială', 'socială'),
                ('fizică', 'fizică'))),
            'branch' : Select(choices = (
                ('Lupișori', 'Lupișori'),
                ('Temerari', 'Temerari'),
                ('Exploratori', 'Exploratori'),
                ('Seniori', 'Seniori'))),
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
