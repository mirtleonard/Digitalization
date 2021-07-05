from django.forms import *
from user.models import User

class registerForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput(), required=True, label=('Repeta parola'))
    password = CharField(widget=PasswordInput(), required=True, label=('Parola'))
    birth = DateField(widget=DateInput(attrs = {'type' : 'date'}))
    username = CharField(required=True, label=('Nume'), error_messages={'unique':'Există deja utilizatorul cu numele introdus.'})
    email = EmailField(required=True, error_messages={'unique' : 'Există deja utilizator cu acest email.'})
    class Meta:
        model = User
        fields = ['username', 'email', 'branch','birth', 'password']
        widgets = {
            'branch' : Select(choices = (
                ('Lupisori', 'Lupisori'),
                ('Temerari', 'Temerari'),
                ('Exploratori', 'Exploratori'))),
        }
        labels = {
            'username' : 'Nume',
            'email' : 'Email',
            'birth' : 'Data de nastere',
            'password' : 'Parola',
            'branch' : 'Ramură',
        }

    def clean(self):
        super(registerForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self._errors['password'] = self.error_class(['Parolele nu se potrivesc!'])
        return self.cleaned_data
