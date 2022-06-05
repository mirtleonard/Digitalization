from django.forms import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from eventReport.models import EventReport

class EventReportForm(ModelForm):
    photos = FileField(required=False, widget=FileInput(attrs = {'multiple' : True}), label="Imagini")
    username = CharField(widget=HiddenInput())
    class Meta:
        model = EventReport
        fields = '__all__'
        widgets = {
            'endDate' : DateTimeInput(attrs = {'type' : 'datetime-local',}),
            'center' : TextInput(attrs = {'placeholder' : 'Centrul local AMD Pildești',}),
            'eventType' : TextInput(attrs = {'placeholder' : 'Local, Regional, Național, Internațional'}),
            'beginingDate' : DateTimeInput(attrs = {'type' : 'datetime-local',})
        }
        labels = {
            'title' : 'Titlu',
            'description' : 'Descriere',
            'location' : 'Locație',
            'center' : 'Centru',
            'eventType' : 'Tip de eveniment',
            'endDate' : 'Data de sfârșit',
            'beginingDate' : 'Data de început',
            'members' : 'Participanți',
            'strengths' : 'Puncte tari',
            'weaknesses' : 'Puncte slabe',
            'goals' : 'Obiective',
        }
