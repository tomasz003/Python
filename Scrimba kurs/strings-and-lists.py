csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names'] #yes mommy

csv=','.join(csv.split(":"))
csv=','.join(csv.split(";"))


friends_list=csv.split(",")
print(friends_list)