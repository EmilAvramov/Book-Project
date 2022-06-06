from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, help_text="25 characters max.")
    email = forms.EmailField(help_text="Example: johndoe@email.com")
    to = forms.EmailField(help_text="Example: johndoe@email.com")
    comments = forms.CharField(required=False, widget=forms.Textarea)
