full_name = input("Enter your full name: ")

cleaned_name = full_name.strip()
character = input("Enter a character to search for: ")

print("Original Input:", full_name)
print("Cleaned Name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title Case:", cleaned_name.title())
print("Length:", len(cleaned_name))

if cleaned_name:
    print("First Character:", cleaned_name[0])
    print("Last Character:", cleaned_name[-1])
else:
    print("First Character: The name is empty.")
    print("Last Character: The name is empty.")

print("Contains the Character:", character in cleaned_name)
