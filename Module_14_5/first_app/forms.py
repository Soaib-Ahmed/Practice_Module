from django import forms
from .models import MyModel

class ExampleForm(forms.Form):
    name = forms.CharField()

    comment_textarea = forms.CharField(widget=forms.Textarea)

    comment_textarea_attr = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    email = forms.EmailField()

    agree = forms.BooleanField()

    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))


    value = forms.DecimalField()

    message = forms.CharField(max_length=10, min_length=3)

    custom_label = forms.EmailField(label="Please enter your email address")

    first_name = forms.CharField(initial='Your name')

    agree = forms.BooleanField(initial=True)

    day = forms.DateField(initial='2023-01-01')

    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'