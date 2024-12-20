import discord
from discord import app_commands
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv
import random
import hmtai

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("Failed to load token. Ensure DISCORD_TOKEN is set in the .env file.")

intents = discord.Intents.default()
intents.message_content = False

bot = commands.Bot(command_prefix='!', intents=intents)

TYPES = {
    'sfw': 'SFW',
    'nsfw': 'NSFW'
}

CATEGORIES = {
    'sfw': [
        {'value': 'waifu', 'name': 'Waifu', 'color': discord.Color.blue()},
        {'value': 'neko', 'name': 'Neko', 'color': discord.Color.purple()},
        {'value': 'shinobu', 'name': 'Shinobu', 'color': discord.Color.green()},
        {'value': 'megumin', 'name': 'Megumin', 'color': discord.Color.orange()},
        {'value': 'bully', 'name': 'Bully', 'color': discord.Color.red()},
        {'value': 'cuddle', 'name': 'Cuddle', 'color': discord.Color.gold()},
        {'value': 'cry', 'name': 'Cry', 'color': discord.Color.dark_blue()},
        {'value': 'hug', 'name': 'Hug', 'color': discord.Color.dark_gold()},
        {'value': 'awoo', 'name': 'Awoo', 'color': discord.Color.dark_purple()},
        {'value': 'kiss', 'name': 'Kiss', 'color': discord.Color.dark_embed()},
        {'value': 'lick', 'name': 'Lick', 'color': discord.Color.light_grey()},
        {'value': 'pat', 'name': 'Pat', 'color': discord.Color.dark_teal()},
        {'value': 'smug', 'name': 'Smug', 'color': discord.Color.dark_red()},
        {'value': 'bonk', 'name': 'Bonk', 'color': discord.Color.dark_magenta()},
        {'value': 'yeet', 'name': 'Yeet', 'color': discord.Color.dark_orange()},
        {'value': 'blush', 'name': 'Blush', 'color': discord.Color.pink()},
        {'value': 'smile', 'name': 'Smile', 'color': discord.Color.yellow()},
        {'value': 'wave', 'name': 'Wave', 'color': discord.Color.teal()},
        {'value': 'highfive', 'name': 'High Five', 'color': discord.Color.magenta()}
    ],
    'nsfw': [
        {'value': 'waifu', 'name': 'Waifu', 'color': discord.Color.dark_red()},
        {'value': 'neko', 'name': 'Neko', 'color': discord.Color.dark_purple()},
        {'value': 'blowjob', 'name': 'Blowjob', 'color': discord.Color.red()}
    ]
}

NSFW_CATEGORIES = [
    {'value': 'ass', 'name': 'Ass', 'color': discord.Color.red()},
    {'value': 'cum', 'name': 'Cum', 'color': discord.Color.gold()},
    {'value': 'classic', 'name': 'Classic', 'color': discord.Color.orange()},
    {'value': 'creampie', 'name': 'Creampie', 'color': discord.Color.dark_gold()},
    {'value': 'hentai', 'name': 'Hentai', 'color': discord.Color.dark_purple()},
    {'value': 'masturbation', 'name': 'Masturbation', 'color': discord.Color.dark_orange()},
    {'value': 'ero', 'name': 'Ero', 'color': discord.Color.magenta()},
    {'value': 'orgy', 'name': 'Orgy', 'color': discord.Color.dark_grey()},
    {'value': 'yuri', 'name': 'Yuri', 'color': discord.Color.magenta()},
    {'value': 'pantsu', 'name': 'Pantsu', 'color': discord.Color.lighter_grey()},
    {'value': 'glasses', 'name': 'Glasses', 'color': discord.Color.blurple()},
    {'value': 'blowjob', 'name': 'Blowjob', 'color': discord.Color.dark_red()},
    {'value': 'boobjob', 'name': 'Boobjob', 'color': discord.Color.pink()},
    {'value': 'footjob', 'name': 'Footjob', 'color': discord.Color.dark_blue()},
    {'value': 'handjob', 'name': 'Handjob', 'color': discord.Color.dark_magenta()},
    {'value': 'boobs', 'name': 'Boobs', 'color': discord.Color.pink()},
    {'value': 'thighs', 'name': 'Thighs', 'color': discord.Color.dark_blue()},
    {'value': 'pussy', 'name': 'Pussy', 'color': discord.Color.lighter_grey()},
    {'value': 'ahegao', 'name': 'Ahegao', 'color': discord.Color.yellow()},
    {'value': 'uniform', 'name': 'Uniform', 'color': discord.Color.purple()},
    {'value': 'tentacles', 'name': 'Tentacles', 'color': discord.Color.green()},
    {'value': 'gif', 'name': 'GIF', 'color': discord.Color.teal()},
]

NEKOS_CATEGORIES = [
    {'value': 'pat', 'name': 'Pat', 'color': discord.Color.blue()},
    {'value': 'hug', 'name': 'Hug', 'color': discord.Color.green()},
    {'value': 'kiss', 'name': 'Kiss', 'color': discord.Color.pink()},
    {'value': 'slap', 'name': 'Slap', 'color': discord.Color.red()},
    {'value': 'smug', 'name': 'Smug', 'color': discord.Color.purple()},
    {'value': 'neko', 'name': 'Neko', 'color': discord.Color.orange()},
    {'value': 'waifu', 'name': 'Waifu', 'color': discord.Color.gold()},
    {'value': 'cuddle', 'name': 'Cuddle', 'color': discord.Color.magenta()},
    {'value': 'feed', 'name': 'Feed', 'color': discord.Color.teal()},
]

TITLE_TEMPLATES = {
    'waifu': [
        "Your Beloved Waifu Awaits!",
        "Enjoy Your Lovely Waifu!",
        "Here’s Your Waifu!",
        "Love at First Sight with Your Waifu!",
        "Your Perfect Waifu Just Arrived!"
    ],
    'neko': [
        "Your Adorable Neko!",
        "Enjoy Your Cute Neko!",
        "Here’s Your Neko!",
        "Purr-fect Neko Coming Your Way!",
        "Snuggle with Your Neko!"
    ],
    'shinobu': [
        "Shinobu is Here!",
        "Enjoy Shinobu’s Company!",
        "Here’s Shinobu!",
        "Elegance and Grace with Shinobu!",
        "Shinobu Brings Peace!"
    ],
    'megumin': [
        "Meet the Explosive Megumin!",
        "Get Ready for Megumin's Magic!",
        "Here’s Megumin!",
        "Blast Off with Megumin!",
        "Unleash the Power of Megumin!"
    ],
    'bully': [
        "Don't Let the Bully Distract You!",
        "Bully Be Gone with this Image!",
        "Here’s the Bully!",
        "Stand Strong Against the Bully!",
        "Bully Out with a Powerful Image!"
    ],
    'cuddle': [
        "Get Cozy with a Cuddle!",
        "Enjoy a Warm Cuddle!",
        "Here’s a Cuddle!",
        "Embrace the Warmth of a Cuddle!",
        "Feel the Love with a Cuddle!"
    ],
    'cry': [
        "A Moment of Sadness Just for You.",
        "Don’t Cry, Enjoy the Image!",
        "Here’s to You Embracing Emotion.",
        "Let Your Tears Flow with this Image.",
        "Feeling Blue? Here’s Something for You."
    ],
    'hug': [
        "Sending You a Warm Hug!",
        "Enjoy a Loving Hug!",
        "Here’s a Hug Just for You!",
        "Feel the Comfort of a Hug!",
        "A Hug to Brighten Your Day!"
    ],
    'awoo': [
        "Awoo! Here's Your Image!",
        "Enjoy the Awoo Moment!",
        "Here’s an Awoo for You!",
        "Awoo-ulicious Image Coming Your Way!",
        "Feel the Awoo Spirit!"
    ],
    'kiss': [
        "A Sweet Kiss Just for You!",
        "Enjoy the Lovely Kiss!",
        "Here’s a Kiss!",
        "A Kiss to Make Your Day!",
        "Sending You a Gentle Kiss!"
    ],
    'lick': [
        "A Playful Lick for You!",
        "Enjoy the Lick!",
        "Here’s a Lick!",
        "A Lick to Brighten Your Mood!",
        "Feel the Playfulness with a Lick!"
    ],
    'pat': [
        "A Gentle Pat for You!",
        "Enjoy the Pat!",
        "Here’s a Pat!",
        "A Pat to Show Some Love!",
        "Feel the Support with a Pat!"
    ],
    'smug': [
        "Feeling Smug? Here's Something for You!",
        "Enjoy Your Smug Moments!",
        "Here’s a Smug Image!",
        "Show Off Your Smug Side!",
        "Embrace the Smug Vibes!"
    ],
    'bonk': [
        "Bonk! Here's Your Image!",
        "Enjoy the Fun Bonk!",
        "Here’s a Bonk!",
        "A Bonk to Lighten the Mood!",
        "Feel the Energy with a Bonk!"
    ],
    'yeet': [
        "Yeet! Enjoy the Image!",
        "Here’s Something to Yeet!",
        "Yeet Your Way with This Image!",
        "Feel the Momentum of Yeet!",
        "Yeet into the Fun World!"
    ],
    'blush': [
        "Look at This Adorable Image and Blush!",
        "Enjoy the Blushing Moment!",
        "Here’s Something to Make You Blush!",
        "Feel the Warmth with a Blush!",
        "A Blushing Surprise for You!"
    ],
    'smile': [
        "A Bright Smile Just for You!",
        "Enjoy the Smile!",
        "Here’s a Smile!",
        "Smile Your Day Away!",
        "Feel the Joy with a Smile!"
    ],
    'wave': [
        "Wave Hello with This Image!",
        "Enjoy the Waving Moment!",
        "Here’s a Wave for You!",
        "Feel the Greeting with a Wave!",
        "A Wave to Brighten Your Day!"
    ],
    'highfive': [
        "High Five! Enjoy the Moment!",
        "Here’s a High Five for You!",
        "Enjoy a Virtual High Five!",
        "Feel the Excitement with a High Five!",
        "Celebrate with a High Five!"
    ],
    'blowjob': [
        "Blowjob Image Coming Your Way!",
        "Enjoy the Blowjob!",
        "Here’s a Blowjob Image!",
        "Feel the Intimacy with this Blowjob!",
        "A Sensual Blowjob for You!"
    ]
}

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is connected and ready.')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands.')
    except Exception as e:
        print(f'Error syncing commands: {e}')

@bot.tree.command(
    name="waifu",
    description="Get a random anime waifu image."
)
@app_commands.describe(
    type="Choose content type",
    category="Choose waifu category"
)
async def waifu(interaction: discord.Interaction, type: str, category: str):
    type = type.lower()
    category = category.lower()

    if type not in TYPES:
        await interaction.response.send_message("❌ **Invalid type.**\nAvailable types: SFW, NSFW", ephemeral=True)
        return

    display_type = TYPES[type]

    valid_categories = [cat['value'] for cat in CATEGORIES[type]]
    if category not in valid_categories:
        display_categories = [cat['name'] for cat in CATEGORIES[type]]
        categories_str = ', '.join(display_categories)
        await interaction.response.send_message(f"❌ **Invalid category for type `{display_type}`.**\nAvailable categories: {categories_str}", ephemeral=True)
        return

    if type == 'nsfw' and not interaction.channel.is_nsfw():
        await interaction.response.send_message("❌ This category contains NSFW content. Please use this command in an NSFW channel.", ephemeral=True)
        return

    api_url = f'https://api.waifu.pics/{type}/{category}'

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as resp:
            if resp.status != 200:
                await interaction.response.send_message("❌ Failed to retrieve image. Please try again later.", ephemeral=True)
                return
            data = await resp.json()
            image_url = data.get('url')
            if not image_url:
                await interaction.response.send_message("❌ Failed to retrieve image.", ephemeral=True)
                return

    display_category = next((cat['name'] for cat in CATEGORIES[type] if cat['value'] == category), category.capitalize())
    embed_title = random.choice(TITLE_TEMPLATES.get(category, ["Here’s your waifu!"]))
    embed_color = next((cat['color'] for cat in CATEGORIES[type] if cat['value'] == category), discord.Color.blue())

    embed = discord.Embed(
        title=embed_title,
        color=embed_color
    )
    embed.set_image(url=image_url)
    embed.set_footer(text=f"Type: {display_type}, Category: {display_category}")

    await interaction.response.send_message(embed=embed)

@waifu.autocomplete('type')
async def waifu_type_autocomplete(interaction: discord.Interaction, current: str):
    types = ['sfw', 'nsfw']
    return [
        app_commands.Choice(name=TYPES[ty], value=ty)
        for ty in types if current.lower() in ty.lower()
    ]

@waifu.autocomplete('category')
async def waifu_category_autocomplete(interaction: discord.Interaction, current: str):
    options = interaction.data.get('options', [])
    selected_type = None
    for option in options:
        if option['name'] == 'type':
            selected_type = option['value'].lower()
            break

    if not selected_type or selected_type not in CATEGORIES:
        return []

    categories = CATEGORIES[selected_type]
    return [
        app_commands.Choice(name=cat['name'], value=cat['value'])
        for cat in categories
        if current.lower() in cat['value'].lower() or current.lower() in cat['name'].lower()
    ]

@bot.tree.command(name="random", description="Get a random anime title")
async def random_command(interaction: discord.Interaction):
    api_url = "https://api.anilibria.tv/v3/title/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status != 200:
                await interaction.response.send_message("Failed to fetch data from Anilibria API.", ephemeral=True)
                return
            data = await response.json()

    name_en = data['names']['en'] if data['names']['en'] else "N/A"
    name_ru = data['names']['ru'] if data['names']['ru'] else "N/A"
    combined_name = f"{name_en} / {name_ru}" if name_en != "N/A" and name_ru != "N/A" else name_en or name_ru or "N/A"
    description = data['description'] if data['description'] else "No description available."
    status = data['status']['string'] if 'status' in data and 'string' in data['status'] else "N/A"
    genres = ", ".join(data['genres']) if data['genres'] else "N/A"
    type_full = data['type']['full_string'] if 'type' in data and 'full_string' in data['type'] else "N/A"
    
    embed = discord.Embed(
        title=combined_name,
        description=description,
        color=discord.Color.gold()
    )
    embed.set_footer(text=f"ID: {data['id']}")
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="Type", value=type_full, inline=True)
    embed.add_field(name="Year", value=data['season']['year'], inline=True)
    embed.add_field(name="Genres", value=genres, inline=True)

    await interaction.response.send_message(embed=embed)
    
@bot.tree.command(
    name="hmtai",
    description="Get a random NSFW image from the hmtai API."
)
@app_commands.describe(
    category="Choose an NSFW category"
)
async def hmtai_command(interaction: discord.Interaction, category: str):
    if not interaction.channel.is_nsfw():
        await interaction.response.send_message("❌ This command can only be used in NSFW channels.", ephemeral=True)
        return

    category = category.lower()

    valid_categories = [cat['value'] for cat in NSFW_CATEGORIES]

    if category not in valid_categories:
        display_categories = [cat['name'] for cat in NSFW_CATEGORIES]
        categories_str = ', '.join(display_categories)
        await interaction.response.send_message(f"❌ **Invalid category.**\nAvailable categories: {categories_str}", ephemeral=True)
        return

    try:
        image_url = hmtai.useHM("nsfw", category)
        if not image_url:
            raise ValueError("Failed to get image URL.")
    except Exception as e:
        await interaction.response.send_message("❌ Failed to retrieve image. Please try again later.", ephemeral=True)
        return

    display_category = next((cat['name'] for cat in NSFW_CATEGORIES if cat['value'] == category), category.capitalize())
    embed_title = f"Here is your image from the {display_category} category!"

    embed_color = next((cat['color'] for cat in NSFW_CATEGORIES if cat['value'] == category), discord.Color.red())

    embed = discord.Embed(
        title=embed_title,
        color=embed_color
    )
    embed.set_image(url=image_url)
    embed.set_footer(text=f"Category: {display_category}")

    await interaction.response.send_message(embed=embed)

# Autocomplete for category
@hmtai_command.autocomplete('category')
async def hmtai_category_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=cat['name'], value=cat['value'])
        for cat in NSFW_CATEGORIES
        if current.lower() in cat['value'].lower() or current.lower() in cat['name'].lower()
    ]
    
@bot.tree.command(
    name="nekos",
    description="Get a random SFW image from the nekos endpoint."
)
@app_commands.describe(
    category="Choose a category"
)
async def nekos_command(interaction: discord.Interaction, category: str):
    category = category.lower()

    valid_categories = [cat['value'] for cat in NEKOS_CATEGORIES]
    if category not in valid_categories:
        display_categories = [cat['name'] for cat in NEKOS_CATEGORIES]
        categories_str = ', '.join(display_categories)
        await interaction.response.send_message(f"❌ **Invalid category.**\nAvailable categories: {categories_str}", ephemeral=True)
        return

    # Fetch the image using hmtai.get("nekos", category)
    try:
        image_url = hmtai.get("nekos", category)
        if not image_url:
            raise ValueError("Failed to retrieve image URL.")
    except Exception as e:
        await interaction.response.send_message("❌ Failed to retrieve image. Please try again later.", ephemeral=True)
        return

    # Find the display category and embed color
    display_category = next((cat['name'] for cat in NEKOS_CATEGORIES if cat['value'] == category), category.capitalize())
    embed_color = next((cat['color'] for cat in NEKOS_CATEGORIES if cat['value'] == category), discord.Color.blue())

    # Create the embed
    embed_title = f"Here's your {display_category} image!"
    embed = discord.Embed(
        title=embed_title,
        color=embed_color
    )
    embed.set_image(url=image_url)
    embed.set_footer(text=f"Category: {display_category}")

    await interaction.response.send_message(embed=embed)

# Autocomplete for 'category'
@nekos_command.autocomplete('category')
async def nekos_category_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=cat['name'], value=cat['value'])
        for cat in NEKOS_CATEGORIES
        if current.lower() in cat['value'].lower() or current.lower() in cat['name'].lower()
    ]

bot.run(TOKEN)
