def encrypt_this(text):
    encrypted = []
    for word in text.split():
        ascii_letter = str(ord(word[0]))
    
        if len(word) == 1:
            encrypted_word = ascii_letter

        elif len(word) == 2:
            encrypted_word = ascii_letter + word[1]

        else:
            encrypted_word = ascii_letter + word[-1] + word[2:-1] + word[1]
        
        encrypted.append(encrypted_word)
    return " ".join(encrypted) 
