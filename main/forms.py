from django import forms
from datetime import datetime

from .models import *
from django.forms.models import BaseModelFormSet


class PostForm(forms.ModelForm):
    created = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('user',)


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)


class BaseImageFormSet(BaseModelFormSet):
    def clean(self):
        if any(self.errors):
            return
        for form in self.forms:
            image = form['image'].data
            if not image:
                raise (forms.ValidationError("Нужна картинка"))


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)