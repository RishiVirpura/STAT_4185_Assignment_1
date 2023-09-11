encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

front = 1
back = -2
normal = encrypted_message
backwards = encrypted_message
decrypted_message = ""
count = 0


while(count < len(encrypted_message)):
    if count % 2 == 0:
        decrypted_message += encrypted_message[count]
    else:
        decrypted_message += encrypted_message[back]
        back -= 2
        
    count += 1

print(decrypted_message)