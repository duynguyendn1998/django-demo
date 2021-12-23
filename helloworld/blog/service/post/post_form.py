from django import forms
from blog.models import Category, Posts

# Post create form 
class PostCreateForm(forms.ModelForm):
    categories  = forms.ModelMultipleChoiceField(queryset=None,
                    widget=forms.CheckboxSelectMultiple,
                    required=True,) #show list category is check box 
    content_post = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Please enter content post',
                                                            'class': 'form-control'})) # Create field content of post redesign to text area 

    class Meta:
        model = Posts #Model use
        fields = ['title', 'content_post','categories',] # Define fields in form

    def __init__(self, *args, **kwargs): # Init data for form
        self.user = kwargs.pop('request') # get current user
        super(PostCreateForm, self).__init__(*args, **kwargs) 
        self.fields['categories'].queryset = Category.objects.order_by("name") # load category list for field categories


    # The title should be unique per user.
    def clean_title(self):
        title = self.cleaned_data['title']
        if Posts.objects.filter(user=self.user, title=title).exists(): #If title is exists to show error
            raise forms.ValidationError("You have already written a Post with same title.")
        return title

class PostUpdateForm(forms.ModelForm):
    categories  = forms.ModelMultipleChoiceField(queryset=Category.objects.prefetch_related(),
                    widget=forms.CheckboxSelectMultiple,
                    required=True,)
    content_post = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Posts
        fields = ['title', 'content_post','categories',]

