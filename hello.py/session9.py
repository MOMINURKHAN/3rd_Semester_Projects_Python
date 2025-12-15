#task 1 
print("Notes App Starting")
#task 2
notes = []

#task 3
user_note = input("Add a note : ")
notes.append(user_note)

#task 4
from pathlib import Path
path = Path('notes.txt')
contents = "\n".join(notes)
path.write_text(contents)

#task 5
path = Path('notes.txt')
if path.exists():
    contents = path.read_text()
    notes = contents.splitlines()
else:
    notes = []

#task 5
import json
data = {'notes':notes}
json_text = json.dumps(data)
Path("notes.json").write_text(json_text)

#task 6
try:
    json_text = Path("notes.json").read_text()
    data = json.loads(json_text)
    notes = data["notes"]
except(FileNotFoundError):
    notes = []

#task 7
while True:
    print("\n=== Notes Menu ===")
    print("1 = View notes")
    print("2 = Add note")
    print("3 = Save notes")
    print("4 = Exit")

    
    choice = input("Choose: ")

    
    
    