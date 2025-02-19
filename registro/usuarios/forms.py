from django import forms

class RegistroUsuarioForms(forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput)
    password_confirmar= forms.CharField(widget= forms.PasswordInput)
    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker', 'data-date-format': 'yyyy-mm-dd'}))
    
  #funcion para validar email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == "existe@gmail.com":
            raise forms.ValidationError("Este ya existe") 
        return email 
     

#funcion para validar contraseña     
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password)<8:
            raise forms.ValidationError('La contraseña debe tener minimo 8 caracteres')
        return password

#funcion para validar contraseña     
    def clean_password_confirmar(self):
        password = self.cleaned_data.get('password')
        password_confirmar = self.cleaned_data.get('password_confirmar')
        if password!=password_confirmar:
            raise forms.ValidationError('La contraseña no son iguales')
        return password_confirmar
    