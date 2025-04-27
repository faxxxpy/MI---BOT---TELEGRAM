import asyncio
from telethon import TelegramClient

# Configura tu sesión
api_id = 27929362     # <--- tu API ID
api_hash = 'c5aacd221f8586d6a5b51d6846ef4e43'  # <--- tu API HASH
session_name = 'mi_sesion'  # Nombre de tu archivo de sesión (.session)

# Configura el bot al que quieres escribir
bot_username = '@MONKEYDATA_BOT'  # <-- cámbialo por el bot al que le escribes

# Rango de DNIs
dni_inicio = 1284  # Desde 00000001
dni_fin = 99999999  # Hasta 99999999 o el número que quieras

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    print("✅ Sesión iniciada correctamente.")

    for dni in range(dni_inicio, dni_fin + 1):
        dni_str = str(dni).zfill(8)  # Rellenar con ceros a la izquierda
        mensaje = f"/dnip {dni_str}"
        try:
            await client.send_message(bot_username, mensaje)
            print(f"📨 Enviado: {mensaje}")
        except Exception as e:
            print(f"❌ Error al enviar {mensaje}: {e}")
        
        await asyncio.sleep(25)  # Espera 20 segundos antes de enviar el siguiente

    print("🚀 ¡Se terminó de enviar todos los DNIs!")

if __name__ == "__main__":
    asyncio.run(main())
