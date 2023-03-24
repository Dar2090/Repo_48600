from django import forms
class CursoForm(forms.Form):
    name = forms.CharField(max_length=20)
    n_camada = forms.IntegerField()


