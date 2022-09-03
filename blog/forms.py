import re
from django import forms

from blog.models import BlogNew


class AddNewForm(forms.ModelForm):
    """Form for adding news for customer by model NewBlog."""
    class Meta:
        model = BlogNew
        fields = ['title', 'content', 'category', 'is_published']
        widgets = {
                'title': forms.TextInput(attrs={}),
                'content': forms.Textarea(attrs={'rows': 5}),
                'category': forms.Select(),

                }

    def clean_title(self):
        """Custom validation title from form."""
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise forms.ValidationError('Название не должно начинаться с цифры')
        return title





