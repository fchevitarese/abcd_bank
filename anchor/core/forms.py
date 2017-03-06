from django import forms


class UploadForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Credit card number'}),
        required=False,
        help_text='You can add your credit card numbers, 1 per line.',
        label='Credit card list')

    file = forms.FileField(
        required=False,
        label='File with the numbers.',
        help_text='Upload file'
    )

