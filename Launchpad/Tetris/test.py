def add_button_to_list(data_list):
    newlist = []
    for item in data_list:
        item["Button"] = item["Button"]
        newlist.append(item["Button"])
    return newlist

# Example usage:
data = [
{"Button": 0, "Note": 24, "Red": 0, "Green": 255, "Instrument": 0, "Key": "C2"},
{"Button": 1, "Note": 25, "Red": 100, "Green": 255, "Instrument": 0, "Key": "C#2"},
{"Button": 2, "Note": 26, "Red": 255, "Green": 200, "Instrument": 0, "Key": "D2"},
{"Button": 3, "Note": 27, "Red": 255, "Green": 150, "Instrument": 0, "Key": "D#2"},
{"Button": 4, "Note": 28, "Red": 255, "Green": 100, "Instrument": 0, "Key": "E2"},
{"Button": 5, "Note": 29, "Red": 255, "Green": 50, "Instrument": 0, "Key": "F2"},
{"Button": 6, "Note": 30, "Red": 50, "Green": 255, "Instrument": 0, "Key": "F#2"},
{"Button": 7, "Note": 32, "Red": 255, "Green": 0, "Instrument": 0, "Key": "G2"},
{"Button": 16, "Note": 33, "Red": 255, "Green": 25, "Instrument": 0, "Key": "G#2"},
{"Button": 17, "Note": 34, "Red": 255, "Green": 255, "Instrument": 0, "Key": "A2"},
{"Button": 18, "Note": 35, "Red": 200, "Green": 255, "Instrument": 0, "Key": "A#2"},
{"Button": 19, "Note": 36, "Red": 150, "Green": 255, "Instrument": 0, "Key": "B2"},
{"Button": 20, "Note": 37, "Red": 0, "Green": 255, "Instrument": 0, "Key": "C3"},
{"Button": 21, "Note": 38, "Red": 100, "Green": 255, "Instrument": 0, "Key": "C#3"},
{"Button": 22, "Note": 39, "Red": 255, "Green": 200, "Instrument": 0, "Key": "D3"},
{"Button": 23, "Note": 40, "Red": 255, "Green": 150, "Instrument": 0, "Key": "D#3"},
{"Button": 32, "Note": 41, "Red": 255, "Green": 100, "Instrument": 0, "Key": "E3"},
{"Button": 33, "Note": 42, "Red": 255, "Green": 50, "Instrument": 0, "Key": "F3"},
{"Button": 34, "Note": 43, "Red": 50, "Green": 255, "Instrument": 0, "Key": "F#3"},
{"Button": 35, "Note": 44, "Red": 255, "Green": 0, "Instrument": 0, "Key": "G3"},
{"Button": 36, "Note": 45, "Red": 255, "Green": 25, "Instrument": 0, "Key": "G#3"},
{"Button": 37, "Note": 46, "Red": 255, "Green": 255, "Instrument": 0, "Key": "A3"},
{"Button": 38, "Note": 47, "Red": 200, "Green": 255, "Instrument": 0, "Key": "A#3"},
{"Button": 39, "Note": 48, "Red": 150, "Green": 255, "Instrument": 0, "Key": "B3"},
{"Button": 48, "Note": 49, "Red": 0, "Green": 255, "Instrument": 0, "Key": "C4"},
{"Button": 49, "Note": 50, "Red": 100, "Green": 255, "Instrument": 0, "Key": "C#4"},
{"Button": 50, "Note": 51, "Red": 255, "Green": 200, "Instrument": 0, "Key": "D4"},
{"Button": 51, "Note": 52, "Red": 255, "Green": 150, "Instrument": 0, "Key": "D#4"},
{"Button": 52, "Note": 53, "Red": 255, "Green": 100, "Instrument": 0, "Key": "E4"},
{"Button": 53, "Note": 54, "Red": 255, "Green": 50, "Instrument": 0, "Key": "F4"},
{"Button": 54, "Note": 55, "Red": 50, "Green": 255, "Instrument": 0, "Key": "F#4"},
{"Button": 55, "Note": 56, "Red": 255, "Green": 0, "Instrument": 0, "Key": "G4"},
{"Button": 64, "Note": 57, "Red": 255, "Green": 25, "Instrument": 0, "Key": "G#4"},
{"Button": 65, "Note": 58, "Red": 255, "Green": 255, "Instrument": 0, "Key": "A4"},
{"Button": 66, "Note": 59, "Red": 200, "Green": 255, "Instrument": 0, "Key": "A#4"},
{"Button": 67, "Note": 60, "Red": 150, "Green": 255, "Instrument": 0, "Key": "B4"},
{"Button": 68, "Note": 61, "Red": 0, "Green": 255, "Instrument": 0, "Key": "C5"},
{"Button": 69, "Note": 62, "Red": 100, "Green": 255, "Instrument": 0, "Key": "C#5"},
{"Button": 70, "Note": 63, "Red": 255, "Green": 200, "Instrument": 0, "Key": "D5"},
{"Button": 71, "Note": 64, "Red": 255, "Green": 150, "Instrument": 0, "Key": "D#5"},
{"Button": 80, "Note": 65, "Red": 255, "Green": 100, "Instrument": 0, "Key": "E5"},
{"Button": 81, "Note": 66, "Red": 255, "Green": 50, "Instrument": 0, "Key": "F5"},
{"Button": 82, "Note": 67, "Red": 50, "Green": 255, "Instrument": 0, "Key": "F#5"},
{"Button": 83, "Note": 68, "Red": 255, "Green": 0, "Instrument": 0, "Key": "G5"},
{"Button": 84, "Note": 69, "Red": 255, "Green": 25, "Instrument": 0, "Key": "G#5"},
{"Button": 85, "Note": 70, "Red": 255, "Green": 255, "Instrument": 0, "Key": "A5"},
{"Button": 86, "Note": 71, "Red": 200, "Green": 255, "Instrument": 0, "Key": "A#5"},
{"Button": 87, "Note": 72, "Red": 150, "Green": 255, "Instrument": 0, "Key": "B5"},
{"Button": 96, "Note": 73, "Red": 0, "Green": 255, "Instrument": 0, "Key": "C6"},
{"Button": 97, "Note": 74, "Red": 100, "Green": 255, "Instrument": 0, "Key": "C#6"},
{"Button": 98, "Note": 75, "Red": 255, "Green": 200, "Instrument": 0, "Key": "D6"},
{"Button": 99, "Note": 76, "Red": 255, "Green": 150, "Instrument": 0, "Key": "D#6"},
{"Button": 100, "Note": 77, "Red": 255, "Green": 100, "Instrument": 0, "Key": "E6"},
{"Button": 101, "Note": 78, "Red": 255, "Green": 50, "Instrument": 0, "Key": "F6"},
{"Button": 102, "Note": 79, "Red": 50, "Green": 255, "Instrument": 0, "Key": "F#6"},
{"Button": 103, "Note": 80, "Red": 255, "Green": 0, "Instrument": 0, "Key": "G6"},
{"Button": 112, "Note": 81, "Red": 255, "Green": 25, "Instrument": 0, "Key": "G#6"},
{"Button": 113, "Note": 82, "Red": 255, "Green": 255, "Instrument": 0, "Key": "A6"},
{"Button": 114, "Note": 83, "Red": 200, "Green": 255, "Instrument": 0, "Key": "A#6"},
{"Button": 115, "Note": 84, "Red": 150, "Green": 255, "Instrument": 0, "Key": "B6"},
{"Button": 116, "Note": 85, "Red": 0, "Green": 255, "Instrument": 0, "Key": "C7"},
{"Button": 117, "Note": 86, "Red": 100, "Green": 255, "Instrument": 0, "Key": "C#7"},
{"Button": 118, "Note": 87, "Red": 255, "Green": 200, "Instrument": 0, "Key": "D7"},
{"Button": 119, "Note": 88, "Red": 255, "Green": 150, "Instrument": 0, "Key": "D#7"}
]


data_with_button = add_button_to_list(data)
print(data_with_button)
