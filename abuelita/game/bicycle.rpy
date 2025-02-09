default training_wheels = True

label bicycle:
    scene bg black
    with fade

    "I spent most weekends with my Abuelita."

    """
    She'd been working with me on how to ride a bike and telling me stories
    about how she used to ride her bike to work and what she did there.
    """

    scene bg placeholder
    with fade

    a "Are you certain you want to take the training wheels off Hector?"

menu:
    "Take them off!":
        jump remove_wheels

    "Keep them on!":
        jump keep_wheels

label remove_wheels:
    $ training_wheels = False

    ym "Yes Grandma! All the other kids stopped using training wheels ages ago!"

    "Hector lets his abuelita remove the second training wheel with reluctance."
    "She puts it to the side and holds the bike up for him."
    "He takes the bike gingerly trying to make sure it stays balanced and swings his leg over the side. He puts his butt on the seat and promptly falls over."

    jump end_bike_ride

label keep_wheels:
    ym "No Grandma! Want to watch how fast I can go?"

    "Hector gets on the bike and dashes off around the block while his abuelita watches."
    "Hector returns, breathing hard, elated with his speed."

    jump end_bike_ride

label end_bike_ride:
    a "Good job Hector! You're going at your own speed. Did I ever tell you about the time I had to get a message to my father in the next town over when I was your age?"

    "Hector shakes his head."

    if training_wheels:
        "He stays on the bike and waits for his abuelita to say something."
    else:
        "He dries his tears and picks up his the bike, listening"

    a "Well, when I was your age, we were about to celebrate my brother’s birthday"
    a "It was going to be a surprise party, because he’d insisted he didn’t want to celebrate."
    a "He was a very serious boy, and thought any birthday that wasn’t a round number wasn’t worth celebrating."
    a "We all decided we wanted a party, and so my father took my brother out to town while we decorated the house and made a huge feast."
    a "My father was supposed to come home with my brother around the time the food was ready. He and my brother didn’t show."
    a "Since I was the youngest and my part had been done. I was told to go into town. So I hopped on my bike and pedaled as fast as I could."
    a "When I got to town, there was a parade going on."

menu:
    "Abuelita joins the parade":
        jump parade

    "Abuelita finds her dad and her brother and goes home":
        jump goes_home

label parade:
    a "There were so many people, and some of my friends saw me on my bike."
    a "They called me over and it turned out they were a part of the parade. I ended up at the front!"
    return

label goes_home:
    a "There were so many people! I didn’t want to lose my bike, but I also couldn’t get around everyone with it"
    a "so I quickly found a place near the supermarket and left it there. Then, trying to see above lots of people when you’re only so tall is hard."
    a "There was a tree that hung over Main Street that my friends and I liked to climb. I climbed up it."
    a "I spotted my father and brother trying to move against the crowd of parade goers. I waved at them so hard I nearly fell out of the tree!"
    a "Eventually they saw me and we all went home."

    return
