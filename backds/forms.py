from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=250,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))



class RegisterAnswer(forms.Form):
    name_e_p = forms.CharField(label="¿Como se llama tu proyecto/empresa?", max_length=30, widget=forms.Textarea(attrs={'class':'input'}))
    segmento_propuesta = forms.CharField(label="¿De qué se trata tu proyecto o negocio? ¿Qué quieres lograr? ",
                                         max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
    segmento = forms.CharField(label="¿Para quiénes son tus productos o servicios? ¿Cómo son esas personas u organizaciones?: ",
                               max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
    propuesta = forms.CharField(label="¿Qué problema resuelves o qué necesidad cubres para tus clientes? ", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
    canales = forms.CharField(label="¿Cómo llegarán tus productos o servicios a tus clientes? ¿Cómo los encontrarán? ",
                              max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
    relaciones = forms.CharField(label="¿Cómo te relacionarás con tus clientes? ¿Cómo los tratarás? ",
                                 max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
    recursos = forms.CharField(label="¿Qué cosas necesitas para hacer que tu proyecto funcione? ¿Qué es esencial? ",
                               max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
    actividades = forms.CharField(label="¿Qué cosas tendrás que hacer todos los días para que tu proyecto funcione bien? ",
                                  max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
    socios = forms.CharField(label="¿Trabajarás con otras personas o empresas en tu proyecto? ",
                             max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
