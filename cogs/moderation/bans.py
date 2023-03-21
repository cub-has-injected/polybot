from bot import main_color, add_log
import nextcord as nc
from nextcord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @nc.slash_command(description="Позволяет забанить участника")
    async def ban(self, interaction: nc.Interaction, member: nc.Member, reason='нету'):
        add_log(interaction.user.name, 'ban')
        try:
            if member != interaction.user:
                await member.ban(reason=reason)
                embed = nc.Embed(title=f'{member} был забанен к хуям!',
                                 description=f'> **по причине:** {reason}', color=main_color)
                await interaction.channel.send(embed=embed)
            else:
                embed = nc.Embed(title='Ошибка!', description='> Вы не можете забанить самого себя!', color=main_color)
                await interaction.followup.send(embed=embed)
        except nc.DiscordServerError:
            embed = nc.Embed(title='Ошибка!', description=f'> ты долбоёб', color=main_color)
            await interaction.followup.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @nc.slash_command(description="Позволяет разбанить пользователя")
    async def unban(self, interaction: nc.Interaction, id, reason='нету'):
        user = await self.bot.fetch_user(id)
        try:
            add_log(interaction.user.name, 'unban')
            await interaction.guild.unban(user)
            embed = nc.Embed(title=f'{user} разбанен!', description=f'> **по причине:** {reason}',
                             color=int(main_color))
            await interaction.channel.send(embed=embed)
        except nc.DiscordServerError:
            embed = nc.Embed(title='Ошибка!', description=f'> Не удалось разбанить {user}', color=int(main_color))
            await interaction.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))
