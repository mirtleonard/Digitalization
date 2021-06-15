from django.forms import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from eventReport.models import EventReport

class EventReportForm(ModelForm):
    username = CharField(widget=HiddenInput())
    class Meta:
        model = EventReport
        fields = '__all__'
        widgets = {
            'endDate' : DateTimeInput(attrs = {'type' : 'datetime-local',}),

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
            'participants' : 'Participanți',
        }
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Adaugă raport', css_class='btn btn-info d-flex justify-content-center'))
