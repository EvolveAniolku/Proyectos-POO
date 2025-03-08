import random

# Definir la ruleta con colores
ruleta = {
    0: "verde",
    1: "rojo", 2: "negro", 3: "rojo", 4: "negro", 5: "rojo", 6: "negro", 7: "rojo", 8: "negro",
    9: "rojo", 10: "negro", 11: "negro", 12: "rojo", 13: "negro", 14: "rojo", 15: "negro", 16: "rojo",
    17: "negro", 18: "rojo", 19: "rojo", 20: "negro", 21: "rojo", 22: "negro", 23: "rojo", 24: "negro",
    25: "rojo", 26: "negro", 27: "rojo", 28: "negro", 29: "negro", 30: "rojo", 31: "negro", 32: "rojo",
    33: "negro", 34: "rojo", 35: "negro", 36: "rojo"
}

def girar_ruleta():
    numero = random.randint(0, 36)
    color = ruleta[numero]
    return numero, color

def jugar():
    dinero = 100  # Dinero inicial

    print("🎰 Bienvenido a la ruleta de casino 🎰")
    print("💵 Tienes 100 monedas para apostar. 💵")

    while dinero > 0:
        print("\n🎲 Opciones de apuesta:")
        print("1️⃣ Número específico (paga 35:1)")
        print("2️⃣ Rojo o Negro (paga 1:1)")
        print("3️⃣ Par o Impar (paga 1:1)")
        print("4️⃣ Primera Docena (1-12) (paga 2:1)")
        print("5️⃣ Segunda Docena (13-24) (paga 2:1)")
        print(f"\n💰 Tienes {dinero} monedas. 💰")

        try:
            opcion = int(input("Elige una opción (1-5) o 0 para salir: "))
            if opcion == 0:
                print("👋 ¡Gracias por jugar!")
                break

            apuesta = None
            if opcion == 1:
                apuesta = int(input("🎲 Elige un número del 0 al 36: "))
                if apuesta < 0 or apuesta > 36:
                    print("⚠️ Número fuera de rango.")
                    continue
            elif opcion == 2:
                apuesta = input("🔴⚫ Elige 'rojo' o 'negro': ").lower()
                if apuesta not in ["rojo", "negro"]:
                    print("⚠️ Opción inválida.")
                    continue
            elif opcion == 3:
                apuesta = input("📊 Elige 'par' o 'impar': ").lower()
                if apuesta not in ["par", "impar"]:
                    print("⚠️ Opción inválida.")
                    continue
            elif opcion == 4:
                apuesta = "primera_docena"
            elif opcion == 5:
                apuesta = "segunda_docena"
            else:
                print("⚠️ Opción no válida.")
                continue

            monto = int(input(f"💸 ¿Cuánto deseas apostar? (Máx: {dinero}): "))
            if monto > dinero or monto <= 0:
                print("⚠️ Apuesta inválida.")
                continue
            
            print("🎡 Girando la ruleta...")
            numero, color = girar_ruleta()
            print(f"🎉 La bola cayó en {numero} ({color}) 🎉")

            # Verificar la apuesta y calcular ganancias
            if opcion == 1 and apuesta == numero:
                ganancias = monto * 35
                dinero += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas! 💰")
            elif opcion == 2 and apuesta == color:
                ganancias = monto
                dinero += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas! 💰")
            elif opcion == 3 and ((apuesta == "par" and numero % 2 == 0 and numero != 0) or 
                                   (apuesta == "impar" and numero % 2 == 1)):
                ganancias = monto
                dinero += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas! 💰")
            elif opcion == 4 and 1 <= numero <= 12:
                ganancias = monto * 2
                dinero += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas en la Primera Docena! 💰")
            elif opcion == 5 and 13 <= numero <= 24:
                ganancias = monto * 2
                dinero += ganancias
                print(f"💰 ¡Ganaste {ganancias} monedas en la Segunda Docena! 💰")
            else:
                dinero -= monto
                print("❌ Perdiste tu apuesta.")

            if dinero == 0:
                print("💸 Te has quedado sin dinero. ¡Juego terminado! 💸")
                break

        except ValueError:
            print("⚠️ Entrada inválida. Intenta de nuevo.")

# Ejecutar el juego
jugar()
