from cryptography.fernet import Fernet
from vip.keys import SENHA_SECRETA

def encrypt_documento(documento):
    cipher = Fernet(SENHA_SECRETA)
    encrypted_documento = str(cipher.encrypt(documento.encode()).decode())
    return encrypted_documento

def decrypt_documento(encrypted_documento):
    try:
        cipher = Fernet(SENHA_SECRETA)
        decrypted_documento = cipher.decrypt(encrypted_documento)

        # Verifica se o resultado é uma string antes de chamar decode()
        if isinstance(decrypted_documento, bytes):
            decrypted_documento = decrypted_documento.decode()
        
        return decrypted_documento
    except Exception as e:
        # Trate as exceções de descriptografia de maneira adequada
        print(f"Erro durante a descriptografia: {e}")
        return None
