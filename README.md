# Discord Lofi Bot (Python)

This is a Discord bot built with discord.py and wavelink that plays lofi music in a voice channel. 

## Installation

To use this bot, you will need to install the following libraries using pip:

```
pip install discord
pip install wavelink==1.3.5
```

## Configuration


Before using Lofi Bot, you need to edit the config.py file and provide the following information:

**TOKEN**: Your Discord bot token.

**GUILD**: Your Discord server ID.

**URL**: The YouTube link to the lo-fi music you want to play.

**VC**: The ID of the voice channel you want the bot to join.

**HOST**: The host address for your Lavalink node.

**PORT**: The port for the Lavalink server.

**PASSWORD**: The password for the Lavalink server.

You can find servers for wave link 
[here](https://lavalink.darrennathanael.com/#tunnelbroker-guide).

## Usage
The bot will automatically join the voice channel when a user enters, and leave when the channel is empty.

After you have edited the `config.py` file, simply run the bot using the following command:
```
python main.py
```



