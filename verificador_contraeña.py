import tkinter as tk
from tkinter import ttk

def check_password_strength():
    password = entry_password.get()
    strength = 0

    # Evaluamos la contraseña según diferentes criterios
    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(not c.isalnum() for c in password):
        strength += 1

    # Determinamos el nivel de seguridad basándonos en la puntuación
    if strength < 3:
        result = "Contraseña Débil"
    elif strength < 5:
        result = "Contraseña Moderada"
    else:
        result = "Contraseña Fuerte"

    label_result.config(text=f"Resultado: {result}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Verificador de Contraseñas")
root.geometry("400x200")

# Crear e insertar widgets en la interfaz
label_info = ttk.Label(root, text="Ingresa una contraseña:")
label_info.pack(pady=(20, 10))

entry_password = ttk.Entry(root, show="*")
entry_password.pack(pady=10)

button_check = ttk.Button(root, text="Verificar", command=check_password_strength)
button_check.pack(pady=10)

label_result = ttk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
