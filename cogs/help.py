import discord
import random
import math
import logging
from discord import ApplicationContext
from discord.commands import slash_command, SlashCommandGroup, Option, permissions
from discord.ext import commands
from utils.Logger import Logger

logger = logging.getLogger('testbot')


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    guild_ids = ['guild ids for the commands']
    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Help Loaded")

    @slash_command(description="A list of the help commands", guild_ids=guild_ids)
    async def help(self, ctx: discord.ApplicationContext):
        randColour = random.randint(0, 0xffffff)
        e = discord.Embed(
            title= 'List of help commands',
            description= '',
            colour = randColour
        )

        e.add_field(name='Music Commands', value='`-Music`', inline=False)
        e.add_field(name='Moderator Commands', value='`-Mod`',inline=False)
        e.add_field(name='Queue Commands', value='`-qHelp`', inline=False)


        await ctx.respond(embed=e)

    @slash_command(description="Music Commands", guild_ids=guild_ids)
    async def music(self, ctx: ApplicationContext, page: Option(int, "Page number", default=1)):
        commandList = [
        '`play <URL or song name>` Used to play music, queue new songs or resume pause songs.\n',
        '`stop` Used to stop the bot from playing, will also disconnect bot and clear the queue.\n',
        '`skip` Used to skip the currently playing song and start the next in queue.\n',
        '`volume <1-100>` Used to change the volume of the bots music. \n',
        '`q <page number(can be empty)>` Used to show the current song queue. \n',
        '`cq` Used to clear the current song queue.\n',
        '`seek <x amount of seconds>` Used to change time in the song thats playing. \n',
        '`pause` Used to pause music playback. \n',
        '`resume` Used to resume music playback. \n',
        '`repeat` Used to set a song to repeat or to stop repeating. \n',
        '`shuffle` Used to set the current queue to play shuffled or turn shuffle off. \n',
        '`remove <song number>` Used to remove a song from the queue. \n',
        '`now` Used to show the song currently playing and how much time is left. \n',
        '`qn` Used to show a list of saved song queues.\n',
        '`qLoad <name>` Used to load a previously saved song queue. \n',
        '`qSave` Used to save the current song queue for use later. \n'
        ]
        items_per_page = 8
        pages = math.ceil(len(commandList) / items_per_page)
        start = (page - 1) * items_per_page
        end = start + items_per_page
        command_list = ''

        for i, rol in enumerate(commandList[start:end], start=start):
            command_list += f'{rol}\n'
        randColour = random.randint(0, 0xffffff)
        embed = discord.Embed(
            title=f'Commands in the list: {len(commandList)}',
            description=f'{command_list}\n',
            colour=randColour
        )
        embed.set_footer(text=f'Viewing Page: {page}/{pages}')

        await ctx.respond(embed=embed)

    @slash_command(description="Moderation Commands", guild_ids=guild_ids)
    @permissions.has_role("moderation role name")
    async def moderation(self, ctx: ApplicationContext, page: Option(int, "Page Number", default=1)):
        commandList = [
            '`ban <user> <reason>` Used to ban a user in the discord.\n',
            '`kick <user> <reason>` Used to kick a user from the discord.\n',
            '`clear <number of messages(max of 200)>` Used to clear messages in chat.\n',
            '`ping` Used to show the ping to the discord server.\n',
            '`unban <user>` Used to unban a user from the discord.\n',
            '`new` Used to see what new features have been added.\n',
            '`tmute <@ user>` Used to give someone the muted role not allowing any text chat.\n',
            '`tunmute <@ user>` Used to unmute someone from text chat.\n',
            '`mute` Used to mute everyone in the voice channel.\n',
            '`unmute` Used to unmute everyone in the voice channel.\n',
            '`bw <word>` Used to add a word to the banned word list.\n',
            '`wl` Used to show what words are in the banned word list.\n',
            '`cwl` Used to clear the banned word list.\n',
            '`cwarn` Used to clear the warned list.\n',
            '`ar <role name>` Used to add a role to the game role list(will create a role if its not there already). \n',
            '`rmr <role name>` Used to remove a role to the game role list(will remove the role if it is there). \n',
            '`ui <@ user>` or `-ui <user#xxxx>` Used to show info about the user specified. \n',
            '`serverinfo` Used to show info about the server. \n'
        ]
        items_per_page = 8
        pages = math.ceil(len(commandList) / items_per_page)
        start = (page - 1) * items_per_page
        end = start + items_per_page
        command_list = ''

        for i, rol in enumerate(commandList[start:end], start=start):
            command_list += f' {rol}\n'
        randColour = random.randint(0, 0xffffff)
        embed = discord.Embed(
            title=f'Commands in the list: {len(commandList)}',
            description=f'{command_list}\n',
            colour=randColour
        )
        embed.set_footer(text=f'Viewing Page: {page}/{pages}')
    
        await ctx.respond(embed=embed)

    @slash_command(description="Queue Commands", guild_ids=guild_ids)
    async def qhelp(self, ctx: ApplicationContext, page: Option(int, "Page Number", default=1)):
        commandList = [
            '`addQueue` Used to create a new saved queue. \n',
            '`queues` Used to show the list of saved queues. \n',
            ]

        items_per_page = 8
        pages = math.ceil(len(commandList) / items_per_page)
        start = (page - 1) * items_per_page
        end = start + items_per_page
        command_list = ''

        for i, rol in enumerate(commandList[start:end], start=start):
            command_list += f' {rol}\n'
        randColour = random.randint(0, 0xffffff)
        embed = discord.Embed(
            title=f'Commands in the list: {len(commandList)}',
            description=f'{command_list}\n',
            colour=randColour
        )
        embed.set_footer(text=f'Viewing Page: {page}/{pages}')

        await ctx.respond(embed=embed)

def setup(client):
    client.add_cog(Help(client))
