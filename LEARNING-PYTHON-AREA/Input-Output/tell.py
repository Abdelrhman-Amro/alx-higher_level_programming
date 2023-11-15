file1 = open("test1.txt", "r")
word1 = file1.read(5)
cursor_position_1 = file1.tell()

word2 = file1.read(6)
cursor_position_2 = file1.tell()

print(f"{word1}|({cursor_position_1}) + {word2}|({cursor_position_2})")

word3 = file1.read()
cursor_position_3 = file1.tell()
print(word3, cursor_position_3)

word4 = file1.read()
cursor_position_4 = file1.tell()
print(word4, cursor_position_4)

file1.close()
