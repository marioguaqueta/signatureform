from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Button,Div
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab,FormActions,StrictButton
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget


#Formulario para el ingreso de usuario
class LoginForm(forms.Form):

    #Campos definidos para el formulario de ingreso
    username = forms.CharField(label = 'Nombre de usuario')
    password = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)

    #Se define el init apra uilizar el helper de crispy
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('password',css_class='form-control'),
            )
        self.fields['username'].required=True
        self.fields['password'].required=True




class RegisterForm(forms.ModelForm):
    #Se define la clase Meta para elegir el modelo que se va a utilizar
    class Meta:
        model = User 
        fields = ['first_name', 'last_name','username','email','password']
        labels = {'first_name':'NOMBRES',
        'last_name':'APELLIDOS',
        'email':'EMAIL',
        'username':'NOMBRE DE USUARIO',
        'password':'CONTRASEÑA'}

        widgets = {
          'password': forms.PasswordInput()
        }

    #Se define el init apra uilizar el helper de crispy
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('first_name',css_class='form-control'),
                Field('last_name',css_class='form-control'),
                Field('email',css_class='form-control'),
                Field('username', css_class='form-control'),
                Field('password',css_class='form-control'),
                )
                
        )
        self.fields['email'].required=True
        self.fields['first_name'].required=True
        self.fields['last_name'].required=True
        self.fields['username'].required=True
        self.fields['password'].required=True



class RegisterSignatureForm(forms.ModelForm):
    #Se define la clase Meta para elegir el modelo que se va a utilizar
    class Meta:
        model = User 
        fields = ['first_name', 'last_name','email','identificationType', 'identification','phone',
        'city', 'address','birthDate','gender']
        labels = {
        'first_name':'NOMBRES',
        'last_name':'APELLIDOS',
        'email':'EMAIL',
        'identificationType':'TIPO DE IDENTIFICACIÓN',
        'identification':'IDENTIFICACIÓN',
        'phone':'TELÉFONO',
        'city':'CIUDAD',
        'address':'DIRECCIÓN',
        'birthDate':'FECHA DE NACIMIENTO',
        'gender':'GENERO'}


    #Se define el init apra uilizar el helper de crispy
    def __init__(self, *args, **kwargs):
        super(RegisterSignatureForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Field('first_name',css_class='form-control'),
                Field('last_name',css_class='form-control'),
                Field('email',css_class='form-control'),
                Field('identificationType', css_class='form-control'),
                Field('identification',css_class='form-control'),
                Field('phone',css_class='form-control'),
                Field('city',css_class='form-control'),
                Field('address', css_class='form-control'),
                Field('birthDate',css_class='form-control'),
                Field('gender',css_class='form-control')
                )
                
        )
        self.fields['email'].required=True
        self.fields['first_name'].required=True
        self.fields['last_name'].required=True
        self.fields['identificationType'].required=True
        self.fields['identification'].required=True
        self.fields['phone'].required=True
        self.fields['city'].required=True
        self.fields['address'].required=True
        self.fields['birthDate'].required=True
        self.fields['gender'].required=True



class SignatureForm(forms.Form):
    signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#000000','decor-color': '#000000'}))












