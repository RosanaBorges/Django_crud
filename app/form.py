from django.forms import ModelForm
from app.models import Clientes


class ClientesForm(ModelForm):
     class Meta:
        model = Clientes
        fields = ['Id', 'NomeCliente', 'CPF', 'Endereco', 'Celular', 'Email']