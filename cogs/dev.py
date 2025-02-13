import discord
from discord.ext import commands
doob_logo = "https://cdn.discordapp.com/avatars/680606346952966177/ada47c5940b5cf8f7e12f61eefecc610.webp?size=1024"

class dev(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # Gives user the dev's Discord.
    @commands.command(aliases=['developer', 'devteam'])
    async def dev(self, ctx):
        embed = discord.Embed(title="mmatt developed me!", colour=discord.Color.blue())

        embed.add_field(name="Dev's Discord", value="<@308000668181069824>")
        embed.set_thumbnail(url=doob_logo)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(dev(client))