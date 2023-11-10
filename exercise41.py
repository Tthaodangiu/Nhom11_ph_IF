notes = {"C4": 261.63, "D4": 293.66, "E4": 329.63, "F4": 349.23, "G4": 392.00, "A4": 440.00, "B4": 493.88}
keys = list(notes.keys())
print(keys)
start_freq = 0
inp = input("Enter Note: ")
p1 = inp[0]
p2 = int(inp[1])
if p1 + "4" in notes:
    note_freq = notes[p1 + "4"] / (2 ** (4 - p2))
    print(note_freq)
else:
    print("Invalid note.")
    