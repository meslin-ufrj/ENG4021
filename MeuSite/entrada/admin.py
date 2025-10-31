from django.contrib import admin

# Register your models here.

# Register your models here.
# Lembre-se que `Pessoa` é o nome da classe que você criou
# Você deve substituir `Pessoa` pela classe criada referente ao seu projeto
from entrada.models import Pessoa
admin.site.register(Pessoa)
