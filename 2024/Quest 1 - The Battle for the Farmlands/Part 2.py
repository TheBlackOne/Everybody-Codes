input = """AxBCDDCAxD"""

sum = 0

for enemies in zip(input[0::2], input[1::2]):
    enemies_string = ''.join(enemies)

    num_b = enemies_string.count('B')
    num_c = enemies_string.count('C')
    num_d = enemies_string.count('D')

    sum += num_b
    sum += num_c * 3
    sum += num_d * 5

    if 'x' not in enemies_string:
        sum += 2

print(sum)  