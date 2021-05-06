from django.forms import ModelForm
from .models import Pendiente
#hacer nuestros propios formularios

class PendienteForm(ModelForm):
    class Meta:
        model = Pendiente
        fields=['title','memo','important']
