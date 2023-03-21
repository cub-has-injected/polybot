from numexpr import evaluate
import nextcord as nc
from nextcord.ext import commands
from bot import main_color, add_log


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nc.slash_command(description='Просто калькулятор')
    async def calc(self, interaction: nc.Interaction, expr):
        try:
            add_log(interaction.user.name, 'calc')
            result = evaluate(expr)
            if result == int(result):
                embed = nc.Embed(title=f'Интересный факт но:', description=f'```{expr} = {int(result)}```',
                                 color=main_color)
            else:
                embed = nc.Embed(title=f'Интересный факт но:', description=f'```{expr} = {result}```', color=main_color)
            await interaction.send(embed=embed)
        except ZeroDivisionError:
            embed = nc.Embed(title=f'Интересный факт но:', color=main_color)
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/1085608393907110040/1086964500181291059/scale_1200_2.gif')
            await interaction.followup.send(embed=embed)
        except SyntaxError:
            embed = nc.Embed(title=f'Интересный факт но:',
                             description=f'```Вы ввели неправильный символ попробуйте позднее```', color=main_color)
            await interaction.followup.send(embed=embed)
        except KeyError:
            embed = nc.Embed(title=f'Интересный факт но:',
                             description=f'Зачем ты ввёл: ```"{expr}"```?', color=main_color)
            await interaction.followup.send(embed=embed)
        except nc.ApplicationInvokeError:
            embed = nc.Embed(title=f'Интересный факт но:',
                             description=f'```Нельзя вводить слишком большой пример 😡😡😡```?', color=main_color)
            await interaction.followup.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))
