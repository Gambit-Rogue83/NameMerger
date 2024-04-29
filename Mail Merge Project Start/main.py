
with open("./Input/Names/invited_names.txt") as names:
    guests = names.read()
    guest_list = guests.split()


with open("./Input/Letters/starting_letter.txt") as invite:
    letter = invite.read()
    for name in guest_list:
        new_letter = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as mail_ready:
            mail_ready.write(new_letter)

