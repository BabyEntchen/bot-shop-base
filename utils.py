# -------------
# Copyright (c) 2022, bot-shop.me
# All rights reserved.
# -------------

import discord
from discord.ext import commands
from discord.commands import *
import discord.ui
import json
import os
import sqlite3
from datetime import datetime


class Config:
    with open("config.json", "r") as f:
        data = json.load(f)
    token = data["token"]
    guild = [data["guild"]]
    color = int(data["color"], 16)
    owner_id = data["owner_id"]
    prefix = data["prefix"]
    debug = data["debug"]


def change_config(key, value):
    with open("config.json", "r") as f:
        data = json.load(f)
    data[key] = value
    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)
    return True


cmd_colors = {
    "bold": "\u001b[1m",
    "underline": "\u001b[4m",
    "reset": "\u001b[0m",
    "force": "\u001b[0m",
    "error": "\u001b[31m",
    "basic": "\u001b[37m"
}


def debug(arg, dt=True, force=False, error=False):
    if Config.debug or force or error:
        color = "error" if error else "force" if force else "basic"
        if dt:
            print(f"[{datetime.now().strftime('%d.%m | %H:%M:%S')}] {cmd_colors[color]}{arg}\u001b[0m")
        else:
            print(f"{cmd_colors[color]}{arg}\u001b[0m")
