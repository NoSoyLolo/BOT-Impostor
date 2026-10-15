# discord-impostor-bot

A standalone Discord party game bot that assigns secret characters or video games to players via Direct Messages, randomly assigning one or more Impostors who must fake their knowledge based only on a subtle category hint.

## Dependencies

* `discord.py`
* `asyncio`

Install dependencies first using `pip`:

```bash
pip install -r requirements.txt
```

Set your bot token as an environment variable and start the bot:

```bash
export TOKEN="your_discord_bot_token"
python main.py
```

Ensure your bot has **Server Members Intent** and **Message Content Intent** enabled in the [Discord Developer Portal](https://discord.com/developers/applications).

## How It Works

### Game Flow & Execution

When a game is initialized using the `!jugar` command:

* **Roles Distribution:** The bot randomly selects the secret topic (a character or a video game) and assigns Impostor roles based on the command arguments.
* **Innocents (Non-Impostors):** Receive a Direct Message with the exact secret topic along with a DuckDuckGo image search link for reference.
* **Impostors:** Receive a Direct Message notifying them of their Impostor role and providing a single general hint (`Personaje` or `Videojuego`).
* **Turn Order:** A randomized turn order list is published in the channel to structure discussion without revealing anyone's identity or role.

## Player Guide

### Direct Message Privacy

Players participating in the game **must enable Direct Messages (DMs)** from server members in their Discord Privacy & Safety settings; otherwise, the bot will fail to deliver secret roles.

### Starting a Game

To start a game, run the `!jugar` command in any channel the bot can read and send messages in.

```text
!jugar [impostors_count] @player1 @player2 @player3 ...
```

#### Examples

* Single impostor game:
  ```text
  !jugar @User1 @User2 @User3 @User4
  ```
* Multi-impostor game:
  ```text
  !jugar 2 @User1 @User2 @User3 @User4 @User5
  ```

> **Note:** If the specified number of impostors is higher than or equal to the total player count, the bot automatically adjusts the count to ensure at least one innocent player remains.
