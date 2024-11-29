# gran_de_tres.py

def gran_de_tres(num1, num2, num3):
    """Retorna el major dels tres números proporcionats."""
    return max(num1, num2, num3)

# Proves de la funció
if __name__ == "__main__":
    # Exemples de prova
    print(f"El major entre 5, 10 i 3 és: {gran_de_tres(5, 10, 3)}")
    print(f"El major entre -1, -5 i 0 és: {gran_de_tres(-1, -5, 0)}")
    print(f"El major entre 2.5, 3.5 i 3.0 és: {gran_de_tres(2.5, 3.5, 3.0)}")
    print(f"El major entre 100, 99 i 150 és: {gran_de_tres(100, 99, 150)}")
    print(f"El major entre 0, 0 i 0 és: {gran_de_tres(0, 0, 0)}")