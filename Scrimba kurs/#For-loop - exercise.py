names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']


#names = names + names1
#for index in range(2):
#    names.append(input('Enter a new name: '))

names[2]+=" Jackson"
names1[1]+=" Blueberry"

for i in names:
    print(f"Dear {i.title()}, you are invited to the party on Saturday!")


for i in names1:
    print(f"Dear {i.title()}, you are invited to the party on Saturday!")

