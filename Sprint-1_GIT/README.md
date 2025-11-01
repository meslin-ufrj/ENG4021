# Tarefa para aprender a suar o Github e o Codespace

> Tarefa

> Essa tarefa deve ser realizada em equipe de 2, 3, 4 ou 5 alunos.

> Antes de implementar essa tarefa, estude um pouco sobre o uso do Github e do Codespace. Em caso de dúvidas ou problemas, consulte também [GIT](https://github.com/AlexandreMeslin/ENG4021/tree/main/GIT).

Crie uma calculadora de quatro operações: `+`, `-`, `*` e `/`.

## Aluno 1:

- Criar o repositório do time (pode usar o mesmo repositório criado como tarefa da `Sprint 1`).
- Criar um diretório chamado `Calculadora` na raiz do repositório.
Esse diretório será utilizado para criar a calculadora.
- Implementar o módulo `calculadora.py` que irá importar os seguintes módulos que está sendo desevolvido pelos alunos 1, 2, 3, 4 e 5:
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

- Criar um card no Kanban.
- Incluir um *print* do diretório `Calculadora` como evidência de que a tarefa foi concluída.
