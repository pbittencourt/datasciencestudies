# QUAL É O MAIOR NÚMERO?
# VERSÃO COM LOOPS (033 extended)

n = int(input('Quantos números queres? _ '))
num = []
i = 0
while i < n:
    num.append(int(input('Digita o {}º número: _ ' .format(i+1))))
    i += 1
num.sort()
print('O maior valor digitado foi {} e, o menor, {}.' .format(num[i-1], num[0]))
