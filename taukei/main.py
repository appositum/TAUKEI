import discord
import os
from discord.ext import commands

client = discord.Client()
TOKEN = ""
language = ""

token = str(input("Discord bot token: "))
TOKEN = os.environ["DISCORD_BOT_TOKEN"] = token

language = str(input("Choose the language(pt(portuguese) or en(english)): "))

@client.event
async def on_ready():
    print("""                                                                        
      ,/   .`|                                  ,--.                          
    ,`   .'  : ,---,                        ,--/  /|    ,---,.   ,---,        
  ;    ;     /'  .' \               ,--, ,---,': / '  ,'  .' |,`--.' |        
.'___,/    ,'/  ;    '.           ,'_ /| :   : '/ / ,---.'   ||   :  :        
|    :     |:  :       \     .--. |  | : |   '   ,  |   |   .':   |  '        
;    |.';  ;:  |   /\   \  ,'_ /| :  . | '   |  /   :   :  |-,|   :  |        
`----'  |  ||  :  ' ;.   : |  ' | |  . . |   ;  ;   :   |  ;/|'   '  ;        
    '   :  ;|  |  ;/  \   \|  | ' |  | | :   '   \  |   :   .'|   |  |        
    |   |  ''  :  | \  \ ,':  | | :  ' ; |   |    ' |   |  |-,'   :  ;        
    '   :  ||  |  '  '--'  |  ; ' |  | ' '   : |.  \'   :  ;/||   |  '        
    ;   |.' |  :  :        :  | : ;  ; | |   | '_\.'|   |    \'   :  |        
    '---'   |  | ,'        '  :  `--'   \'   : |    |   :   .';   |.'         
            `--''          :  ,      .-./;   |,'    |   | ,'  '---'           
                            `--`----'    '---'      `----'                    
          """)                                                           
    print("\n\nLogged in as")
    print(client.user.name)
    print(client.user.id)
    if language == "pt" or language == "portuguese":
        print("Eu sou TAUKEI, ta ok? ?help para saber mais comandos")
    elif language == "en" or language == "english":
        print("I am TAUKEI... (this joke does not work in english ;-;) /help for commands")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if language == "pt" or language == "portuguese":
        if message.content.startswith("?oi"):
            await client.send_message(message.channel, "Olá amigão, meu nome é TAUKEI... ta ok?")
    elif language == "en" or language == "english":
        if message.content.startswith("?hello"):
         await client.send_message(message.channel, "Hello, my name is TAUKEI... so good to see you")
         await client.send_message(message.channel, "so good...")
client.run(TOKEN) 
