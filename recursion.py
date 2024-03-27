def list_recursion_print(my_list, index=None):
    """ 
        PT-BR:
            Função que recebe uma lista e adicionalmente um parametro index (indice) que se não for passado será tratado como nulo,
            e imprime a lista do fim para o começo utilizando recursão. 
            Retornos: 
            - Vazio.
        EN: 
            Function that receives a list e and an additional parameter index, that it's default value is null. 
            The function will use recursion to print the list from the last element to the first.
            Returns:
            - None.
    """
    if my_list is None:
        return None
    if type(my_list) is not list or len(my_list) < 1:
        return None
    if index is None:
        index = len(my_list)
    if index is None or index == 0:
        return None
    if my_list[index-1]:
        print(my_list[index-1])
    list_recursion_print(my_list, index-1)

def fibonacci_recursion(n): 
    """ 
        PT-BR:
            Função de calculo da sequencia de Fibonacci que recebe um número e retorna uma lista com a 
            sequencia dos numeros de Fibonacci, utilizando recusão (Função que chama a si própria).
            Retornos:
            - Lista vazia.
            - Lista com números da sequencia de Fibonacci.
            Exemplos:
                Fibonacci de 5: [1, 1, 2, 3]
                Fibonacci de 6: [1, 1, 2, 3, 5]
                Fibonacci de 7: [1, 1, 2, 3, 5, 8]
        EN: 
            Function that receives a number and returns a list with Fibonacci sequence of a 
            provided number, using recursion (Function that calls itself) .
            Returns:
            - Empty List.
            - List with the Fibonacci sequence numbers. 
            Examples:
                Fibonacci of 5: [1, 1, 2, 3]
                Fibonacci of 6: [1, 1, 2, 3, 5]
                Fibonacci of 7: [1, 1, 2, 3, 5, 8]
    """
    if n is None:
        return []
    elif type(n) is not int:
        return []
    elif n < 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        sequence = [1]
        return sequence
    else:         
        sequence = fibonacci_recursion(n-1)
        if len(sequence) > 1:
            sequence.append(sequence[-1] + sequence[-2])
        else:
            sequence.append(sequence[-1])
        return sequence

print('Simple Recursion Function Example')
my_list = ['Banana', 'Apple', 'Orange', 'Blueberry', 'Strawberry', 'Melon', 'Pineapple', 'Pear', 'Lemon', 'Grape']
my_list.sort()
print(my_list)
list_recursion_print(my_list)
print('----------')
my_list.sort(reverse=True)
print(my_list)
list_recursion_print(my_list)
print('----------')
print('Fibonnaci Sequence Using Recursion Example')
n=12
my_list = fibonacci_recursion(n)
print(my_list)
if len(my_list) > 1:
    print(f"Fibonnaci de {n}: {my_list[-1] + my_list[-2]}")
else:
    print(1)