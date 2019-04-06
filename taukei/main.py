import discord
import os
from discord.ext import commands

client = discord.Client()
TOKEN = ""
language = ""

token = str(input("Discord bot token: "))
TOKEN = os.environ["DISCORD_BOT_TOKEN"] = token

while True:
    language = str(input("Choose the language(pt(portuguese) or en(english)): "))

    if language == 'pt' or language == 'portuguese':
        language = 'pt'
        break
    elif language == 'en' or language == 'english':
        language = 'en'
        break

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
                            `--`----'    '---'      `----'""")
    print("\n\nLogged in as")
    print(client.user.name)
    print(client.user.id)
    if language == "pt":
        print("Eu sou TAUKEI, ta ok? +help para saber mais comandos")
    elif language == "en":
        print("I am... TAUKEI... (sorry this joke doesn't work in english ;-;) +help for commands")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if language == "pt":
        if message.content.startswith("+oi"):
            await client.send_message(message.channel, "Olá amigão, meu nome é TAUKEI... ta ok?")
    elif language == "en":
        if message.content.startswith("+hello"):
         await client.send_message(message.channel, "Hey kiddo, my name is TAUKEI. Good to see you.")
         await client.send_message(message.channel, "so good :weary: ...")
client.run(TOKEN) 
