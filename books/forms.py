from django import forms
from django.core.exceptions import ValidationError
from .models import Book, Category

###################################################################################
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean(self):
        super(CategoryForm, self).clean()
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError("Title Length should be At least 2")
        return self.cleaned_data

#################################################################################
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # exclude = ("isbn",)

    def clean(self):
        super(BookForm, self).clean()
        title = self.cleaned_data.get('title')
        category = self.cleaned_data.get('categories')
        if len(title) < 10 or len(title) > 50:
            raise ValidationError("Title Length should be between 10 and 50")
        if len(category) < 2:
            raise ValidationError("category Length should be At least 2")
        return self.cleaned_data