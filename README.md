# EventBot
EventBot is a bot for Discord written in Python using [discord.py](https://github.com/Rapptz/discord.py) that cycles the server image for special events and holidays.

## How To Use
- Download a [release]() or [clone]() the repo
  - Extract files if necessary
- Rename *demo_config.toml* to *config.toml*
- Put desired images in the *images* directory
- In the config:
  - *Bot*
    - Set *token* to your [Discord application](https://discord.com/developers/applications) bot token
    - Set *key* to a bot key or leave alone for default
  - *Settings*
    - Set *server_id* to the ID of the server you wish to cycle the icon of
    - Set *default_image_name* to the name of the image that will be the icon when "events" don't take place
  - *Events*
    - You can specify as many events as needed
    - Set *image_name* to the name of the image to set icon to
    - Set *date_start* to the date in which the icon will be changed to
    - Set *date_end* to the date in which the icon will be reset to specified default
    - See [*demo_config.toml*](https://github.com/MiningMark48/EventBot/blob/master/demo_config.toml) for example usage


## Todo
- [x] Get working
- [ ] Add support for multiple servers