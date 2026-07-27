import os
import random
import discord

# BOTの設定
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# 猫の鳴き声リスト
MEOW_LIST = [
    "にゃー",
    "みー",
    "ペロペロ",
    "ナオーン",
    "ナオーン(女)",
    "ミョーン",
    "コオート(男)",
    "しね",
    "ニャッ！",
    "にゃーん(社会性フィルタ)",
    "黙れガキ",
    "アンニョン",
    "にゃおーん",
    "イク",
    "うにゃーん",
    "にゃんわ",
    "ミョーン",
    "犬",
    "にゃおーん",
    "ニャッ",
    "にゃんにゃん",
    "にょいーん",
    "オ゛ッ♡イク゛ッ♡",
    "にゃにゃーん",
]


@client.event
async def on_ready():
    print(f"ログインしました: {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    meow = random.choice(MEOW_LIST)
    await message.channel.send(meow)


# トークン（鍵）の設定
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)