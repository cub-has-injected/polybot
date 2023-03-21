from bot import main_color, add_log
import nextcord as nc
from nextcord.ext import commands
import datetime


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @nc.slash_command(description="Позволяет замутить участника")
    async def mute(self, interaction: nc.Interaction, member: nc.Member, reason='нету', seconds: int = None,
                   minutes: int = None, hours: int = None):
        await interaction.response.defer(ephemeral=True)
        try:
            add_log(interaction.user.name, 'mute')
            if member != interaction.user:
                await member.timeout(reason=reason,
                                     timeout=datetime.timedelta(seconds=seconds, minutes=minutes, hours=hours))
                embed = nc.Embed(title=f'{member} был замучен!',
                                 description=f'> **на:** \n{seconds} Секунд\n{minutes} Минут\n{hours}'
                                             f'Часов\n>**по причине:** {reason}',
                                 color=main_color)
                await interaction.channel.send(embed=embed)
            else:
                embed = nc.Embed(title='Ошибка!', description=f'> Вы не можете замутить самого себя!', color=main_color)
                await interaction.followup.send(embed=embed)
        except nc.DiscordServerError:
            embed = nc.Embed(title='Ошибка!', description=f'> ты долбоёб', color=main_color)
            await interaction.followup.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @nc.slash_command(description="Позволяет размутить участника")
    async def unmute(self, interaction: nc.Interaction, member: nc.Member, reason='нету'):
        try:
            add_log(interaction.user.name, 'unmute')
            await member.remove_timeout()
            embed = nc.Embed(title=f'{member} был размучен!',
                             description=f'> **по причине:** {reason}', color=main_color)
            await interaction.channel.send(embed=embed)
        except nc.DiscordServerError:
            embed = nc.Embed(title='Ошибка!', description=f'> ты долбоёб', color=main_color)
            await interaction.followup.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))
