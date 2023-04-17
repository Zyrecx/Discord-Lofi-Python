import discord
import wavelink
from discord.ext import commands
import config

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="l!", intents=intents)

async def connect_nodes():
    await bot.wait_until_ready()
    await wavelink.NodePool.create_node(bot=bot,
                                        host=config.HOST,
                                        port=config.PORT,
                                        password=config.PASSWORD)

@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f'Node: <{node.identifier}> is ready!')

@bot.event
async def on_ready():
    await bot.loop.create_task(connect_nodes())
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="lofi for you"))
    print("READY")

async def join_vc():
    voice = await bot.fetch_channel(config.VC)  
    guild = await bot.fetch_guild(config.GUILD)
    vc = await voice.connect(cls=wavelink.Player)
    url = await wavelink.NodePool.get_node().get_tracks(wavelink.YouTubeTrack, config.URL)
    await guild.change_voice_state(channel=voice,self_deaf=True)
    await vc.play(url[0])

@bot.event
async def on_voice_state_update(member, before, after):
        if after.channel is not None:
            if after.channel.id == config.VC:  
                node = wavelink.NodePool.get_node()
                guild = await bot.fetch_guild(config.GUILD)
                voice = node.get_player(guild)
                if voice is None:
                    await join_vc()
                    
        elif before.channel and not after.channel:  
            vc = await bot.fetch_channel(config.VC)  
            node = wavelink.NodePool.get_node()
            guild = await bot.fetch_guild(config.GUILD)
            voice = node.get_player(guild)
            if len(vc.members) <= 1 and voice is not None:
                await voice.disconnect()
                
bot.run(config.TOKEN)
