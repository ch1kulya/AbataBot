## Abata Bot

is a Discord bot that provides random anime images and titles from SFW and NSFW content categories.

### Usage

- `/waifu` command to get random waifu images.
- `/random` command to fetch random Anilibria titles.
- `/nekos` command to get random neko images.
- `/hmtai` command to get random hentai images.

### Prerequisites

- **Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).
- **Bot Token**: Create a Discord bot and obtain its token from the [Discord Developer Portal](https://discord.com/developers/applications).

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ch1kulya/AbataBot.git
    cd AbataBot
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables**:
    - Create a `.env` file in the project root:

        ```env
        DISCORD_TOKEN=bot_token
        ```
    - Replace `bot_token` with your actual Discord bot token.

### Deployment

1. **Run the Bot**:

    ```bash
    python bot.py
    ```

2. **Invite the Bot to Your Server**:
    - Generate an invite link from the Discord Developer Portal with the necessary permissions and add the bot to your desired server.

#### Contributing is encouraged 🤗
