from django import forms

class InputForm(forms.Form):
    currency_input = forms.CharField(
        label='Currency',
        widget=forms.Select(choices=[
        ('', '--Select Currency--'),
        ('USD', 'USD'),
        ('AED', 'AED'),
        ('SAR', 'SAR'),
        ('EGP', 'EGP'),
        ('EUR', 'EUR'),
    ],
    attrs = {
        'id':"currency_input",
        'class' :"input-field",
        'name' : "currency_input" }
    ), )


    input_currency = forms.FloatField(
        label='Input currency',
        widget=forms.NumberInput(
        attrs={
            'placeholder': 'Enter currency value here',
            'id': "input-currency",
           'class' :"input-field"

        })
                                      )

class OutputForm(forms.Form):
    currency_output = forms.CharField(label='Currency', widget=forms.Select(choices=[
        ('', '--Select Currency--'),
        ('USD', 'USD'),
        ('AED', 'AED'),
        ('SAR', 'SAR'),
        ('EGP', 'EGP'),
        ('EUR', 'EUR'),
    ],
        attrs={
            'id': "currency_output",
            'class': "output-field",
            'name': "currency_input"}
    ))
    output_currency = forms.FloatField(
        label='Output currency',
        disabled=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': '1.00 ',
                'id': "output-currency",
                'class': "output-field"

            })

    )
