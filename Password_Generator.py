import random 
#Length of password from user
password_length = int(input("How many characters do you want in your password? "))

digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0'] 
char_lc = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'] 
char_uc = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'] 
symbols = ['>', '#', '~', '<', '%', ':', '.', '/', '@', '|', '*', '(', '=', '?', ')', '$'] 

# Ensure at least one of each type of character is included
char_combine = random.choice(digits) + random.choice(char_lc) + random.choice(char_uc) + random.choice(symbols)

# Fill the rest of the password length
for i in range(password_length - 4): 
    char_combine = char_combine + random.choice(digits + char_lc + char_uc + symbols)

# Shuffle the generated password
char_list = list(char_combine)
random.shuffle(char_list)
password = "".join(char_list)

# Print out password 
print("Your strong random password:", password)
