import time
message = input("type your mind(something long though): ")
words =keyboard_chars = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
    ' ', '\t', '\n', '\r', '\x0b', '\x0c'
]


empty = ""
for m in message:
  for word in words:
        time.sleep(0.001)
        print(f"{empty}{word}")
        if word == m:
          empty += word
          print(empty)
          break
print("i hope you liked it!")
#Elephant on my chest. . . . Another day passed again.I waste my energy. . . I'm looking for escape within..I thought about turnin' off the lights in here.But I've still got things to do. . .