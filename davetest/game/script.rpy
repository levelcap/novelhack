# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dave = Character('Dave', color="#b59aff")
define me = Character('Me', color="#c8ffc8")
default insult = False

# The game starts here.

label start:
    show bg city
    with fade
    show dave point at right
    with moveinright
    dave "Welcome to my visual novel, cool guy"
    call screen chest

label memories:
    call screen memories

label spy:
    hide screen memories
    "I remember that granny was a spy"

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
    hide dave point
    with dissolve
    show dave weird at right
    with dissolve

    if insult:
        "THE END, maybe you should have been nicer"
    else:
        "THE END, guess being nice didn't help"
