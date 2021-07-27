# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# count = [num**3 for num in range(1, 31)]
# print(count)

# players = ['charles', 'martina', 'michael', 'florance', 'eli']
# # print(players[1:4])
# print(players[:-2])

#Looping thorough a Slice
# players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print("Here are the First three players on my team: ")
# for player in players[:3]:
#     print(player.title())

#Input
x = int(input())
y = int(input())
z = int(input())
N = int(input())
#Solve
arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != N]
#Output
print(arr)