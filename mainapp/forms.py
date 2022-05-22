from django import forms
from .models import *



class GalleryForm(forms.ModelForm):
	
	title=forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control','Placeholder':'Enter Title of the images','rows':1}), label='')
	page_image=forms.ImageField( help_text='<br><span style="color: red;">Select Gallery Cover</span>', widget=forms.FileInput(),required=False, label='')
	image=forms.ImageField(widget=forms.FileInput(attrs={"multiple":"True",}),required=False, label='')



	class Meta:

		model=Gallery
		fields = ['title','page_image']

