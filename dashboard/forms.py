from django.shortcuts import get_object_or_404
from post.models import Post
from django.contrib.auth.models import User
from django import forms

class PostForm(forms.ModelForm):
    creator = forms.CharField(required=False, widget=forms.HiddenInput())
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    cover_image = forms.ImageField()

    class Meta:
        model = Post
        fields = ('title', 'content', 'cover_image')

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        post.creator = get_object_or_404(User, pk=self.cleaned_data['creator'])
        post.likes = forms.TextInput()
        post.views = forms.TextInput()

        if commit:
            post.save()
        return post