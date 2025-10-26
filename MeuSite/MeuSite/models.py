from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Entre o nome')
    idade = models.IntegerField(help_text='Entre a idade')
    salario = models.DecimalField(help_text='Entre o salário', decimal_places=2, max_digits=8)
    email = models.EmailField(help_text='Informe o email', max_length=254)
    dtNasc = models.DateField(help_text='Nascimento no formato DD/MM/AAAA', verbose_name='Data de nascimento')
    
    def __str__(self):
        '''
        Como cada uma das entradas do banco de dados vai aparecer 
        na interface administrativa.
        Veja mais em `magic method`, `special method`, `dunder method`
        dunder == double underscore ou double underline
        @seealso: https://docs.python.org/3/reference/datamodel.html#specialnames
        '''
        return "Pessoa: " + self.nome 
