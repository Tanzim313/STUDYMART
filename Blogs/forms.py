from django import  forms

class TeacherRegistration(forms.Form):
    
    first_name = forms.CharField(
        max_length=50,
        label="Enter Your First Name",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First name'})
    )
    
    last_name  = forms.CharField(
        max_length=50,
        label="Last Name",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last name'})
    )
    email = forms.EmailField(
        max_length=50,
        label="E-mail",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter email address'})
    )
    password = forms.CharField(
        max_length=50,
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    textarea = forms.CharField( widget= forms.Textarea )
    file = forms.CharField( widget= forms.FileInput)
    cheackbox = forms.CharField( widget= forms.CheckboxInput )
    