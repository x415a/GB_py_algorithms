# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв

c1, c2 = input('Введите 2 буквы через пробел: ').split()
shift = ord('a') - 1

print(f"№{c1} = {ord(c1) - shift}", f"№{c2} = {ord(c2) - shift}", sep='\n')
print(f"Расстояние между буквами: {abs(ord(c1) - ord(c2))}")