class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Remove possíveis caracteres de sinal negativo
        if num1[0] == '-':
            num1 = num1[1:]
        if num2[0] == '-':
            num2 = num2[1:]

        # Converte as strings em listas de dígitos invertidos
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Inicializa o resultado e a lista de carry
        result = [0] * (len(num1) + len(num2))
        carry = 0

        # Realiza a multiplicação usando o algoritmo de Karatsuba
        for i in range(len(num1)):
            carry = 0
            for j in range(len(num2)):
                temp = int(num1[i]) * int(num2[j]) + carry + result[i+j]
                carry = temp // 10
                result[i+j] = temp % 10

            result[i + len(num2)] = carry

        # Remove os zeros à esquerda do resultado
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        # Converte o resultado de volta para uma string invertida
        result = ''.join(str(digit) for digit in result[::-1])

        # Adiciona o sinal negativo, se necessário
        if (num1[0] == '-' and num2[0] != '-') or (num1[0] != '-' and num2[0] == '-'):
            result = '-' + result

        return result
