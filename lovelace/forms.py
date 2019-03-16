from django import forms
from lovelace.models import Usuario

#class DateInput(forms.DateInput):
#    input_type = 'date'

class UsuarioCriarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome_usuario',
            'dt_nasc_usuario',
            'email_usuario',
            'senha_usuario'
        ]

class UsuariooCriarForm(forms.Form):
#    foto_usuario = forms.ImageField(
#        label='Foto do Perfil: '
#        widget=forms.ImageField(
#            attrs={
#                'required': True,
#                'id' : 'foto_usuario'
#            }
#        )
#    )

    nome_usuario = forms.CharField(
        max_length=120,
        label='Nome:',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'id' : 'nome_usuario'
            }
        )
    )

    dt_nasc_usuario = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(
            attrs={
                'required' : True,
                'id' : 'dt_nasc_usuario'
            }
        )
    )

    email_usuario = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'required' : True,
                'id' : 'email_usuario'
            }
        )
    )

    senha_usuario = forms.CharField(
        max_length=30,
        label='Senha',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'senha_usuario'
            }
        )
    )

    confirma_senha_usuario = forms.CharField(
        max_length=30,
        label='Confirme a senha:',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'confirma_senha_usuario'
            }
        )
    )

class ParceirasCriarForm(forms.Form):
#    foto_parceira = forms.ImageField(
#        label='Foto do Perfil: '
#        widget=forms.ImageField(
#           attrs={
#               'required': True,
#               'id' : 'foto_parceira'
#           }
#       )
#    )

    nome_parceira = forms.CharField(
        max_length=120,
        label='Nome:',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'nome_parceira'
            }
        )
    )

    formacao = forms.CharField(
        max_length=60,
        label='Formação',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'formacao'
            }
        )
    )

    profissao = forms.CharField(
        max_length=60,
        label='Profissão',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'profissao'
            }
        )
    )

    endereco_atend = forms.CharField(
        max_length=100,
        label='Endereço',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'endereco_atend'
            }
        )
    )

    tipo_atend = forms.CharField(
        max_length=30,
        label='Tipo de Atendimento',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'tipo_atend'
            }
        )
    )

    valor = forms.CharField(
        max_length=60,
        label='valor',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'valor'
            }
        )
    )

    telefone_parceiras = forms.CharField(
        max_length=11,
        label='Telefone',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'telefone_parceiras'
            }
        )
    )

    celular_parceiras= forms.CharField(
        max_length=11,
        label='celular',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'id' : 'celular_parceiras'
            }
        )
    )

    email_parceiras= forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'required': True,
                'id' : 'email_parceiras'
            }
        )
    )