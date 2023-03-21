from bot import main_color, add_log
import nextcord as nc
from nextcord.ext import commands

red = nc.Color.red()
blue = nc.Color.blue()
green = nc.Color.green()
default = nc.Color.default()
random = nc.Color.random()


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @nc.slash_command(description="Бот пишет сообщение которое ты написал в поле")
    async def sendmessage(self, interaction: nc.Interaction, message, message_count=1):
        add_log(interaction.user.name, 'sendmessage')
        message_count_limit = 50
        await interaction.response.defer(ephemeral=True)
        if int(message_count) == 0:
            embed = nc.Embed(title='Ошибка!', color=main_color)
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/1085608393907110040/1086964500181291059/scale_1200_2.gif')
            await interaction.followup.send(embed)
        if int(message_count) > message_count_limit:
            embed = nc.Embed(title='Ошибка!',
                             description=f'> Нельзя указывать этот параметр больше {message_count_limit} 😡😡😡',
                             color=int(main_color))
            await interaction.followup.send(embed=embed)
        else:
            for i in range(int(message_count)):
                await interaction.channel.send(message)
            await interaction.followup.send('Бот закончил срать сообщениями 🥳🥳🥳')

    @commands.has_permissions(administrator=True)
    @nc.slash_command(description='Позволяет написать ембедами')
    async def sendembed(self, interaction: nc.Interaction, title, description=None, image=None, color=main_color):
        try:
            add_log(interaction.user.name, 'sendembed')
            embed = nc.Embed(title=f'{title}', description=f'{description}', color=color)
        except ValueError:
            embed = nc.Embed(title=f'{title}', description=f'{description}', color=main_color)
        embed.set_image(url=image)
        await interaction.channel.send(embed=embed)
        await interaction.followup.send('Бот успешно! написал ваш ембед 🥳🥳🥳')


def setup(bot):
    bot.add_cog(Main(bot))
