# -------------
# Copyright (c) 2022, bot-shop.me
# All rights reserved.
# -------------

from utils import *

bot = commands.Bot(command_prefix=Config.prefix, intents=discord.Intents.all(), debug_guilds=Config.guild)


@bot.event
async def on_ready():
    # create_db()
    if len(bot.guilds) > 1 and bot.debug_guilds:
        debug(
            "Achtung! Wenn du den Bot auf mehr als einem Server benutzt können Fehler auftreten, da der Bot nicht für mehrere Server konzepiert ist!",
            error=True)
    debug(f'Logged in as {bot.user}', force=True)
    debug(f'Support: help@bot-shop.me', force=True)
    debug(f'------', force=True)
    debug(f'ID: {bot.user.id}')
    debug(f'Ping: {bot.latency * 1000:.0f}ms', error=False if bot.latency * 1000 < 300 else True)
    debug(
        f'Guilds: {len(bot.guilds)}' if not bot.debug_guilds else f'Guilds: {len(bot.guilds)} (Debug: {len(bot.debug_guilds) if bot.debug_guilds else 0})')
    debug(f'Users: {len(bot.users)}')
    debug(f'------')


def setup():
    token = input(
        "Was ist ein Discord Token und wie erhalte ich ihn: https://de.technobezz.com/how-to-get-a-discord-bot-token/\nGebe den Token ein: ")
    change_config("token", token)
    guild = input(
        "Wie erhalte ich die ID eines Servers: https://support.discord.com/hc/de/articles/206346498-Wie-finde-ich-meine-Server-ID-\nGebe die ID des Servers ein, auf dem der Bot laufen soll: ")
    change_config("guild", guild)
    color = input(
        "\nWie erhalte ich eine Farbe: https://www.color-hex.com/\nGebe die Farbe ein, die der Bot verwenden soll: ")
    change_config("color", color)
    prefix = input("Gebe den Prefix ein, den der Bot verwenden soll: ")
    change_config("prefix", prefix)
    owner = input(
        "Wie erhalte ich die ID eines Benutzers: https://support.discord.com/hc/de/articles/206346498-Wie-finde-ich-meine-Server-ID-\n Gebe die ID des Besitzers ein: ")
    change_config("owner", owner)
    print("Setup eingerichtet! Starte das skript neu um änderungen anzuwenden!")


def settings():
    selection = input(f"""\nWas möchtest du einstellen?
--------------------------------
setup = Allgemeine Einrichtung
guild = Bot Server wechseln
color = Standard Farbe ändern
token = Token ändern
prefix = Prefix ändern
owner = Besitzer wechseln
debug = Debug Modus wechseln
cancel = Einstellungen beenden
--------------------------------
Deine Auswahl: """)
    if selection.lower() == "setup":
        setup()

    elif selection.lower() == "guild":
        guild = input(
            "Wie erhalte ich die ID eines Servers: https://support.discord.com/hc/de/articles/206346498-Wie-finde-ich-meine-Server-ID-\nGebe die ID des Servers ein, auf dem der Bot laufen soll: ")
        change_config("guild", guild)
        print("Server geändert! Starte das skript neu um änderungen anzuwenden!")
    elif selection.lower() == "color":
        color = input(
            "Gebe die Farbe ein, die der Bot verwenden soll: \nWie erhalte ich eine Farbe: https://www.color-hex.com/")
        change_config("color", color)
        print("Farbe geändert! Starte das skript neu um änderungen anzuwenden!")
    elif selection.lower() == "token":
        token = input(
            "Was ist ein Discord Token und wie erhalte ich ihn: https://de.technobezz.com/how-to-get-a-discord-bot-token/\nGebe den Token ein: ")
        change_config("token", token)
        print("Token geändert! Starte das skript neu um änderungen anzuwenden!")
    elif selection.lower() == "prefix":
        prefix = input("Gebe den Prefix ein, den der Bot verwenden soll: ")
        change_config("prefix", prefix)
        print("Prefix geändert! Starte das skript neu um änderungen anzuwenden!")
    elif selection.lower() == "owner":
        owner = input(
            "Wie erhalte ich die ID eines Benutzers: https://support.discord.com/hc/de/articles/206346498-Wie-finde-ich-meine-Server-ID-\n Gebe die ID des Besitzers ein: ")
        change_config("owner", owner)
        print("Besitzer geändert! Starte das skript neu um änderungen anzuwenden!")
    elif selection.lower() == "debug":
        setting = input("Gebe an ob der Debug Modus aktiviert sein soll (y/n): ")
        if setting.lower() == "y":
            change_config("debug", True)
        else:
            change_config("debug", False)
        print("Debug Modus geändert! Starte das skript neu um änderungen anzuwenden!")
    elif selection.lower() == "cancel":
        print("Einstellungen beendet!")
        return
    else:
        print("Ungültige Eingabe!")
        settings()


def run():
    if Config.debug:
        debug('\u001b[1m⚙ - Schreibe "settings" um in die Einstellungen zu gelangen.\n'
              '🟢 - Drücke Enter um den Bot zu starten.\u001b[0m', force=True, dt=False)
        debug('Debug autoskip\n')
    else:
        enter = input('\u001b[1m⚙ - Schreibe "settings" um in die Einstellungen zu gelangen.\n'
                      '🟢 - Drücke Enter um den Bot zu starten.\u001b[0m\n')
        if enter.lower() == "settings":
            settings()
            return
    try:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
                debug(f'Cog Loaded: {filename}')
        bot.run(Config.token)
    except Exception as e:
        debug(e)
        if isinstance(e, AttributeError):
            setup()
        elif isinstance(e, discord.errors.LoginFailure):
            debug("Der Token den du in dem setup angegeben hast ist ungültig!", error=True)
            settings()


async def stop():
    await bot.close()


if __name__ == '__main__':
    run()
