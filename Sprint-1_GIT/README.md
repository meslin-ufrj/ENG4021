# Tarefa para aprender a usar o Github e o Codespace

> Nível de dificuldade: Difícil (por membro do time)

Nessa tarefa, o time irá aprender o uso básico do Git, Github e CodeSpace.
Iremos criar uma calculadora de quatro operações: `+`, `-`, `*` e `/` para exemplificar os diversos passos.

> Essa tarefa deve ser realizada em equipe de 2, 3, 4 ou 5 alunos.

Antes de implementar essa tarefa, estude um pouco sobre o uso do Github e do Codespace.

Bibliografia recomendada:
- [Hello World - GitHub Docs](https://docs.github.com/en/get-started/start-your-journey/hello-world)
- [Using Git - GitHub Docs](https://docs.github.com/en/get-started/using-git)

Em caso de dúvidas ou problemas, consulte também [GIT](https://github.com/AlexandreMeslin/ENG4021/tree/main/GIT).

## Todos os alunos

Criar uma conta PRO no GitHub.
Se você já tem uma conta, transforme a sua conta em *PRO*.

### Criando a conta (se você já tem uma conta no GitHub, pode pular essa etapa)

- Acesse o site [github.com](https://github.com/).

- Clique em `Sign up` no canto superior direito.

    ![GitHub Signup](img/github-signup.png)

- Preencha os dados necessários.
Use o seu e-mail da PUC para criar uma conta *PRO*.


### Transformando a sua conta em *PRO*

- Na sua *home-page*, clique na sua foto, no canto superior direito.

- Clique em <svg aria-hidden="true" focusable="false" class="octicon octicon-gear" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M8 0a8.2 8.2 0 0 1 .701.031C9.444.095 9.99.645 10.16 1.29l.288 1.107c.018.066.079.158.212.224.231.114.454.243.668.386.123.082.233.09.299.071l1.103-.303c.644-.176 1.392.021 1.82.63.27.385.506.792.704 1.218.315.675.111 1.422-.364 1.891l-.814.806c-.049.048-.098.147-.088.294.016.257.016.515 0 .772-.01.147.038.246.088.294l.814.806c.475.469.679 1.216.364 1.891a7.977 7.977 0 0 1-.704 1.217c-.428.61-1.176.807-1.82.63l-1.102-.302c-.067-.019-.177-.011-.3.071a5.909 5.909 0 0 1-.668.386c-.133.066-.194.158-.211.224l-.29 1.106c-.168.646-.715 1.196-1.458 1.26a8.006 8.006 0 0 1-1.402 0c-.743-.064-1.289-.614-1.458-1.26l-.289-1.106c-.018-.066-.079-.158-.212-.224a5.738 5.738 0 0 1-.668-.386c-.123-.082-.233-.09-.299-.071l-1.103.303c-.644.176-1.392-.021-1.82-.63a8.12 8.12 0 0 1-.704-1.218c-.315-.675-.111-1.422.363-1.891l.815-.806c.05-.048.098-.147.088-.294a6.214 6.214 0 0 1 0-.772c.01-.147-.038-.246-.088-.294l-.815-.806C.635 6.045.431 5.298.746 4.623a7.92 7.92 0 0 1 .704-1.217c.428-.61 1.176-.807 1.82-.63l1.102.302c.067.019.177.011.3-.071.214-.143.437-.272.668-.386.133-.066.194-.158.211-.224l.29-1.106C6.009.645 6.556.095 7.299.03 7.53.01 7.764 0 8 0Zm-.571 1.525c-.036.003-.108.036-.137.146l-.289 1.105c-.147.561-.549.967-.998 1.189-.173.086-.34.183-.5.29-.417.278-.97.423-1.529.27l-1.103-.303c-.109-.03-.175.016-.195.045-.22.312-.412.644-.573.99-.014.031-.021.11.059.19l.815.806c.411.406.562.957.53 1.456a4.709 4.709 0 0 0 0 .582c.032.499-.119 1.05-.53 1.456l-.815.806c-.081.08-.073.159-.059.19.162.346.353.677.573.989.02.03.085.076.195.046l1.102-.303c.56-.153 1.113-.008 1.53.27.161.107.328.204.501.29.447.222.85.629.997 1.189l.289 1.105c.029.109.101.143.137.146a6.6 6.6 0 0 0 1.142 0c.036-.003.108-.036.137-.146l.289-1.105c.147-.561.549-.967.998-1.189.173-.086.34-.183.5-.29.417-.278.97-.423 1.529-.27l1.103.303c.109.029.175-.016.195-.045.22-.313.411-.644.573-.99.014-.031.021-.11-.059-.19l-.815-.806c-.411-.406-.562-.957-.53-1.456a4.709 4.709 0 0 0 0-.582c-.032-.499.119-1.05.53-1.456l.815-.806c.081-.08.073-.159.059-.19a6.464 6.464 0 0 0-.573-.989c-.02-.03-.085-.076-.195-.046l-1.102.303c-.56.153-1.113.008-1.53-.27a4.44 4.44 0 0 0-.501-.29c-.447-.222-.85-.629-.997-1.189l-.289-1.105c-.029-.11-.101-.143-.137-.146a6.6 6.6 0 0 0-1.142 0ZM11 8a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM9.5 8a1.5 1.5 0 1 0-3.001.001A1.5 1.5 0 0 0 9.5 8Z"></path></svg> Settings.

- Expanda `Billing and licensing`, no menu lateral esquerdo.

- Clique em `Education benefits`.

- Clique no botão `Start an application` e siga as instruções.
Use o documento de inscrição fornecido pelo SAU para comprovar que você é aluno da PUC.



## Aluno 1:

- Criar o repositório do time (pode usar o mesmo repositório criado como tarefa da `Sprint 1`).
- Usando o **Codespace**, criar um diretório chamado `Calculadora` na raiz do repositório do time.
Esse diretório será utilizado para criar a calculadora.
- Implementar o módulo `calculadora.py` que irá importar os seguintes módulos que estão sendo desevolvidos pelos alunos 1, 2, 3, 4 e 5:
    - `soma.py`
    - `subtrai.py`
    - `multiplica.py`
    - `divide.py`
- No módulo calculadora, realizar a leitura de dois números reais e um operando. Baseado nos valores lidos exibir o resultado da operação usando as seguintes funções definidas nos modulos importados:
    - `soma.somaf`
    - `subtrai.subtraif`
    - `multiplica.multiplicaf`
    - `divide.dividef`
- Aceitar os PRs dos componentes do time e fazer o *merge*.

## Aluno 2, 3, 4 e 5

- Criar um `fork` do repositório original.
    - Os alunos 2, 3, 4 e 5 devem pegar com o aluno 1 o endereço do repositório do time.
    - Navegar até o repositório do time.
    - Clicar no botão
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked mr-2"><path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z" fill="currentColor"></path></svg> 
    **Fork** no topo da página.
    - Na página seguinte, basta clicar no botão verde `Create fork`.
    - Verifique se o endereço que aparece no seu navegador agora é um endereço da sua conta do **GitHub**.
    - Antes de começar a trabalhar, siga sempre essas [dicas](#dicas-muito-úteis-ou-não-só-vai-depender-de-você).
- Aluno 2:
    - Criar o modulo `soma.py` dentro do diretório `Calculadora`.
    - Criar a função `somaf` que recebe dois números reais e retorna a sua soma.
- Aluno 3:
    - Criar o modulo `subtrai.py` dentro do diretório `Calculadora`.
    - Criar a função `subtraif` que recebe dois números reais e retorna a sua subtração.
- Aluno 4:
    - Criar o modulo `multiplica.py` dentro do diretório `Calculadora`.
    - Criar a função `multiplicaf` que recebe dois números reais e retorna a sua multiplicação.
- Aluno 5:
    - Criar o modulo `divide.py` dentro do diretório `Calculadora`.
    - Criar a função `dividef` que recebe dois números reais e retorna a sua divisão.
- Implementar testes no módulo. Você pode usar o segmento de código a seguir para realizar o teste. Esse código exemplifica como realizar o teste para a função `somaf`. Modifique-o para a sua função.
    ```python
    def somaf(n1, n2):
        return n1 + n2

    def main():
        assert somaf(2, 3) == 5, "Erro: 2 + 3 deveria ser 5"
        assert somaf(2.5, 3.7) == 6.2, "Erro: 2.5 + 3.7 deveria ser 6.2"
        assert somaf(-1.5, 4.5) == 3.0, "Erro: -1.5 + 4.5 deveria ser 3.0"
        assert somaf(0, 5) == 5, "Erro: 0 + 5 deveria ser 5"
        assert somaf(5, 0) == 5, "Erro: 5 + 0 deveria ser 5"
        assert somaf(1.1, 1.1) == 2.2, "Erro: 1.1 + 1.1 deveria ser 2.2"
        print("Todos os testes passaram com sucesso!")
        return
    if __name__ == "__main__":
        main()
    ```
- Realizar um PR depois de tudo testado e funcionando.
- Depois que o aluno 1 tiver feito o *merge* de todos os PR, atualizar o seu `fork`.

## Todos os alunos

- Testar o funcionamento da calculadora usando o Codespace
- Criar um card no Kanban.
- Incluir um *print* da calculadora funcionando.
- Incluir um *print* do diretório `Calculadora` como evidência de que a tarefa foi concluída.

## Dicas (muito úteis ou não, só vai depender de você)

### Relação do seu *branch* com o original

O seu *branch* pode estar em um desses três estados com relação ao repostório original.
Verifique sempre a mensagem no topo da página.

1. `up to date`: nada a fazer, pode começar a trabalhar!

![up to date](img/github-up-to-date.png)

1. `behind`: se for esse o seu caso, basta clicar em 
<svg aria-hidden="true" focusable="false" class="octicon octicon-sync" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="M1.705 8.005a.75.75 0 0 1 .834.656 5.5 5.5 0 0 0 9.592 2.97l-1.204-1.204a.25.25 0 0 1 .177-.427h3.646a.25.25 0 0 1 .25.25v3.646a.25.25 0 0 1-.427.177l-1.38-1.38A7.002 7.002 0 0 1 1.05 8.84a.75.75 0 0 1 .656-.834ZM8 2.5a5.487 5.487 0 0 0-4.131 1.869l1.204 1.204A.25.25 0 0 1 4.896 6H1.25A.25.25 0 0 1 1 5.75V2.104a.25.25 0 0 1 .427-.177l1.38 1.38A7.002 7.002 0 0 1 14.95 7.16a.75.75 0 0 1-1.49.178A5.5 5.5 0 0 0 8 2.5Z"></path></svg> Sync fork <svg aria-hidden="true" focusable="false" class="octicon octicon-triangle-down" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align: text-bottom;"><path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path></svg>, depois no botão verde `Update branch`.

![branch behind](img/github-behind.png)