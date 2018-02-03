from django import forms

from .models import ValidWord

class ValidWordForm(forms.ModelForm):

	class Meta:
		model = ValidWord
		fields = ('inputword',)