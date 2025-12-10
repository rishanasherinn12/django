from django import forms
from .models import BookData



class Bookform(forms.ModelForm):
    class Meta:
        model = BookData
        fields = '__all__'

        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'book_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'book_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'book_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Book Price'}),
            'book_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }





# class Bookform(forms.ModelForm):
#     class Meta:
#         model = BookData
#         fields = '__all__'
         
#     def __init__(self, *args, **kwargs):
#         super(Bookform, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
            
#             field.widget.attrs['placeholder'] = field.label


