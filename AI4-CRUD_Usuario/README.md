# Autenticando e autorizando um usuário

### Atividade Individual 4

## Passos iniciais

Para você desenvolver essa atividade, você deve completar a [atividade individual 2](../AI2-MeuProjeto/).

> Você vai desenvolver essa atividade no seu repositório privado. **NÃO** use o repositório do time!

1. Vá para o diretório do seu projeto:

    ```bash
    cd MeuProjeto
    ```

    Se você estiver no lugar correto, você verá uma saída semelhante à seguinte ao usar o comando `ls -l` no terminal:

    ```bash
    $ ls -l
    total 29
    drwxrwxrwx 1 root root     0 nov 12 19:15 img
    drwxrwxrwx 1 root root     0 nov 12 19:15 MeuSite
    -rwxrwxrwx 1 root root 25398 nov 12 19:15 README.md
    -rwxrwxrwx 1 root root     7 nov 12 19:15 requirements.txt
    ```

1. Crie um ambiente virtual, se ele não existir.

    ```bash
    python -m venv venv
    ```

1. Ative o ambiente virtual:

    ```bash
    source venv/bin/activate
    ```

    > Tenha certeza que o ambiente virtual está ativo conferindo o texto `(venv)` no início do *prompt*.

1. Provavelmente você já migrou o seu banco de dados, mas se não tiver migrado ainda, essa é uma boa hora:

    ```bash
    python manage.py migrate
    ```

1. Aproveite para criar um usuário, caso ainda não tenha criado.
Se você está em dúvida, crie um novo usuário e está resolvido.

    ```bash
    python manage.py createsuperuser
    ```

1. Uma boa ideia seria você testar para ver se o seu site está no funcionando. Coloque o site no ar e use o seu navegador para testar:

    ```bash
    cd MeuSite/
    python manage.py runserver 0.0.0.0:8000
    ```

## Criando o login

### Rotas

No arquivo `MeuSite/MeuSite/urls.py`, inclua a seguinte rota na lista de rotas:

```python
urlpatterns = [
    # aqui pode haver mais linhas
    # inclua a linha abaixo no final da lista
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]
```

Ao incluir essa path, o Django vai criar para você as seguintes URLs. Entre colchetes você encontra o nome do endpoint para usar como link:

```
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
```

### Configuração

1. Edite o arquivo `MeuSite/MeuSite/settings.py` e inclua as seguintes linhas para criar as variáveis de configuração do *login* :

```python
LOGOUT_REDIRECT_URL = '/accounts/login/'  # Para onde vai após logout
LOGIN_URL = '/accounts/login/'       # URL de login (padrão)
# ATENÇÃO!!! Troque o valor da variável abaixo para que ela seja uma das rotas
# válidas no seu arquivo MeuSite/curriculo/urls.py
LOGIN_REDIRECT_URL = '/curriculo/spiff/'   # Para onde vai após login
```

### Página de login

Em `curriculo/templates/`, crie o diretório `registration`. 
Dentro desse diretório, crie o arquivo `login.html`.

> Certifique-se que dentro de `templates`, você visualiza os dois diretórios no mesmo nível: `curriculo` e `registration`.

Na sua *home-page*, inclua uma rota para o *login* editando o arquivo `MeuSite/MeuSite/templates/MeuSite/home.html`. A rota pode ser parecida com essa:

```html
<a href="{% url 'login' %}">Login</a>
```

O exemplo a seguir inclui um *link* para o *login* e outro para o *logout* na *home-page*:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
</head>
<body>
    <h1>Home Page do MeuSite</h1>

    <h2>Links para os currículos</h2>
    <ul>
        <li><a href="{% url 'curriculo:curriculo_spiff' %}">Currículo do Spiff</a></li>
        <li><a href="{% url 'curriculo:curriculo_spiff_v2' %}">Currículo responsivo do Spiff</a></li>
    </ul>

    <h2>Área de controle de acesso</h2>
    <ul>
        <li><a href="{% url 'login' %}">Login</a></li>
        <li><form method='POST' action="{% url 'logout' %}">{% csrf_token %}<button type='submit'>Logout</button></form></li>
    </ul>
</body>
</html>
```

### Proteção da página

Se você implementou totalmente A AI2, a sua aplicação `curriculo` deve ter, no mínimo, dois views. Vamos proteger um deles.

Edite o arquivo `MeuSite/curriculo/views.py`. Importe o seguinte decorador:

```python
from django.contrib.auth.decorators import login_required
```

Anote todos (pelo menos um) os `views` que você gostaria de proteger com:

```python
@login_required
```

O seu `view` deve estar parecido com esse (veja o *import* e a anotação na função): 

```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# Essa função abaixo não está protegida
def curriculo_spiff(request):
    return render(request, 'curriculo/curriculo-v1.html')

# A função abaixo está protegida. Veja a anotação @login_required
@login_required
def curriculo_spiff_v2(request):
    return render(request, 'curriculo/curriculo-v2.html')
```

### Testando tudo

1. Acesse a sua *home-page*.

1. Faça login.

1. Visite ambas as páginas: a liberada e a protegida (copie o endereço das páginas - principalmente a protegida).

1. Volte para a sua *home-page*.

1. Faça *logout*.

1. Tente visitar as páginas, principalmente a protegida. Você será encaminhado para a página de *login*, mas conseguirá visitar a página liberada.

1. Faça um vídeo com essa demonstração e coloque no chat do Discord.
