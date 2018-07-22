from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario


class CustomUserCreationForm(forms.ModelForm):

    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden",
    }

    email = forms.EmailField(
        _('email address'),
        widget=forms.EmailInput(attrs={'placeholder': 'Correo'})
    )
    numero_identificacion = forms.CharField(
        _('número identificación'), 
        widget=forms.TextInput(
        attrs={'placeholder': 'Número identificación'})
    )
    telefono = forms.CharField(
        _('teléfono'), 
        widget=forms.TextInput(
        attrs={'placeholder': 'Teléfono'})
    )

    class Meta:
        model = Usuario
        fields = ('grupo', 'email', 'first_name', 'last_name',
                  'numero_identificacion', 'telefono', 'ocupacion')

    def save(self, commit=True):
        # Save the provided password in hashed format
        usuario = super().save(commit=False)
        # usuario.set_password("")
        # user.password_primera_vez = self.cleaned_data["password1"]

        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = User
        fields = ('grupo', 'email', 'first_name', 'last_name',
                  'numero_identificacion', 'telefono', 'ocupacion', 'is_active', 'is_admin')
