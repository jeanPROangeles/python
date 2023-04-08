import hashlib
import secrets

def convertir_password(password):
    # Comprobar que el password tiene entre 6 y 12 caracteres
    if len(password) < 6 or len(password) > 12:
        raise ValueError("El password debe tener entre 6 y 12 caracteres")

    # Generar una sal aleatoria de 16 bytes
    salt = secrets.token_bytes(16)

    # Convertir el password y la sal a bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt

    # Concatenar la sal y el password
    concatenated_bytes = salt_bytes + password_bytes

    # Generar el hash SHA-256 de la concatenación
    hash_object = hashlib.sha256(concatenated_bytes)
    hash_hex = hash_object.hexdigest()

    # Devolver la sal y el hash concatenados
    return salt.hex() + hash_hex

#print(convertir_password('123456'))