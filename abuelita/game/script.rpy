# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Abuelita", color='#ff5100')
define m = Character("Me", color='#006aff')
define ym = Character("Me (Younger)", color='#006aff')

# The game starts here.

label start:
    scene bg house outside
    with dissolve

    "Abuelita died of being super old a week ago now."

    "I'm going to her house to look through old photos and cry and whatever"

    show bg house inside
    with fade

    "It's weird seeing it empty."

    "Hey look a trunk that is probably filled with old memories."

    scene bg house inside trunk

menu:
    "What should I do with this really really cool trunk?"

    "Open it!":
        jump memories

    "You know what I'm actually not really feeling memories right now":
        jump do_nothing

label memories:
    scene bg trunk open
    call screen memories

label spy:
    "WHOA A SPY THING"

    return

label do_nothing:
    "I'll deal with this later."

    scene bg house outside

    "Sometimes not playing the game is a way of winning, probably."

    "The End."

    return
