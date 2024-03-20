from django import forms

class QuestionLevelForm(forms.Form):
    choices = (('', '---Please choose a level---'), ('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard'))
    label = forms.CharField(label="Choose your question level")
    select = forms.CharField(widget=forms.Select(choices=choices))
    
