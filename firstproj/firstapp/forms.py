from django import forms    

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100)
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator'))
    numb = forms.IntegerField(label='Number', max_value=9999999999) 
    field = forms.ChoiceField(choices=posts)

