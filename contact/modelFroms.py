from django  import forms
from .models import Message

class ContacForm(forms.ModelForm):
    issue = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Asunto del mensaje'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Correo electronico'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Mensaje o consulta'}))

    def __init__(self, *args, **kwargs):
        super(ContacForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class', '')
                    classes += ' is-invalid'
                    self.fields[f_name].widget.attrs['class'] = classes

    class Meta:
        model = Message
        fields = ('issue', 'email', 'content')
