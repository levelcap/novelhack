label spy:
    "Whoa why is this old shoebox filled with spy stuff? I found:"
    "Documents"
    "Several different passports"
    "Binoculars"
    "Sunglasses"
    "A small book of codenames"
    "..."
    m "I remember grandma getting strange calls sometimes..."

    jump spy_memory_start

label spy_memory_start:
    scene bg black
    with fade

    scene bg spy living room
    with fade

    show landline phone at truecenter
    with moveintop

    "The phone rings three times and then stops - Hector knew better than to pick up before it rang thrice."
    "Abuelita was quite strict, almost superstitious about that."
    "The phone rings 2 times and stops"
    "The phone rings again and after the third ring, Abuelita picks it up"

    show grandma spy at left
    with dissolve
    a "Hello? Yes, the eggplants are ready, we had a plentiful harvest this year."
    "Hector looks puzzled —Abuelita doesn’t even grow eggplants, he knows she doesn’t even like them!"
    a "What do you mean you won’t need them anymore? THE PURVEYOR RETIRED???!!!!"
    a "Surely the dealer won’t let this fall through… SHE RETIRED TOO????"

    menu:
        "Interrupt Abuelita about the eggplant discrepancy??"

        "Yes, its very important!":
            jump spy_interrupt

        "Maybe leave it alone for now...":
            jump spy_no_interrupt

label spy_interrupt:
    show hector young smile at right
    with dissolve

    ym "But we don’t even have eggplants!"
    a "Kid! Shut up! Go away!"

label spy_no_interrupt:
    a "Oh… no, not them… (silent tears slowly roll down her cheeks)"

label spy_next:
    hide landline phone
    show hector young cry at right
    with dissolve

    "Sometimes, Abuelita would suddenly cancel family plans after a phone call. Hector would often be upset about this."
    "He remembered that one time he decided to hide in her closet to jump on her and beg her not to leave"
    "Hector peeks through the closet slats waiting for Abuelita to come into the room to do whatever she did after her weird phone calls before leaving the house"
    "Abuelita enters the room hurriedly and..."

    jump end_spy

label end_spy:
    $ memory_counter += 1
    $ memory_states["spy"] = True

    jump return_memories
