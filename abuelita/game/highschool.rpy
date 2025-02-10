default with_sophie = False



label highschool_start:
    scene campus
    show fairchild
    mrs_fairchild "Alright kids, we made it to Harrington High School. This place is positively Sybaritic (S-Y-B-A-R-I-T-I-C)."

    "But we didn’t come here to marvel, we are here to get our club’s first ever regional title."

    "We have 1 hour before the contest starts, so go make new friends and remember to be respectful."

    "(Pointing at you) Hector, don’t get distracted on the campus."

    "Billy Ray, please make an effort and review your word list, you don’t want to be the reason we lose."

    "Sophie, make sure all the boys are in the auditorium in 1 hour sharp."

    menu:
        "Speak to Sophie Chou":
            jump SC1
        "Speak to Billy Ray":
            jump BR1
        "Go mingle with the Harrington High group":
            jump H1
        "Go find your family in the auditorium":
            jump F1
        "Visit the halls of the high-school":
            jump H1

label F1:

    scene auditorium with fade


    "Hector enters the grand auditorium, scanning the crowd."

    # Grandma waves the camera
    show sb_abuelita at left with dissolve
    "Abuelita waves a camera in the air, beaming at him. She rushes over and pulls him into a warm hug."

    a "How do you feel, mijo?"
    "She grins, squeezing his shoulders."
    a "You'll do great! I have faith in you."

    a "(Leaning in slightly, lowering her voice, and winking) But if you need a little help… just say the word."

    menu:
        "Oh for sure Abuela, we'll need all the help we can get. All I need is for you to google the words on your iPad and cough if they contain an 'H'.":
            show sb_abuelita_laughing at left with dissolve
            a "Oh my little bandidos!"
        "Ah ah no worries grandma, we don't need any help to beat these morons.":
            a "I am so proud of you, mijo!"

    a "Ah, my Hectorito. Stay with me for a bit. I brought you your favorite tamarocas."

    "It was a great day. Hector had a good time with his grandma and wasn’t even stressed when the championship started."

    "His team didn’t win, but looking back, it wasn’t important at all."

    $ memory_counter += 1
    $ memory_states["highschool"] = True
    jump hs_return_memories


label SC1:
    scene campus
    show sophie_chou
    sophie_chou "Hi Hector, best of luck for the contest!"

    sophie_chou "I hope we win, it would look really good on my university applications and would be perfectly cromulent (C-R-O-M-U-L-E-N-T)."

    menu:
        "That Billy Ray is really hurting our team’s chance, what can we do to get rid of him?":
            jump SC2
        "I’ll go see what the Harrington high spelling bee club is up to. Wanna come with me? I might need help beating them up ah ah.":
            $ with_sophie = True
            jump H1
        "Wanna sneak into the high school corridors with me? We could steal a golden pen or two":
            $ with_sophie = True
            jump H1
        "Wanna go talk to Billy Ray?":
            jump BR1

label SC2:
    scene campus
    show sophie_chou_frowning
    sophie_chou "How dare you say something like this! So very solipsistic of you (S-O-L-I-P-S-I-S-T-I-C)."

    sophie_chou "Billy Ray is our team-mate and we’re all in this together."

    show sophie_chou
    sophie_chou "That is, unless he got locked in a room, or got food poisoning, or would run into trouble in a way that doesn’t penalize the team."

    menu:
        "Wanna go talk to Billy Ray?":
            jump BR1
        "Fine. Let’s go see what the Harrington High spelling bee club is up to.":
            jump H1
        "Wanna sneak into the high school corridors with me? We could steal a golden pen or two":
            jump H1

label BR1:
    scene campus
    show billy_ray
    billy_ray "Wassup, loser!"

    billy_ray "There’s no way I’m studying my word list today. If my dad hadn’t paid for the team’s travel expenses and forced Mrs Fairchild to take me in the team, I’d be playing with my Switch right now."

    billy_ray "This place is sumptuous (S-O-M-T-U-O-S) though. I’m sure there is some good stuff to steal in these corridors."

    menu:
        "I’ll go check the corridors, will let you know if I find something":
            jump H1
        "You do you, Billy Ray. I’m going to talk to the Harrington High team":
            jump H1
        "Er, I’ll talk to Sophie":
            jump SC1

label H1:
    scene hallway
    "The high school is even more luxurious inside, with its golden lockers, marble archways, satin curtains."

    "Entering the hallway, Hector spots the Harrington Spelling Bee team: five boys, looking at a piece of paper, and whispering to each other in a small circle."

    "When they see you, their captain folds the paper, puts it in his uniform jacket. The group disperses, and the captain comes towards you."

    show montgomery
    montgomery "What are you doing here, peon (P-E-O-N). Are you lost?"

    menu:
        "What’s the paper, are you guys cheating?":
            jump H2
        "We are here to evacuate the building, there has been a moron alert.":
            jump H2
        "Wow is that jacket made of silk, I think my abuela has the same.":
            jump H2

label H2:
    scene hallway
    show montgomery
    montgomery "Whatever, peasant. Be on your way before I call the security."

    menu:
        "Punch him in the face.":
            if with_sophie:
                jump H4
            else:
                jump H3
        "Run towards the corridor in the back":
            jump MR1
        "Retreat to the auditorium":
            jump F1

label H3:
    scene hallway
    show montgomery
    montgomery "What are you even trying to do, midget (M-I-D-G-E-T)."
    "You realize that, if you are to fight Montgomery, you’ll need a friend."

    menu:
        "Go talk to Sophie Chou":
            jump SC1
        "Run towards the corridor in the back":
            jump MR1
        "Retreat to the auditorium":
            jump F1

label H4:
    "Hector and Sophie punch that idiot Montgomery Ashford Wintrhope IV and it is cathartic (C-A-T-H-A-R-T-I-C)."

    "He leaves the room, screaming 'now I am really calling security, and Father will hear of this. You are done for!'."

    "You realize that the paper he had folded into his jacket fell to the ground."

    "Opening it, it reads: Spelling Bee contest - official words that will be asked to the candidates."

    "THIS LOOKS LIKE CHEATING!How did the Harrington team get hold of that paper??"

    menu:
        "Go warn Mrs Fairchild":
            jump FR1
        "Go to the end of the corridor":
            jump MR1

label MR1:
    scene hallway
    "You run aimlessly through the building, each corridor more scrumptious than the next."

    scene cctv_room
    "After a few minutes, as you catch your breath, a dark room catches your attention."

    "In that room stand many monitors and microphones, the monitors show live footage from within the auditorium, from cameras positioned as to see the spelling bee judges’ notes!"

    "You realize this room is probably USED FOR CHEATING."

    menu:
        "Break everything in the room":
            jump MR2

        "Go tell Ms Fairchild about the cheating":
            jump FR1

label MR2:
    scene cctv_room_on_fire
    "You kick the monitors, rip the cables, slam the microphones on the ground."

    "$300,000 in damages later, you believe you have achieved sufficient destruction."

    "Time to go see your abuelita! She must be wondering what you've been up to."

    menu:
        "Go back to see your abuelita":
            jump F1
        "Go warn Mrs Fairchild first":
            jump FR1


label FR1:
    scene auditorium
    show fairchild
    mrs_fairchild "Ah, finally. I was wondering where you were hiding."

    menu:
        "Ms Fairchild, Harrington High is cheating! We have proof!":
            show fairchild_sad
            mrs_fairchild "I know, Hector. Everyone knows."

            mrs_fairchild "But Harrington High is so rich, and their bribes are so generous..."

            "(she looks at her Rolex)"

            show fairchild_sad

            mrs_fairchild "Ok, time say hi to your Abuelita before the contest starts."
            jump F1
        "Ok, whatever Mrs Fairchild, I’ll go see my abuela":
            jump F1

label hs_return_memories:
    scene bg trunk open
    with fade

    "Ah good memories. anyway..."

    if memory_counter >= 3:
      "That's everything in the trunk"
      jump happy_end

    call screen memories
