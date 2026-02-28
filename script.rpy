# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Sandy")
define c = Character("You", color="#c8ffc8")
define clownfish = Character("Clownfish", color="#c8c8ff")
define redclownfish = Character("Clownfish", color="#8D021F")
define turtle = Character("Turtle", color="#c8c8ff")
define s = Character("Statues", color="#c8c8ff")
transform darker:
    matrixcolor BrightnessMatrix(-0.2)
transform larger:
    zoom 1.5

init:
    image bg dark = "#000000"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg dark

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "At the very bottom of the ocean, in the darkest trench no sunlight has ever touched, a forgotten monster stirs."

    "Long ago, the Sea Guardians sealed it away in the deepest abyss."

    "But now, the seal is weakening, and its shadow is spreading upward through the layers of the ocean."

    scene bg beach

    show sandy

    m "Oh, it's a human! We've needed your help for so long!"

    c "What are you? What do you want from me?"

    m "I'm a mermaid, a guardian of the ocean. The world of the sea is falling into darkness, and only you can keep the monster from awakening!"

    c "What? What monster?"

    m "Long ago, the humans unleashed a sea monster on us to destory our kind."

    m "The ancestors managed to lock up the creature, but it has awoken again."

    m "It won't be long before it destroys us all. And because the humans were the first to create the creature, they must be the ones to destory it."

    c "How am I supposed to stop it?"

    m "We have to fight its shadow, and make our way down to the abyss until we reach its lair."

    c "I'm confused.."

    m "Just follow me, and we'll find a way to stop it!"

    "The mermaid says a spell that creates a bubble of air around you, allowing you to breathe underwater. You follow her into the ocean."

    scene bg first

    "As you swim deeper, the light fades and the water grows colder."

    show sandy with dissolve

    m "This is the first layer of the ocean. It's still pretty bright here, but it's getting darker as we go down."

    "Suddenly, you see two shadowy creatures near you, blocking your path."

    m "Those are the guardians of the first layer. They need to make sure you're fit to save us from the monster before they let you journey further."

    m "However, one of them is a servant of the monster, and will betray you to stop you from reaching the monster's lair. You have to choose which one to trust."
    
    jump asking

label asking:
    scene bg first
    show clownfish:
            xalign 0.75 yalign 0.1
            zoom 1.5
    show turtle:
        xalign 0.9 yalign 0.3
    menu:
        "Which guardian do you talk to?"
        "The giant clownfish":
            hide turtle
            "The clownfish swims in circles above you, examining you with its large eyes. Its body is massive and you can feel the wake it leaves pushing and pulling at you. It seems to be friendly, and it tells you that the other guardian is a servant of the monster."
            jump clownfish
                
        "The sea turtle":
            hide clownfish
            "The sea turtle seems to be reserved, and he doesn't say much as he looks at you. His shell is a mossy and weathered, and its eyes are a brilliant green as it watches you. It urges you to be careful, and tells you that this decision will determine the fate of your journey."
            jump turtle

label clownfish:
    menu:
        "What do you do?"
        "Ask, 'Why are you here in this part of the ocean?'":
            clownfish "I just stay where the current brings me. Lately, the currents have been shifting. It's... interesting to observe."
            jump clownfish

        "Ask, 'What's happening below us?'":
            clownfish "Stories grow darker the deeper you go. But stories aren't always true, you know. Sometimes fear creates its own monsters."
            jump clownfish

        "Ask, 'Should I keep going?'":
            clownfish "That depends. What do you want to fix? The ocean has survived worse than this. It will adapt."
            jump clownfish

        "Ask, 'If I trust you, what will you do?'":
            clownfish "I'll make sure you don't overreact. Panic causes more damage than the monster itself."
            jump clownfish
        
        "Choose to trust the clownfish and follow it to the next layer of the ocean":
            #clownfish scene
            c "I choose you. I trust you."
            scene bg dark with fade
            pause 3.0
            "The turtle's eyes narrow slightly, but it stays silent."
            redclownfish "I knew you would choose me."
            scene bg first at darker with fade
            show clownfish:
                xalign 0.75 yalign 0.7
                zoom 2.5
            "The effect is immediate. The current around you shifts, seemingly normal at first, but then it becomes stronger and violently tosses you around. Slowly, the color leaches from the clownfish's stripes, flowing like ink into the water."
            "The ground splits open underneath you and darkness flows out. The shadows pull you into the depths, never to return."
            "{b}Bad Ending{/b}"
            menu:
                "Try again":
                    jump asking
                "Quit":
                    return
        
        "Leave to talk to the other guardian":
            jump asking

label turtle:
    scene bg first
    show turtle
    menu:
        "What do you do?"
        "Ask, 'Why are you here in this part of the ocean?'":
            turtle "I travel between layers. When something changes, I can feel it. Something's changed, and I don't like it."
            jump turtle

        "Ask, 'What's happening below us?'":
            turtle "Something is stirring. It doesn't matter what you call it, but its influence is rising"
            jump turtle

        "Ask, 'Should I keep going?'":
            turtle "If you go, you must understand the risk. The deeper layers will test you in ways you can't imagine."
            jump turtle

        "Ask, 'If I trust you, what will you do?'":
            turtle "I will guide you to where you must go. But I cannot protect you from the dangers that lie ahead."
            jump turtle
        
        "Choose to trust the turtle and follow it to the next layer of the ocean":
            c "I choose you. I trust you."
            jump turtlepath
        
        "Leave to talk to the other guardian":
            jump asking

label turtlepath:
    scene bg dark with fade
    pause 3.0
    "Your journey starts to the next layer of the ocean, the turtle guiding you and Sandy following by your side. As you swim deeper, the turtle begins to talk to you."
    turtle "I've been waiting for you. The sea needs you right now more than ever. The monster is growing stronger, and I knew that one day, someone would come to stop it. I hope you can be that person."
    turtle "I know what you will have to face next. The journey through the second layer will be a an arduous one. The statues are known to be guardians of the deeper layers, and they make sure only the worthiest pass."
    turtle "After all, we mustn't allow traitors of the sea to get down there and awaken the monster."
    scene bg second with fade
    s "Who goes there? Who dares to enter the second layer of the ocean?"
    s "Only those who are worthy may pass. Do you think you are worthy? I see that you have come this far, and trusted the right guardian. But that doesn't mean you are worthy. You must prove yourself to me before I let you pass."
    c "I'll do whatever it takes to prove myself. I have to stop the monster, and nothing will stop me."
    s "Very well. I will ask you three questions. If you answer them correctly, I will let you pass. But if you answer them incorrectly, I will have no choice but to end your journey here."
    #first question
    menu:
        s """{b}The False Calm{/b}
            \n'I dance on the surface, But never go deep.
            \nI sparkle in sunlight,Yet vanish at night.
            \nI am loud from afar, But hollow within.
            \nWhat am I?'"""
        "Sea foam":
            s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
            menu:
                "Try again":
                    jump turtlepath
                "Quit":
                    return
        "Waves":
            s "Correct. You are wise, and you have passed the first test."
            #second question
            menu:
                s """{b}The Sea Beast{/b}
                    \n'I once ruled the surface, Now I serve the deep.
                    \nWood and iron bones In eternal sleep.
                    \nWhat am I?'"""
                "A shipwreck":
                    s "Correct. You have answered the second question correctly."
                    #third question
                    menu:
                        s """{b}The Hidden Giant{/b}
                            \n'I sleep beneath miles of blue, Longer than kingdoms live.
                            \nWhen I wake, The sea reshapes itself.
                            \nI am not the monster you seek, But I shake its prison walls.
                            \nWhat am I?'"""
                        "A kraken egg":
                            s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
                            menu:
                                "Try again":
                                    jump turtlepath
                                "Quit":
                                    return
                        "A deep-sea leviathan":
                            s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
                            menu:
                                "Try again":
                                    jump turtlepath
                                "Quit":
                                    return
                        "A volcano":
                            s "Correct. Your wisdom is evident. You may pass."
                            scene bg second with hpunch and vpunch
                            pause 1.5
                            "Suddenly, the floor beneath you shakes, and you feel the ground below you shift."
                            jump finalscene
                        "A drowned titan":
                            s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
                            "{b}Bad Ending{/b}"
                            menu:
                                "Try again":
                                    jump turtlepath
                                "Quit":
                                    return

                "A pirate's grave":
                    s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
                    menu:
                        "Try again":
                            jump turtlepath
                        "Quit":
                            return
                "A sea serpent's skeleton":
                    s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
                    "{b}Bad Ending{/b}"
                    menu:
                        "Try again":
                            jump turtlepath
                        "Quit":
                            return
                "A sunken city":
                    s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
                    "{b}Bad Ending{/b}"
                    menu:
                        "Try again":
                            jump turtlepath
                        "Quit":
                            return

        "A mirage":
            s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
            "{b}Bad Ending{/b}"
            menu:
                "Try again":
                    jump turtlepath
                "Quit":
                    return
        "Wind":
            s "No, that's not correct. I'm sorry, but you have failed the test. Your journey ends here."
            menu:
                "Try again":
                    jump turtlepath
                "Quit":
                    return

label finalscene:
    scene bg explosion with hpunch and vpunch
    pause 1.5
    scene bg third with fade
    show monster
    "this parts not done yet"
    
    # This ends the game.

    return
