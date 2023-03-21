import nextcord as nc
from nextcord.ext import commands
from os import listdir
import logging

main_color = 0x9c0c0c

bot = commands.Bot(
    intents=nc.Intents.all(),
    help_command=None)

logging.basicConfig(level=logging.INFO)

file_handler = logging.FileHandler('bot.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.addHandler(file_handler)


def add_log(user, command_name):
    logging.info(f"Команда '{command_name}' была вызвана пользователем **{user}**'")


def setup_log():
    logging.info(f"Бот успешно запущен 🥳🥳🥳")


@bot.event
async def on_ready():
    setup_log()


@commands.has_permissions(administrator=True)
@bot.slash_command(description="Останавливает бота")
async def stop(interaction: nc.Interaction, extension):
    await interaction.response.defer(ephemeral=True)
    if interaction.user.id == 756172667266007082 or interaction.user.roles == 1086704578659094640:
        bot.unload_extension(f'cogs.{extension}')
        embed = nc.Embed(title='Бот успешно остановлен :partying_face::partying_face::partying_face:', color=main_color)
        await interaction.user.send(embed=embed)
    else:
        embed = nc.Embed(title='Вы не разработчик бота :rage::rage::rage:', color=main_color)
        await interaction.followup.send(embed=embed)


@commands.has_permissions(administrator=True)
@bot.slash_command(description="Перезагружает бота")
async def reload(interaction: nc.Interaction, extension):
    await interaction.response.defer(ephemeral=True)
    if interaction.user.id == 756172667266007082 or interaction.user.roles == 1086704578659094640:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        embed = nc.Embed(title='Бот успешно перезагружен :partying_face::partying_face::partying_face:',
                         color=main_color)
        await interaction.user.send(embed=embed)
    else:
        embed = nc.Embed(title='Вы не разработчик бота :rage::rage::rage:', color=main_color)
        await interaction.followup.send(embed=embed)


for filename in listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("")
