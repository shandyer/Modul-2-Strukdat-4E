Hewan = ["Sapi", "Kelinci", "Kambing", "Unta", "Domba"]
DeleteHewan = []

print("Silakan hapus hewan yang dipilih:")
animal = input()

current_animal = animal.split(",")
for i in range(len(current_animal)):
    Hewan.remove(current_animal[i])
    DeleteHewan.append(current_animal[i])

print(Hewan)
