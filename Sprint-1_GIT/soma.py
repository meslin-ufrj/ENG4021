def somaf(n1: float, n2: float) -> float:
    '''
    Função que retorna a soma de dois números (inteiros ou reais).

    :param n1: número 1 (int ou float)
    :param n2: número 2 (int ou float)
    :return: soma de n1 e n2 (int ou float)
    
    Exemplo:
    >>> somaf(2, 3)
    5
    >>> somaf(2.5, 3.7)
    6.2
    '''
    return n1 + n2

def main():
    '''
    Função principal para testar a função somaf.
    1. Testa a soma de dois números inteiros.
    2. Testa a soma de dois números reais.
    3. Testa a soma de um número negativo e um positivo.
    4. Testa a soma de zero com um número positivo.
    5. Testa a soma de um número positivo com zero.
    6. Testa a soma de dois números reais iguais.
    7. Imprime uma mensagem de sucesso se todos os testes passarem.
    8. Retorna None.

    :return: None
    
    Exemplo:
    >>> main()
    Todos os testes passaram com sucesso!
    None
    '''
    assert somaf(2, 3) == 5, "Erro: 2 + 3 deveria ser 5"
    assert somaf(2.5, 3.7) == 6.2, "Erro: 2.5 + 3.7 deveria ser 6.2"
    assert somaf(-1.5, 4.5) == 3.0, "Erro: -1.5 + 4.5 deveria ser 3.0"
    assert somaf(0, 5) == 5, "Erro: 0 + 5 deveria ser 5"
    assert somaf(5, 0) == 5, "Erro: 5 + 0 deveria ser 5"
    assert somaf(1.1, 1.1) == 2.2, "Erro: 1.1 + 1.1 deveria ser 2.2"
    print("Todos os testes passaram com sucesso!")
    return
    
if __name__ == "__main__":
    '''
    Executa a função main se o script for executado diretamente.
    1. Chama a função main.
    2. Retorna None.
    '''
    main()
