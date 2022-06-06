# Enter a piece of text. Ask for a starting and ending number and just display the section between.

text = input("Enter a String: ")

start = int(input("Enter the starting point: "))
end = int(input("Enter the end point:"))

print(text[start:end])