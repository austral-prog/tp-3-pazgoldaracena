def check_vowels():
    # Código a implementar utilizando input.
    name = input(" ")
    print(f"Contiene a: {'a' in name.lower()}")
    print(f"Contiene e: {'e' in name.lower()}")
    print(f"Contiene i: {'i' in name.lower()}")
    print(f"Contiene o: {'o' in name.lower()}")
    print(f"Contiene u: {'u' in name.lower()}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
