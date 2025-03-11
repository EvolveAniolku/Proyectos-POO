import time

numero = 42
print("Generando", end="", flush=True)

for _ in range(3):
    time.sleep(1)
    print(".", end="", flush=True)

print(f"\nEl número generado es: {numero}", flush=True)
time.sleep(1)