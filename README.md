# Abata Bot

A Discord bot that provides random anime waifu images and anime titles. Users can choose between SFW and NSFW content categories to receive themed images and explore random anime titles with detailed information.

## Prerequisites

- **Python 3.8 or higher**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

- **Discord Bot Token**: Create a Discord bot and obtain its token from the [Discord Developer Portal](https://discord.com/developers/applications).

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ch1kulya/AbataBot.git
    cd AbataBot
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:
    - Create a `.env` file in the project root:
        ```env
        DISCORD_TOKEN=your_discord_bot_token_here
        ```
    - Replace `your_discord_bot_token_here` with your actual Discord bot token.

## Deployment

1. **Run the Bot**:
    ```bash
    python bot.py
    ```

2. **Invite the Bot to Your Server**:
    - Generate an invite link from the Discord Developer Portal with the necessary permissions and add the bot to your desired server.

3. **Using the Bot**:
    - Use the `/waifu` command to get random waifu images.
    - Use the `/random` command to fetch random anime titles.

## Commands

- **/waifu**
    - **Description**: Get a random anime waifu image.
    - **Parameters**:
        - `type`: Choose content type (`SFW`, `NSFW`).
        - `category`: Choose waifu category (e.g., `waifu`, `neko`, `hug`, etc.).

- **/random**
    - **Description**: Get a random anime title with detailed information.

## License

This project is licensed under the [MIT License](LICENSE).
