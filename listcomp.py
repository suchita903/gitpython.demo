squares=[]

for i in range(1,11):
    squares.append(i**2)
print(squares)

squares=[i**2 for i in range(1,6)]
print(squares)

odd_num=[-i for i in range(1,11) if i%2!=0]
print(odd_num)


