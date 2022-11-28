from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"gAAAAABjhMfxG9Vq1u8XViS3OSNigOv9duOYlH8yOobRY-HGGPwwI8qG54Tj7qSqJKlBBUwSGTMhbUJBOJgWrTsUudeVBLUqxA==")
#print(token)
'...'
f.decrypt(token)
print(f.decrypt(token))
'A really secret message. Not for prying eyes.'