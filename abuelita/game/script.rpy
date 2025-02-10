# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Abuelita", color='#ff5100')
define m = Character("Me", color='#006aff')
define ym = Character("Me (Younger)", color='#006aff')


#Highschool characters
define sophie_chou = Character("Sophie Chou")
define billy_ray = Character("Billy Ray")
define montgomery = Character("Montgomery")
define mrs_fairchild = Character("Mrs Fairchild")



# Memory states
default memory_states = {
  "spy": False,
  "bicycle": False,
  "recipe": False,
  "highschool": False,
}
default memory_counter = 0

# The game starts here.

label start:
    jump memories
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
    with hpunch
    call screen memories

label return_memories:
    scene bg trunk open
    with fade

    "Ah good memories. anyway..."

    if memory_counter >= 4:
      "That's everything in the trunk"
      jump happy_end

    call screen memories

label do_nothing:
    "I'll deal with this later."

    scene bg house outside
    with fade

    "Sometimes not playing the game is a way of winning, probably."

    "The End."

    return

label happy_end:
    scene bg house outside
    with fade

    "I remembered some good memories today"
    "The End."

    return
