from django import forms
from .models import Games


class GameIntakeForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ('genre', 'name', 'description', 'image', 'price', 'on_sale', 'developer', 'release_date')
        widgets = {
            'genre': forms.Select(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'name': forms.TextInput(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'image': forms.FileInput(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'on_sale': forms.CheckboxInput(),
            'developer': forms.Select(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'release_date': forms.widgets.DateInput(attrs={'type': 'date', 
                'class': 'mx-3 gap-4 w-1/6 h-1/2 py-4 px-6 rounded-xl'
            })
        }
        
class GameEditForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ('genre', 'name', 'description', 'image', 'price', 'on_sale', 'developer', 'release_date')
        widgets = {
            'genre': forms.Select(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'name': forms.TextInput(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'image': forms.FileInput(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'on_sale': forms.CheckboxInput(),
            'developer': forms.Select(attrs={
                'class': 'mx-3 gap-4 w-1/2 h-1/2 py-4 px-6 rounded-xl'
            }),
            'release_date': forms.widgets.DateInput(attrs={'type': 'date', 
                'class': 'mx-3 gap-4 w-1/6 h-1/2 py-4 px-6 rounded-xl'
            })
        }