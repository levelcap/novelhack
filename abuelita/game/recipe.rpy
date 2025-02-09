default recipe_tries = 0
default step = 0
default cooking_succes = False

default ingredients = {
  "masa": False,
  "agua": False,
  "mezcla": False,
}

label recipe:
    scene bg black
    with fade

    "This is the book where my abuelita wrote down all of her recipes for me."
    "(She, of course, never used a recipe herself)"
    "The first recipe is for corn tortillas. All it says on the page is “masa harina” and “agua” and “mezcla y tortea” and nothing else."

    scene bg kitchen
    with fade
    show cookbook at truecenter
    m "Can't hurt to try!"

    jump cooking_step

label cooking_step:
    if step == 0:
        "What should I do first?"
    elif step <= 2:
        "And then..."
    else:
        jump cooking_end

    $ step += 1

    menu:
        "Add the masa harina" if not ingredients["masa"]:
            $ ingredients["masa"] = True
            jump cooking_step

        "Add the agua" if not ingredients["agua"]:
            $ ingredients["agua"] = True
            jump cooking_step

        "Mezcla... y ... tortea" if not ingredients["mezcla"]:
            $ ingredients["mezcla"] = True
            jump cooking_step

label cooking_end:
    $ recipe_tries += 1
    if recipe_tries < 3:
        m "I do NOT remember abuelita's tortillas tasting like burnt ass..."
        $ ingredients["masa"] = False
        $ ingredients["agua"] = False
        $ ingredients["mezcla"] = False
        jump cooking_retry
    else:
        m "Yeees this is it! Crushed it!"
        m "I remember abuelita always telling me - you suck at cooking, just keep trying I guess"
        $ cooking_success = True
        jump end_recipe

label cooking_retry:
    menu:
        "Should I bother to try again?"

        "Yes, for abuelita!":
            $ step = 0
            jump cooking_step
        "No, I can't bear the shame of another failure":
            jump end_recipe

label end_recipe:
    "Wow I sure cooked"

    $ memory_counter += 1
    $ memory_states["recipe"] = True
    jump return_memories
