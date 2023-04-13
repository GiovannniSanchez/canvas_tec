from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label = "Titulo de tarea", max_length=250,
                            widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class':'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="nombre del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))


class RegisterAnswer(forms.Form):
     answer1=forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class':'input'}))
     answer2 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
     answer3 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
     answer4 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
     answer5 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
     answer6 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
     answer7 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
     answer8 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
     answer9 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
     answer10 = forms.CharField(label="Pregunta 1", max_length=1000, widget=forms.Textarea(attrs={'class': 'input'}))
