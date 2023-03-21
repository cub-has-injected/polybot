from bot import add_log
import nextcord as nc
from nextcord.ext import commands
import json


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''@commands.has_permissions(administrator=True)
    @nc.slash_command(description='Позволяет отправлять темплейты')
    async def sendtemplate(self, interaction: nc.Interaction, template):
        add_log(interaction.user.name, 'sendtemplate')
        with open("templates.json", "r") as file:
            messages = json.load(file)

            for message in messages:
                await interaction.followup.send('Бот успешно! написал ваш темплейт 🥳🥳🥳')
                await interaction.channel.send(template)

    @commands.has_permissions(administrator=True)
    @nc.slash_command(description='Позволяет записать сообщение в темлейт')
    async def addtemplate(self, message: nc.Message, name):
        add_log(message.author.name, 'addtemplate')
        name = {"content": message.content, 'author': message.author.name, 'nick': message.author.nick,
                'author_id': message.author.id,
                'channel': message.channel.name, 'timestamp': str(message.created_at)}
        with open("templates.json", "a") as file:
            json.dump(name, file)
            file.write("\n")'''


def setup(bot):
    bot.add_cog(Main(bot))
