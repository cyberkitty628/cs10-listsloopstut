songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[2])
print(songs[1:3])
songs[2] = "Savage"
print(songs)

songs.append("Cherish the Day")
songs.extend(["Make It Right"])
songs.insert(5, "Juicy")
songs.remove("Do It")

animals = ["cat", "quokka", "bunny"]
animals.append("snow leopard")
print(animals[2])
del animals[0]

for animal in animals:
    print(animal)