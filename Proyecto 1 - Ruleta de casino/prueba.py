import random
import time

# Se definen los colores de la ruleta segun su numero
ruleta = {
    0: "verde",
    1: "rojo", 2: "negro", 3: "rojo", 4: "negro", 5: "rojo", 6: "negro", 7: "rojo", 8: "negro",
    9: "rojo", 10: "negro", 11: "negro", 12: "rojo", 13: "negro", 14: "rojo", 15: "negro", 16: "rojo",
    17: "negro", 18: "rojo", 19: "rojo", 20: "negro", 21: "rojo", 22: "negro", 23: "rojo", 24: "negro",
    25: "rojo", 26: "negro", 27: "rojo", 28: "negro", 29: "negro", 30: "rojo", 31: "negro", 32: "rojo",
    33: "negro", 34: "rojo", 35: "negro", 36: "rojo"
}

contador_victorias = 0
contador_derrotas = 0
dinero_ganado = 0

# Se define el mecanismo aleatorio para la ruleta usando la funcion random.randit y retornamos las variables
# numero y color.
def girar_ruleta():
    numero = random.randint(0, 36)
    color = ruleta[numero]
    return numero, color

def historial():
    if contador_derrotas > 0:
        promedio_de_victorias = (contador_victorias / contador_derrotas) * 100
    else:
        promedio_de_victorias = 0
    print(f"Victorias: {contador_victorias}")
    print(f"Derrotas: {contador_derrotas}")
    print(f"Promedio de victorias: {promedio_de_victorias:.2f}%")
    print(f"Dinero ganado: {dinero_ganado}")

def jugar():
    global contador_victorias, contador_derrotas, dinero_ganado
    dinero = 100  # Dinero inicial

    print("🎰 Bienvenido a la ruleta de casino 🎰")
    print("💵 Tienes 100 monedas para apostar. 💵")

    while dinero > 0:
        print("\n🎲 Opciones de apuesta:")
        print("1️⃣ Número específico (Ganancia: 36:1) Numero (0) (Ganancia: 100:1) ")
        print("2️⃣ Rojo o Negro (Ganancia: 1:1)")
        print("3️⃣ Par o Impar (Ganancia: 1:1)")
        print("4️⃣ Primera Seccion (1-12) (Ganancia: 5:1)")
        print("5️⃣ Segunda Seccion (13-24) (Ganancia: 5:1)")
        print("6️⃣ Tercera Seccion (25-36) (Ganancia: 5:1)")
        print("7️⃣ Historial y promedio")
        print(f"\n💰 Tienes {dinero} monedas. 💰")

        try:
            opcion = int(input("Elige una opción (1-7) o 0 para salir: "))
            if opcion == 0:
                print("👋 ¡Gracias por jugar!")
                break
            elif opcion == 7:
                historial()
                continue

            apuesta = None
            if opcion == 1:
                apuesta = int(input("🎲 Elige un número del 0 al 36: "))
                if apuesta < 0 or apuesta > 36:
                    print("⚠️ Número fuera de rango.")
                    continue
            elif opcion == 2:
                apuesta = input("🔴⚫ Elige 'rojo' o 'negro': ").strip().lower()
                if apuesta not in ["rojo", "negro"]:
                    print("⚠️ Opción inválida.")
                    continue
            elif opcion == 3:
                apuesta = input("📊 Elige 'par' o 'impar': ").strip().lower()
                if apuesta not in ["par", "impar"]:
                    print("⚠️ Opción inválida.")
                    continue
            elif opcion == 4:
                apuesta = "primera_seccion"
            elif opcion == 5:
                apuesta = "segunda_seccion"
            elif opcion == 6:
                apuesta = "tercera_seccion"
            else:
                print("⚠️ Opción no válida.")
                continue

            monto = int(input(f"💸 ¿Cuánto deseas apostar? (Máx: {dinero}): "))
            if monto > dinero or monto <= 0:
                print("⚠️ Apuesta inválida.")
                continue
            
            print("🎡 Girando la ruleta", end="", flush=True)
            for _ in range(4):
                time.sleep(1)
                print(".", end="", flush=True)
            
            numero, color = girar_ruleta()
            print(f"🎉 La bola cayó en {numero} ({color}) 🎉", flush=True)
            time.sleep(1)

            # Verificar la apuesta y calcular ganancias
            if opcion == 1 and apuesta == numero:
                if numero == 0:
                    ganancias = monto * 100
                else:
                    ganancias = monto * 36
                dinero += ganancias
                contador_victorias += 1
                dinero_ganado += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas! 💰", flush=True)
                time.sleep(1)
            elif opcion == 2 and apuesta == color:
                ganancias = monto
                dinero += ganancias
                contador_victorias += 1
                dinero_ganado += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas! 💰", flush=True)
                time.sleep(1)
            elif opcion == 3 and ((apuesta == "par" and numero % 2 == 0 and numero != 0) or 
                                   (apuesta == "impar" and numero % 2 == 1)):
                ganancias = monto
                dinero += ganancias
                contador_victorias += 1
                dinero_ganado += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas! 💰", flush=True)
                time.sleep(1)
            elif opcion == 4 and 1 <= numero <= 12:
                ganancias = monto * 5
                dinero += ganancias
                contador_victorias += 1
                dinero_ganado += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas en la Primera Docena! 💰", flush=True)
                time.sleep(1)
            elif opcion == 5 and 13 <= numero <= 24:
                ganancias = monto * 5
                dinero += ganancias
                contador_victorias += 1
                dinero_ganado += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas en la Segunda Docena! 💰", flush=True)
                time.sleep(1)
            elif opcion == 6 and 25 <= numero <= 36:
                ganancias = monto * 5
                dinero += ganancias
                contador_victorias += 1
                dinero_ganado += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas en la Tercera Docena! 💰", flush=True)
                time.sleep(1)
            else:
                dinero -= monto
                contador_derrotas += 1
                print("❌ Perdiste tu apuesta.", flush=True)
                time.sleep(1)

            if dinero == 0:
                print("💸 Te has quedado sin dinero. ¡Juego terminado! 💸", flush=True)
                time.sleep(1)
                break

        except ValueError:
            print("⚠️ Entrada inválida. Intenta de nuevo.") 

jugar()