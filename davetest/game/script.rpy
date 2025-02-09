# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dave = Character('Dave', color="#b59aff")
define me = Character('Me', color="#c8ffc8")
default insult = False

# The game starts here.

label start:
    dave "Welcome to my visual novel, cool guy"

menu:
    "YOU ARE THE NERD":
        jump insult

    "Thanks, I guess":
        jump move_on

label insult:
    $ insult = True

    me "YOU ARE THE NERD!"

    dave "Nice comeback... double-nerd!"

    jump end

label move_on:
    me "Thanks, I guess"

    dave "You're welcome, stupid"

    jump end

label end:
    if insult:
        "THE END, maybe you should have been nicer"
    else:
        "THE END, guess being nice didn't help"
