from django import forms


class MacroForm(forms.Form):
    macro = forms.DecimalField(label='Macro', min_value=0, max_value=100, max_digits=3)


