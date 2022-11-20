# -------------
# Copyright (c) 2022, bot-shop.me
# All rights reserved.
# -------------

from utils import *


class Modal(discord.ui.Modal):
    def __init__(self, type):
        if type == "color":
            super().__init__(title="Basic embed color")
            self.add_item(discord.ui.InputText(label="Your color", placeholder="Hex color", custom_id="color", required=True, style=discord.InputTextStyle.short))
        elif type == "prefix":
            super().__init__(title="Bot Prefix")
            self.add_item(discord.ui.InputText(label="Your prefix", placeholder=f"{Config.prefix}", custom_id="prefix", required=True, style=discord.InputTextStyle.short))
        elif type == "guild":
            super().__init__(title="Guild ID")
            self.add_item(discord.ui.InputText(label="Guild ID", placeholder=f"{Config.guild}", custom_id="guild", required=True, style=discord.InputTextStyle.short))
        elif type == "token":
            super().__init__(title="Bot Token")
            self.add_item(discord.ui.InputText(label="New Bot token", placeholder=f"Token", custom_id="token", required=True, style=discord.InputTextStyle.short))
        elif type == "owner":
            super().__init__(title="Bot Owner")
            self.add_item(discord.ui.InputText(label="New Bot owner", placeholder=f"Owner ID", custom_id="owner", required=True, style=discord.InputTextStyle.short))


    async def callback(self, interaction: discord.Interaction):
        change_config(self.children[0].custom_id, self.children[0].value)
        debug(f"Changed {self.children[0].custom_id} to {self.children[0].value} (restart required)", force=True)
        await interaction.response.edit_message(content="Settings Changed! Restart the bot to apply the changes", view=None)


class SettingView(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot


    @discord.ui.button(label="Prefix", style=discord.ButtonStyle.gray, custom_id="prefix", emoji="⚙️")
    async def prefix(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(Modal("prefix"))



    @discord.ui.button(label="Color", style=discord.ButtonStyle.gray, custom_id="color", emoji="⚙️")
    async def prefix(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(Modal("color"))


    @discord.ui.button(label="Guild", style=discord.ButtonStyle.gray, custom_id="guild", emoji="⚙️")
    async def prefix(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(Modal("guild"))


    @discord.ui.button(label="Token", style=discord.ButtonStyle.gray, custom_id="token", emoji="⚙️")
    async def token(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(Modal("token"))


    @discord.ui.button(label="Owner", style=discord.ButtonStyle.gray, custom_id="owner", emoji="⚙️")
    async def owner(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_modal(Modal("owner"))


class Settings(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot


    @discord.ui.button(label="Settings", style=discord.ButtonStyle.gray, custom_id="settings", emoji="⚙️")
    async def settings(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Settings", color=Config.color)
        embed.add_field(name="Prefix", value=f"Current prefix: {Config.prefix}", inline=False)
        embed.add_field(name="Color", value=f"Current color: {Config.color}", inline=False)
        embed.add_field(name="Guild/s", value=f"Current guild id/s: {conv_list(Config.guild)}", inline=False)
        embed.add_field(name="Token", value=f"Current token starts with: {Config.token[:5]}", inline=False)
        embed.add_field(name="Owner", value=f"Current owner: {self.bot.get_user(int(Config.owner_id)).mention}", inline=False)
        await interaction.response.edit_message(embed=embed)


class BotShop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(guild_ids=Config.guild, permissions=["administrator"])
    async def help(self, ctx):
        if ctx.author.id == int(Config.owner_id):
            embed = discord.Embed(title="Bot Shop Bot", color=Config.color, description="""
    `Dieser Bot wurde von bot-shop.me entwickelt`
    
    Um hilfe mit deinem Bot zu bekommen, besuche https://discord.bot-shop.me oder schreibe eine E-Mail an help@bot-shop.me
            """)

            await ctx.respond(embed=embed, view=Settings(self.bot), ephemeral=True)
        else:
            embed = discord.Embed(title="Bot Shop Bot", color=Config.color, description="""
    `Dieser Bot wurde von bot-shop.me entwickelt`
    
    Um hilfe mit deinem Bot zu bekommen, besuche https://discord.bot-shop.me oder schreibe eine E-Mail an help@bot-shop.me
    """)
            await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(BotShop(bot))

