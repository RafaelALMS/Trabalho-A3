from django.forms import ModelForm
from gestao.models import Funci, estoque

class AD_Funci(ModelForm):
    class Meta:
        model= Funci
        fields ='__all__'


class AD_Estoque(ModelForm):
    class Meta:
        model= estoque
        fields= ['idSto','proNome','quanEsto','funci']