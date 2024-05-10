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
        ('KRW', 'KRW'),
        ('KWD', 'KWD'),
        ('JPY', 'JPY'),
        ('RUB', 'RUB'),
        ('BHD', 'BHD'),
        ('QAR', 'QAR'),
        ('CNY', 'CNY'),
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
            'id': "input_field",
           'class' :"input-field"

        })
                                      )

class OutputForm(forms.Form):
    currency_Output = forms.CharField(
        label='Currency',
        widget=forms.Select(choices=[
            ('', '--Select Currency--'),
            ('USD', 'USD'),
            ('AED', 'AED'),
            ('SAR', 'SAR'),
            ('EGP', 'EGP'),
            ('EUR', 'EUR'),
            ('KRW', 'KRW'),
            ('KWD', 'KWD'),
            ('JPY', 'JPY'),
            ('RUB', 'RUB'),
            ('BHD', 'BHD'),
            ('QAR', 'QAR'),
            ('CNY', 'CNY'),
        ],
            attrs={
                'id': "currency_output",
                'class': "input-field",
                'name': "currency_Output"}
        ), )

    output_currency = forms.FloatField(
        label='Output currency',
        disabled=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': '1.00 ',
                'id': "output_field",
                'class': "output-field"

            })

    )
