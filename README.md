![Eventus Banner](.README_images/banner.png | width=512)

Eventus is a bot for Discord written in Python using [discord.py](https://github.com/Rapptz/discord.py) that cycles the server image for special events and holidays.

## How To Use
- Download a [release](https://github.com/MiningMark48/EventBot/releases) or [clone](https://github.com/MiningMark48/EventBot/archive/master.zip) the repo
  - Extract files if necessary
- Rename [*demo_config.toml*](https://github.com/MiningMark48/EventBot/blob/master/demo_config.toml) to *config.toml*
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

### Things to note
- If there are duplicate dates, it uses whatever was first and then stops
- If an event starts on the same as another one ends, the server icon will reset to default and then an hour later (by default), it will be set to the new event's icon

## Todo
- [x] Get working
- [x] Use with Tidal Wave
- [ ] Add support for multiple servers