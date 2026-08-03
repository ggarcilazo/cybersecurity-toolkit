import re
from cryptography.fernet import Fernet

def check_password_strength(password: str) -> tuple[int, list[str]]:
    score = 0
    feedback = []
    if len(password) >= 12: score += 1
    else: feedback.append("Debe tener al menos 12 caracteres.")
    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Añade al menos una mayúscula.")
    if re.search(r"\d", password): score += 1
    else: feedback.append("Añade al menos un número.")
    if re.search(r"[@$!%*?&]", password): score += 1
    else: feedback.append("Añade un carácter especial (@$!%*?&).")
    return score, feedback

def encrypt_message(message: str) -> tuple[str, str]:
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode(), key.decode()

