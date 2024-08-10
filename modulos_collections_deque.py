from collections import deque
'''Deque são listas de alta performance'''

# Criando deque
deq = deque('geek')
print(deq) # Resposta: deque(['g', 'e', 'e', 'k'])

# Adicionando elementos deque(final)
deq.append('y')
print(deq) # deque(['g', 'e', 'e', 'k', 'y'])

# adicionando elementos deque(inicio)
deq.appendleft('oi')
print(deq) # deque(['oi', 'g', 'e', 'e', 'k', 'y'])

# Removendo elementos (ultimo)
deq.pop()
print(deq) # deque(['oi', 'g', 'e', 'e', 'k'])

# Removendo elementos (primeiro)
deq.popleft()
print(deq)
