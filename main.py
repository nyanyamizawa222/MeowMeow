import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Renderのスリープ防止（外部からのアクセスを受け取るWebサーバー）
def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()
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

    # 5回に1回（20%の確率）だけ反応する設定
    if random.randint(1, 5) == 1:
        meow = random.choice(MEOW_LIST)
        await message.channel.send(meow)


# トークン（鍵）の設定
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)
