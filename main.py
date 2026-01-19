import os
import random
import discord
from discord.ext import commands
from urllib.parse import quote_plus

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# -----------------------------
# Lista
# -----------------------------

lista = [
    # Villanos
    "Darth Vader","Joker","Thanos","Voldemort","Sauron","Magneto","Lex Luthor","Green Goblin",
    "Ultron","Loki","Hannibal Lecter","Scar","Maleficent","Pennywise","Freddy Krueger",
    "Jason Voorhees","Michael Myers","Emperor Palpatine","Bowser","Sephiroth","Ganon",
    "Doctor Octopus","Red Skull","Venom","Kingpin","Bane","Megatron","Freezer","Cell","Light Yagami",

    # Superhéroes
    "Superman","Batman","Spider-Man","Iron Man","Captain America","Thor","Hulk","Wonder Woman",
    "Flash","Aquaman","Black Widow","Hawkeye","Doctor Strange","Black Panther","Ant-Man","Wasp",
    "Wolverine","Deadpool","Cyclops","Jean Grey","Green Lantern","Shazam","Daredevil","Punisher",
    "Scarlet Witch","Vision","Captain Marvel","Star-Lord","Groot","Rocket Raccoon",

    # Personaje Series
    "Walter White","Jesse Pinkman","Saul Goodman","Jon Snow","Daenerys Targaryen","Tyrion Lannister",
    "Rick Grimes","Daryl Dixon","Eleven","Dustin Henderson","Homer Simpson","Bart Simpson",
    "Sheldon Cooper","Leonard Hofstadter","Michael Scott","Dwight Schrute","Tony Soprano",
    "Dexter Morgan","House","Sherlock Holmes","Rick Sanchez","Morty Smith","Geralt de Rivia",
    "Wednesday Addams","Pablo Escobar","Naruto Uzumaki","Goku","Vegeta","Luffy","Zoro",

    # Personajes de videojuegos
    "Michael De Santa","Franklin Clinton","Trevor Philips","Arthur Morgan","John Marston","Joel Miller",
    "Ellie Williams","Kratos","Atreus","Aloy","Ezio Auditore","Altair","Bayek","Eivor","Geralt de Rivia",
    "V (Cyber Punk)","Johnny Silverhand","Nathan Drake","Lara Croft","Doom Slayer","Master Chief","Jin Sakai","Wolf (Sekiro)",
    "Sam Porter Bridges","Solid Snake","Big Boss","Tommy Angelo","Vito Scaletta","Sole Survivor (Fallout 4)",
    "Dragonborn","Commander Shepard","The Inquisitor","Batman","Peter Parker","Miles Morales","Leon S. Kennedy",
    "Claire Redfield","Jesse Faden","Vaas Montenegro","Deacon St. John","Booker DeWitt","Aiden Pearce","Cal Kestis"

    # Videojuegos
    "Minecraft","Fortnite","GTA V","GTA San Andreas","Call of Duty","FIFA","PES","Among Us",
    "League of Legends","Valorant","Counter-Strike","Dota 2","World of Warcraft","Skyrim",
    "The Witcher 3","Dark Souls","Elden Ring","God of War","Red Dead Redemption 2",
    "Assassin’s Creed","Zelda: Breath of the Wild","Mario Kart","Super Smash Bros",
    "Pokémon Red/Blue","Pokémon GO","Resident Evil","Silent Hill","The Last of Us","Halo","Doom",
    "Cyberpunk 2077","Fallout 4","Fallout New Vegas","Mass Effect","Dragon Age",
    "Metal Gear Solid","Final Fantasy VII","Final Fantasy X","Street Fighter",
    "Mortal Kombat","Tekken","Overwatch","Apex Legends","PUBG","Rocket League",
    "Bloodborne","Sekiro","Horizon Zero Dawn","Ghost of Tsushima","Death Stranding",
    "The Legend of Zelda: Ocarina of Time","Diablo III","Diablo IV","Path of Exile",
    "StarCraft","StarCraft II","Warcraft III","Age of Empires","Civilization VI",
    "The Sims","Animal Crossing","Terraria","Stardew Valley","Celeste","Undertale"
]

VIDEOJUEGOS = {
    "Minecraft","Fortnite","GTA V","GTA San Andreas","Call of Duty","FIFA","PES","Among Us",
    "League of Legends","Valorant","Counter-Strike","Dota 2","World of Warcraft","Skyrim",
    "The Witcher 3","Dark Souls","Elden Ring","God of War","Red Dead Redemption 2",
    "Assassin’s Creed","Zelda: Breath of the Wild","Mario Kart","Super Smash Bros",
    "Pokémon Red/Blue","Pokémon GO","Resident Evil","Silent Hill","The Last of Us","Halo","Doom",
    "Cyberpunk 2077","Fallout 4","Fallout New Vegas","Mass Effect","Dragon Age",
    "Metal Gear Solid","Final Fantasy VII","Final Fantasy X","Street Fighter",
    "Mortal Kombat","Tekken","Overwatch","Apex Legends","PUBG","Rocket League",
    "Bloodborne","Sekiro","Horizon Zero Dawn","Ghost of Tsushima","Death Stranding",
    "The Legend of Zelda: Ocarina of Time","Diablo III","Diablo IV","Path of Exile",
    "StarCraft","StarCraft II","Warcraft III","Age of Empires","Civilization VI",
    "The Sims","Animal Crossing","Terraria","Stardew Valley","Celeste","Undertale"
}


def duckduckgo_image_search_url(personaje: str) -> str:
    q = quote_plus(f"{personaje} character")
    return f"https://duckduckgo.com/?q={q}&iax=images&ia=images"

def obtener_pista(personaje):
    if personaje in VIDEOJUEGOS:
        return "Videojuego"
    else:
        return "Personaje"

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def jugar(ctx):
    jugadores = ctx.message.mentions

    if not jugadores:
        await ctx.send("⚠️ Usá: `!jugar @jugador1 @jugador2 ...`")
        return

    # Elegir impostor al azar
    impostor = random.choice(jugadores)

    # Elegir personaje para los NO impostores
    personaje_elegido = random.choice(lista)
    search_url = duckduckgo_image_search_url(personaje_elegido)
    pista = obtener_pista(personaje_elegido)

    enviados = []
    fallidos = []

    for user in jugadores:
        try:
            # Mensaje para el impostor
            if user.id == impostor.id:
                await user.send(
        "🕵️‍♂️ **Eres el IMPOSTOR**\n\n"
        f"🔍 **Pista:** {pista}\n"
        "No sabes el personaje exacto."
    )
            else:
                await user.send(
                    f"🎭 **Se juega con:** {personaje_elegido}\n"
                    f"🖼️ Imágenes: {search_url}"
                )

            enviados.append(user.mention)

        except discord.Forbidden:
            fallidos.append(user.mention)
        except discord.HTTPException:
            fallidos.append(user.mention)

    orden = jugadores.copy()
    random.shuffle(orden)

    orden_texto = "\n".join(
        [f"{i+1}. {user.mention}" for i, user in enumerate(orden)]
    )

    # Mensaje en el canal (sin revelar impostor)
    msg = "✅ **Juego iniciado. Revisen sus mensajes privados.**\n\n"

    if enviados:
        msg += f"📩 Mensajes enviados a: {' '.join(enviados)}\n\n"

    msg += "🕒 **Orden de juego:**\n"
    msg += orden_texto + "\n\n"

    if fallidos:
        msg += f"⛔ No pude enviar DM a: {' '.join(fallidos)} (DMs cerrados o error)"

    await ctx.send(msg)


TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
