import argon2

# Define the password you want to hash
password = b"your_password_here"

# Define the salt (should be a byte string)
salt = b"saltsalt"

# Hash the password with the specified salt
hashed_password = argon2.hash_password(password,salt)
hashed_password_different_salt = argon2.hash_password(password)
hashed_password_2 = argon2.hash_password(password,salt)

# Print the hashed password
print("\n\nSAME SALT 1", hashed_password)
print("\n\nSAME SALT 2", hashed_password_2)
print("\n\nDIFFERENT SALT", hashed_password_different_salt)
