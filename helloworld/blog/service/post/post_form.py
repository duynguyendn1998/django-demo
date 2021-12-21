from django import forms
from blog.models import Posts

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['title', 'content_post']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PostCreateForm, self).__init__(*args, **kwargs)

    # The title should be unique per user.
    def clean_title(self):
        title = self.cleaned_data['title']
        if Posts.objects.filter(user=self.user, title=title).exists():
            raise forms.ValidationError("You have already written a Post with same title.")
        return title