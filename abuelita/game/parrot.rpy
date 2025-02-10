
#define h = Character("Hector")
#define p = Character("Picasso")
#define dp = Character("Pepita")

label Parrot:

    scene bg birdcage

    "My grandma used to have a parrot named Picasso."
    "She would put his cage outside on the balcony above the door. "
    "My grandma never opened the door before asking who was there."
    "So when someone rang the doorbell Picaso would say “who is it” and just after the person responded, the bird would keep asking questions that he had heard before."
    "So every time somebody would ring the bell and my grandma couldn’t answer immediately I would hide close to the door and giggle at the scene."

    scene bg house outside

    show parrotright at right

    #play sound "audio/effect.ogg"

    p "Who is it?"

    show pepita at left
    hide parrotright

    dp "Hi! I am looking for doña Clotilde, is she available?"
    show parrotright at right
    hide pepita
    p "What do you want?"

    show pepita at left
    hide parrotright
    dp "I need to talk to her"
    show parrotright at right
    hide pepita
    p "Is it urgent?"
    show pepita at left
    hide parrotright
    dp "Not really, just coming by to say hi!"
    show parrotright at right
    hide pepita
    p "Hi!"
    show pepita at left
    hide parrotright
    dp "Hi!"
    show parrotright at right
    hide pepita
    p "Hi!"
    show pepita at left
    hide parrotright
    dp "Can I talk to doña Clotilde?"
    show parrotright at right
    hide pepita
    p "Who is it?"
    show pepita at left
    hide parrotright
    dp "I’m Doña Pepita, from down the street"
    show parrotright at right
    hide pepita
    p  "What do you want?"
    show pepita at left
    hide parrotright
    dp "I just want to say hi!"
    show parrotright at right
    hide pepita
    p "Hi!"
    show pepita at left
    hide parrotright
    dp "I think I’ll come back later"
    show parrotright at right
    hide pepita
    p  "Is it urgent?"
    show pepita at left
    hide parrotright
    dp"Not really, have a nice day!"
    show parrotright at right
    hide pepita
    p "Have a nice day! A nice day!" 


    #play sound "audio/parrot effect.ogg"

    

     


    