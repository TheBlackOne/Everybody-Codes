input = """xBxAAABCDxCC"""

sum = 0

for enemies in zip(input[0::3], input[1::3], input[2::3]):
    enemies_string = ''.join(enemies)

    num_b = enemies_string.count('B')
    num_c = enemies_string.count('C')
    num_d = enemies_string.count('D')

    sum += num_b
    sum += num_c * 3
    sum += num_d * 5

    if enemies_string.count('x') == 1:
        sum += 2
    elif enemies_string.count('x') == 0:
        sum += 6

print(sum)  