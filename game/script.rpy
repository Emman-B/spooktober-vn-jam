﻿#Credits:
#https://lemmasoft.renai.us/forums/viewtopic.php?t=26544
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#mc input name
define mc = Character("[mcname]") # purple
define il = Character("Ilse") # beekeeper
define el = Character("Elodie") # blue
define va = Character("Vance") # red
define g = Character("Ghost")
##configure fonts ##
#name: Nova Slim
#text: Inconsolata
#maze: Inconsolata
#hangman: Lacquer
init python:
    DEBUG_start_menu_testing = False # Set to true to enable the debug menu at the start
    config.preload_fonts = ['NovaSlim-Regular.ttf','PoorStory-Regular.ttf','Lacquer-Regular.ttf','Inconsolata-Regular.ttf']
    
# The game starts here.

##MUSIC##
define audio.mazebgm = "./music/panik@theHouseonYYYYstreet.wav"
define audio.mainbgm = "./music/Ringin_eaR_ost_ver.wav"
define audio.enteringHouse = "./music/Ringin_eaR.wav"
define audio.setupbgm = "./music/Ghost_techies.wav"
#########

##SFX##
define audio.electronicAmbience = "./sfx/ambience.wav"
define audio.heavyBreathSlow = "./sfx/breathing_slow.wav"
define audio.heavyBreathFast = "./sfx/breathing.wav"
define audio.buzzWrong = "./sfx/buzz_wrong.wav"
define audio.camera01 = "./sfx/camera_click.wav"
define audio.cameraMultiple = "./sfx/camera_multiple_slow.wav"
define audio.cameraMultiple02 = "./sfx/camera_multiple.wav"
define audio.clickDouble = "./sfx/click_double.wav"
define audio.clickSingle = "./sfx/click_single.wav"
define audio.correct ="./sfx/correctans.wav"
define audio.creak_long ="./sfx/creaking_long.wav"
define audio.creak_short ="./sfx/creaking_short.wav"
define audio.doorSlamClick = "./sfx/door_click.wav"
define audio.doorSlam = "./sfx/door_close.wav"
define audio.glassShatter = "./sfx/glass_shatter.wav"
define audio.runningLoud = "./sfx/running_closer.wav"
define audio.runningLight = "./sfx/running.wav"
define audio.rustling = "./sfx/rustling.wav"
define audio.saltScatter = "./sfx/salt.wav"
define audio.radioStatic = "./sfx/static.wav"
define audio.vacuum = "./sfx/vacuum.wav"
define audio.footsteps = "./sfx/walking.wav"
define audio.vroom = "./sfx/wind_ambience.wav"
#######

##Image Character Sprites##
image bp sad = "./images/bp_rock_d.png"

image ghost mad = "./images/ghost_mad.png"
image ghost neutral = "./images/ghost_neutral.png"

image elodie neutral = "./images/elodie_neutral.png"
image elodie happy = "./images/elodie_happy.png"
image elodie scared = "./images/elodie_scared.png"
image elodie smug = "./images/elodie_smug.png"
image vance neutral = "./images/vance_neutral.png"
image vance scared = "./images/vance_scared.png"
image vance happy = "./images/vance_happy.png"

image ilse happy = "./images/ilse_happy.png"
image ilse mad = "./images/ilse_mad.png"
image ilse neutral = "./images/ilse_neutral.png"
image ilse scared = "./images/ilse_scared.png"
image ilse shocked = "./images/ilse_shocked.png"

image mc happy = "./images/mc_happy.png"
image mc neutral = "./images/mc_neutral.png"
image mc scared = "./images/mc_scared.png"

##Image Backgrounds##
image bg dorm night = "./images/A01-3_HomeBase_DormRoom_Night.png"
image bg dorm day = "./images/A01-3_HomeBase_DormRoom_daytime.png"
image bg dorm evening = "./images/A01-3_HomeBase_DormRoom_Evening.png"
image bg bathroom day = "./images/Bath_house_test_daytime_v3.png"
image bg bathroom dusk = "./images/Bath_house_test_dusk_v2.png"
image bg bathroom night = "./images/Bath_house_test_night1_v2.png"
image bg bathroomGhostOrb night = "./images/Bath_house_test_night2_v2.png"
image bg outsideHouse = "./images/outside_house.png"
image bg livingRoom = "./images/A01-3_HomeBase_DormRoom_Night.png"
image bg study = "./images/study.png"
image bg diningRoom = "./images/living_room.png"
image bg door = "./images/door.png"
image bg hallway = "./images/hallway.png"
image bg bedroom1 = "./images/bedroom_1.png"
image bg bedroom2 = "./images/bedroom_2.png"



###########################

##custom x coord for sprites##
transform middle:
    xalign 0.5
transform left:
    xalign 0.2
transform right:
    xalign 0.8
###############################

label DEBUG_start_menu:
    menu:
        "You're in the debug menu! Choose where you want to be sent."

        "Ghost-chase scene":
            call begin_chase_room
        
        "Debug hangman game":
            call hangman

        "Exit debug menu":
            return

label start:
    scene bg dorm night with fade

    python:
        mcname = renpy.input("Your name?", length=32)
        mcname = mcname.strip()
        if not mcname: 
            mcname = "Emm Cee"
    mc "The name is [mc]."
    
    if DEBUG_start_menu_testing:
        call DEBUG_start_menu

    jump ch01

    return

label ch01:
    scene black
    play sound vroom fadein 0.1 volume 1.0
    "\"Your destination is on the right.\""
    
    "While the monotone voice of the GPS barely catches my attention, the car rolling into a slow stop
    makes me look up and out the van's wide window."

    "Squinting through the darkness of night, I can make out an average sized townhouse."
    stop sound fadeout 0.3
    "The client had said it wasn't an old or decrepit house, and yet looking at it now,"
    "I can see chipped paint and a boarded up window. Sure it's not old, but it's definitely damaged."
    play sound doorSlam 
    play music electronicAmbience
    "The client, a rather skittish lawyer, insisted on our services. Supposedly, they're having trouble
    transferring the property's ownership to new hands."
    stop sound 
    "The new owner-to-be finds the house eerie and disturbing, so uncomfortable they might refuse to inherit it."
    
    "Both the lawyer and the owner-to-be believe these uncomfortable feelings originate from a
    supernatural source."
    
    "There were unknown messes littering the ground, furniture moved to positions they weren't supposed to be in," 
    "appliances broken when they were working the last time they were touched."

    "Both attributed these mysteries to the presence of a ghost."

    "That's where we come in."

    "I'm a member of a team of ghost hunters, hired to eliminate threats from the afterlife."

    "It's not the most dignified occupation, but I applied hoping to satisfy my need for adventure."

    "As the newest member of the team, I can only hope that I meet everyone's expectations."

    "After all, this is a team of professionals I'm joining."
    stop music fadeout 0.3
    jump ch02

label ch02:
    play music setupbgm loop volume 0.4
    scene bg outsideHouse

    "\"Out!\""
    
    "As per our team leader's orders, I scramble out of the van. They're already standing
    outside, waiting, signature hat secured on their head." 

    show ilse neutral at left
    ""
    show ilse neutral at right with easeinleft 
    show mc neutral at left
    mc "Yes, boss!" 
    hide mc neutral at left
    "Boss" "No need to call me boss. Just Ilse is fine."
    "That's the boss for you; reliable and friendly. They know everything there is to
    know about ghost hunting. I'm sure I'll learn a lot from watching them."
    il "I'm opening the trunk. Get your things."
    "My things? Uh..."
    
    "While Ilse grabs the Ghyson Vac-Pack and secures it onto their back, 
    I look at the heaping pile of objects nearly spilling out of the open trunk."
    hide ilse neutral at right
    "Not only are all the ghost hunting gadgets dumped in this pile, 
    but a good portion of it is made of snacks."
    
    "I have no doubt that the snacks were packed by Elodie."
    
    "Speaking of, Elodie finally slinks out of the car."
    show elodie neutral at left
    el "What am I supposed to bring again?"
    hide elodie neutral at left
    "Even as she asks, she doesn't look up from her phone screen."
    show ilse neutral at left
    il "Here. You can watch over the EMF meter this time."
    hide ilse neutral at left
    show elodie neutral at left
    el "Right. The enterprise media functions."
    hide elodie neutral at left
    "The what now?"
    show mc neutral at left
    mc "Do you mean the-"
    hide mc neutral at left
    show elodie happy at left 
    el "Sorry, sorry. I was watching a video. I meant the Ecto-Mode Finder!"
    hide elodie happy at left
    show mc neutral at left
    mc "Huh? I thought it was the electromag-"
    hide mc neutral at left
    show elodie neutral at right with easeinleft
    el "Eggs, muffins, frittata!"
    "Elodie rushes past me to the pile of everything and grabs her snacks, stuffing whatever fits into her pockets."
    "She must've had food on her mind."

    el "This job is cutting into my dinner time, you know?"

    el "Let's get in, clean the place, prove nothing spooky's up, and get out."
    hide elodie neutral at right
    show mc neutral at left

    mc "Huh? Is it likely for it to end up being nothing? The client seemed pretty scared of going back to the house."

    mc "It doesn't look like the usual haunted house, but there must be something paranormal going on if we were called in, right?"

    hide mc neutral at left 
    show ilse neutral at left
    
    il "It's possible. There are false alarms once in a while."
    
    il "But whether there is or isn't a ghost, we'll still at least check thoroughly like we were hired to."
    
    show ilse happy at left
    
    il "However, I do believe there's something. The signs the client reported are pretty convincing."
   
    show ilse neutral at right with easeoutright
    
    "As expected of the boss! Their confidence is a steady presence that bolsters my own courage."

    hide ilse
    
    play sound clickDouble volume 0.9

    "I quickly find my heavy-duty flashlight and video camera. Luckily, neither were damaged during the drive." 

    "With the video cam, I'll be able to record my first job for prosperity!"
    
    "And maybe if I'm lucky, I can get a glimpse of the ghost!"

    "In my excitement, I nearly miss that only three of our four member team are present."
    show mc neutral at left
    mc "Where's Vance?"

    "\"Shh, not so loud!\"" # vance

    "I look around."
    hide mc neutral at left 
    
    $ looking_for_vance_left = False
    $ looking_for_vance_right = False

    label looking_for_vance_section:
        menu:
            "Look left" if not looking_for_vance_left:
                $ looking_for_vance_left = True
                "I looked over to my left. Nothing."
                jump looking_for_vance_section
            "Look right" if not looking_for_vance_right:
                $ looking_for_vance_right = True
                "I looked over to my right. Nothing."
                jump looking_for_vance_section
        
    "I peer around the car but I can't see the source of the voice."

    "... Wait, it can't be... can it?"

    "I look in the one place I haven't yet: back inside the car."

    "There he is, the last member of our team."
    
    hide mc neutral at left
    show vance neutral at left
    # Enter Vance

    "Vance is stiff, still sitting in his seat."

    va "If Ilse forgets about me, I won't need to go in."
    
    hide vance neutral at left
    show mc neutral at left
   
    mc "What, why not? Isn't this exciting?"
   
    hide mc neutral at left
    show vance neutral at left
    
    va "More like the complete opposite! What's fun about sacrificing ourselves to the demons inside that house?!"
    
    show vance neutral at right with easeoutright
    
    # Enter Ilse
    show ilse neutral at left
    
    il "There you are, Vance. It's time to go."
    
    va "No. Please, don't make me go in there."

    il "It'll be over soon."

    va "Nooooo!"

    # Exit Ilse, Vance
    hide vance neutral
    hide ilse neutral
    
    "Well, that's everyone."
    stop music fadeout 0.2
label ch03:

    show ilse neutral at left
    show ilse neutral at right with easeinright
    il "Everyone ready?"
    hide ilse neutral at right
    show vance scared at left
    show vance scared at middle with easeinleft
        
    va "No! Can I leave? Three is more than enough people."
    show elodie smug at left 
    el "Calm down, Vance. It's just an old house."
    show vance scared at right 
    va "Just?! Say that again when you're six feet under!" with vpunch

    menu:
        "Yes, boss!":
            hide vance scared
            show ilse neutral at right with easeinleft
            il "Alright. Looks like we're at a consensus. Let's begin."

            "Ilse turns the handle. Unlocked."
            play sound doorSlamClick
        
            "Ooh, things are already spooky."
            
            hide elodie neutral
            hide ilse neutral
            
            "Elodie follows the boss, dragging Vance along forcefully. I close in behind the group, dutifully filming everything."
            
        "Maybe Vance has a point.":
            
            show elodie neutral at left 
            el "Aw, not you, too! C'mon, it'll be a quick in and out job."
            hide elodie neutral
            hide vance neutral
            show ilse neutral at right 
            il "This is your chance to get more experience. It's not as scary as Vance makes it out to be."
            hide ilse neutral 
            show mc neutral at left 
            mc "That's true… I suppose I should be brave about it."

            "They're right. I can't psych myself out before I've even started."
            hide mc neutral 
            "Ilse opens the front door, and as the others start filing in, I take a deep calming breath."
    
    scene bg door with dissolve 
    "The open doorway looms over me menacingly, as if it's trying to scare me away and dare me to enter at the same time."
    "A scuffed old doormat lies in front of it."

    "{i}Wel{/i}, it reads. The rest has faded away."
    show mc neutral at left 
    "Well. Then I'll come in."
    hide mc neutral 

    menu:
        "Wipe my feet on the mat before entering.":
            pass
        "Enter without wiping my feet on the mat":
            pass
    play music enteringHouse volume 0.6
    scene bg livingRoom with dissolve 
    "The moment I step past the threshold, I feel an immediate chill wash over me and shiver. The others don't seem
    to be affected in the same way."
    show vance neutral at middle 
    "Well, except for Vance, but he was already shivering in fright before entering the house."
    "But he isn't any more frightened than before. Is this what it means to be a professional?"
    hide vance neutral at middle 
    "The entranceway is connected to the living room. "
    "The place isn't empty; there's still some furniture left over from the previous tenant."

    "A visible layer of dust coats everything, so thick our footsteps could probably kick clumps of it into the air."
    show elodie neutral at right 
    "Elodie waves her EMF meter in a wide arc over her head. "
    "It creates a lagging streak of green across the screen of the camera."
    show elodie happy at right 
    el "This room's clear!"
    hide elodie happy 
    "What? Bull!" 
    
    "That should only check Elodie's immediate vicinity, not the whole room. Unless...?"

    "It's possible that the company's tech R&D team upgraded the EMF to cover a wider area, isn't it?" 
    "That amazing tech just hasn't reached my newly employed hands."

    show vance scared at right
    va "T-The lights...They're not working!" with vpunch 

    va "Have the ghosts already short circuited the electricity? I thought the client said the appliances worked!"
    
    show ilse shocked at middle with ease 
    il "Actually, the client said the appliances didn't work."
    
    va "But they're supposed to!"

    show elodie neutral at left with ease
    el "No worries. They probably just stopped the electricity service while no one's living here."
    el "That's how you save on bills."
    show vance neutral 
    show ilse neutral 
    il "It's fine. We all have flashlights for a reason. Are we all done with this room?"
    
    "Everyone nods."
    
    show ilse happy
    il "Alright, gang. Let's split up."
    hide ilse happy with dissolve
    hide vance neutral with dissolve 
    hide elodie neutral with dissolve 
    show mc neutral at left with ease 
    mc "I thought the first rule of horror movies was to not split up."
    
    show vance scared at right
    hide mc neutral 
    va "I agree! How about we don't?" with vpunch 
    hide vance scared 
    show elodie neutral at left
    el "But that'll take more time. Didn't you want to get out of here fast? I know I do."
    hide elodie neutral 
    show ilse neutral at middle 
    il "We're professionals. We know what we're doing."
    show ilse happy 
    il "Then again, it is your first job. How about this?"
    show ilse shocked 
    il "According to the floorplan that was given to us, there are three other rooms downstairs." 
    show ilse neutral 
    il "We'll split up and cover one room each on the ground floor."

    il "After that, we'll all go upstairs and divvy up the area again." 
    il  "That way, we can stick close... {w}ish."
    hide ilse neutral with dissolve 

    # TODO: Update the dialogue where you are one-and-one with another character
    menu:
        "Where do you want to go?"

        "Study with Ilse":
            call study_ilse

        "Bathroom with Vance":
            call bathroom_vance

        "Dining Room with Elodie":
            call diningroom_elodie
    
    jump ch04

label study_ilse:
    show ilse happy at middle 
    il "With me? Then let's go. I'll teach you everything you need to know."

    scene bg study with dissolve 
    hide ilse happy 
    "We shuffle into the study and immediately see the mess the client mentioned."

    "Unlike the somewhat sparse living room, the study almost looks like someone could've been
    living here until recently, if that person was raving mad."

    "Papers, books, and a dented electric kettle of all things lie on the ground. Glass and
    ceramic shards are also scattered across the floor."
    
    show mc neutral at left 
    mc "Was this caused by the ghost?"
    
    hide mc neutral at left 
    show ilse neutral at middle 
    il "It's likely, considering our client wants this house habitable. There's no one else who
    would want to cause a mess."
    
    
    il "Some say ghosts move objects in an attempt to communicate. "
    il "But the ghosts' efforts usually end up useless, because once people realize they're there, people like us
    are hired to eliminate them."
    
    hide ilse neutral
    show mc neutral at left 
    mc "Should we be trying to communicate with the ghost, then? Try to find out what it wants?"
    
    show ilse mad at middle 
    il "While that sounds interesting, that's not our job. For what reason should we cater
    to the desires of the dead?"

    "They flip on the switch of their Vac-Pack. If they say anything else, I can't hear
    it over the sound of the Ghyson."
    play sound clickSingle 
    play sound vacuum volume 0.5 loop
    "They direct the vacuum head over the dangerous shards.
    With a faint clinking noise, the fragments are all sucked into the machine."
    
    show ilse neutral at middle 
    il "There! Now the ground is clear for us to work with."
    
    "I shove the rest of the objects to the side of the room while Ilse rummages through their
    deep pockets. "
    "What could they be looking for?"

    play sound glassShatter volume 0.2
    play sound rustling volume 0.2
    
    show ilse shocked at middle 
    il "Ah ha!" with vpunch 
    
    il "Salt! Listen here. Ghosts are scared of salt. It's got a history of purifying properties."

    show ilse happy at middle 
    il "With this, we can protect ourselves, maybe even hurt the ghost. Like so!"
    
    "They take the carton and pour the salt out, forming a ring of it. They step inside the circle."
    play sound saltScatter volume 0.5
    show ilse neutral 
    il "Ta dah!"
    
    show mc happy at left 
    "Choosing to follow Ilse was the right choice. I'm picking up so many tricks!"
    show mc neutral at left 
    mc "Now what?"
    hide mc neutral at left 

    show ilse neutral at middle 
    il "...Well, if the ghost were trying to hurt us, then theoretically, we'd be safe
    inside the circle."
    
    "Unfortunately, the circle isn't actually big enough for two people to stand inside.
    Fortunately, the ghost isn't here at the moment."
    
    "Ilse beckons me closer."

    il "Hold out your hands."
    show mc neutral at left 
    "I do the best I can while holding onto a video camera and a flashlight.
    They pour the salt into my awkwardly cupped hands."
    hide mc neutral 
    il "Now toss it around the room. Sprinkle it."
    show ilse shocked 
    il "...{w}Hmm, nothing at all. If there were a ghost, it would probably react."
    show mc happy at left 
    mc "It's a good thing there isn't."
    show ilse neutral at middle 
    il "Why is that?"
    show mc neutral at left 
    mc "Because your salt circle. The wind's already blown it away."
    show ilse shocked at middle 
    il "The wind? But the doors and windows are all closed."
    show ilse scared at middle 
    show mc scared at left 
    "Ilse and I exchange glances. We wordlessly agree that it's time to regroup."
    hide ilse scared 
    hide mc scared 

    return

label bathroom_vance:
    show vance happy 
    va "Yes! Thank god I don't have to go alone."

    scene bg bathroom night
    hide vance happy 
    "The two of us crowd into the bathroom. There's nothing out of the ordinary that I can catch."
    show mc neutral at left with ease 
    mc "Do you see anything?"
    hide mc neutral 
    show vance scared with vpunch 
    va "Aah!"
    hide vance scared 
    show mc scared at left with vpunch 
    mc "Ah!"
    hide mc scared at left 
    "Our shouts echo off the bathroom's tile floor."

    show vance neutral at right
    va "Don't startle me like that! Please."
    show mc scared at left 
    mc "Sorry, I didn't mean to."
    
    mc "So what did you bring to help us find the ghost?"
    show vance scared at right
    va "I don't want to find the ghost. In fact, I hope there is no ghost!"
    show mc neutral at left 
    mc "What? Why not? The whole point of this job is to locate the ghost, isn't it?"
    show vance neutral at right 
    va "It pays, [mcname], it pays."
    show mc happy at left 
    "Ah, yes. Money speaks. I guess that's another valid reason for people to apply for this job."
    "Not everyone is searching for the thrill of adrenaline like me."
    show mc neutral at left 
    mc "We won't get paid if we don't find the ghost."
    show vance neutral at right 
    va "Correction: We don't get paid if there is a g-ghost and we don't find it.
    If we tell them there wasn't a ghost in the first place, on the other hand..."
    
    mc "You mean lying?"
    show vance scared at right 
    va "No, of course not! This here—"
    
    "He waves the device in his hands around so frantically I can't tell what he's holding.
    I can just make out an antenna sticking out of it."
    show vance neutral at right 
    va "—is a ghost phone. We can use it to talk to the ghost by changing frequencies."
    va "And since the ghost isn't saying anything, then it must not be here!"
    show mc neutral at left 
    mc "Well, have you tried talking to it?"
    
    va "W-Why would I do that?!"
    show mc happy at left 
    mc "{i}ahem{/i} Hello? Is anyone here?"
    
    show vance neutral at right 
    #hide mc neutral at left 
    va "Shh!"
    #hide vance neutral at right 
    show mc happy at left 
    mc "If someone is in this room with us, can you give us a sign?"
    #hide mc happy 
    show vance scared 
    va "Shhhhhh!"
    hide vance scared 
    show mc neutral at left 
    mc "I don't think this frequency is working. Try another?"
    hide mc neutral 
    play sound radioStatic 
    "\" - -s-six - - oint - - - thre - fff - -\""
    show vance scared at right 
    va "WAAAAUUGGHH!!!" with vpunch 
    show mc scared at left 
    mc "UUWAAAH!!" with vpunch 

    "It talked back!"

    mc "You heard that, too, right? A ghost! A real live ghost!"
    show vance scared
    va "W-What'd it say?"
    
    va "No, nevermind! We're done. We're so dead."
    show mc neutral at left 
    mc "It was saying numbers, I think."
    
    mc "Six? Three?"
    
    va "Forget about it! L-Let's just leave..."
    show mc happy at left 
    mc "Hi, could you say that again?"
    hide mc happy 
    hide vance neutral 
    play sound "<from 1 to 3>./sfx/static.wav" 
    "Instead of repeating the words the ghost phone releases a brief burst of static.
    Then it falls silent and stays that way."
    show mc scared at left 
    show vance scared at right 
    mc "You know what? Let's just...go."
    play sound runningLoud
    "We nearly fall on top of each other scrambling to get out of the cramped bathroom."
    hide mc scared 
    hide vance scared 
    
    return





label diningroom_elodie:
    show elodie happy 
    el "Okay. Let's go!"
    hide elodie happy 

    scene bg diningRoom
    
    "We shuffle into the dining room, where a table capable of seating four and its chairs sit."
    
    show elodie neutral 
    "Instead of scanning the room for the presence of ghosts,"
    play sound cameraMultiple
    "Elodie pulls out her phone and starts taking pictures of the paintings hanging on the wall."
    show elodie neutral at right with ease 
    show mc scared at left 
    mc "Elodie? What are you doing?"
    show elodie smug at right 
    el "I'm taking pics for Ginstagram. People go wild for this kind of creepy stuff."
    show elodie neutral at right 
    mc "Shouldn't we...search for the ghost?"
    show elodie smug at right 
    el "Ha! You can't be serious! You actually fell for this crap? It's a ploy!"
    hide mc scared 
    hide elodie smug 
    "It can't be! The company has teams of ghost hunters. Ours is just one of many."
    
    "They all have ghost hunting equipment and hundreds of reports of completed cases."
    
    "It's not possible to fake all of that."
    show mc neutral at left
    mc "You've been here longer than me. Haven't you seen ghosts yourself?"
    
    show elodie neutral at right 
    el "They're fake. Probably an actor, hired by the so-called client."
    hide mc neutral at left
    hide elodie neutral 
    "There's probably hidden cameras recording our reactions."
    show mc neutral at left 
    show elodie smug at right 
    mc "And our tools?"
    
    el "Please, this Energy Maker Free! (edition) reacts to almost anything."
    play sound electronicAmbience
    "As if on cue, the EMF meter beeps high and long. The lights on the device flash yellow."
    show mc scared at left 
    mc "Signs of a ghost! It could be here in this room with us." with vpunch 
    
    show elodie neutral at right 
    el "Ugh, there's no ghost. It's just responding to my phone."
    hide mc scared at left 
    show elodie neutral at middle with ease 
    "She moves her phone close to the device and submits whatever post she's making on her social media."
    hide elodie neutral 
    "{i}beeeeep{/i}"
    
    "The EMF meter climbs another frequency, light turning orange."
    show elodie neutral
    el "It's just the internet. No such thing as ghosts."
    
    el "And for the rest, Ilse just carries around a vacuum cleaner.
    Vance's special ghost phone? Just an old radio."
    hide elodie neutral 
    "As I blankly process this information, Elodie wraps an arm around my shoulder."
    show elodie smug 
    el "Aww, don't be so sad. Take a selfie with me to commemorate! We can go watch 
    Vance and Ilse run around fighting with the air after. Say 'cheese'!"
    play sound camera01
    "Elodie snaps a selfie, snickering all the while as she leaves the room."
    hide elodie smug with dissolve 
    show mc neutral at left 
    "Wow. She truly believes there's nothing to believe in."
    hide mc neutral at left 
    
    "Behind her, a lamp suddenly flickers on and off within the blink of an eye." 
    
    "Elodie's forgotten EMF meter ranks up yet another notch, blinking bright red."
    
    "{i}beeeeeeeeeeeeeep{/i}"
    
    "Then, nothing."
    show mc scared at left 
    mc "Ha. Haha...ha. No such things as ghosts? Yeah, right."
    
    mc "Then what the heck was that?!" with vpunch 
    
    "Eyes wide in silent terror, I follow Elodie out." 
    
    "It's not like she'd believe me if I told her."

    hide mc scared

    return


label ch04:

    scene bg livingRoom
    python: 
        if renpy.music.is_playing(channel=u'music') == True:
            renpy.music.stop(channel=u'music', fadeout=None)
    "We arrive in the living room once more, gathering around a non-existent campfire."
    show elodie neutral at left with ease
    show vance neutral at right with ease 
    show ilse happy at middle with ease
    
    il "Well, gang? Did you find signs of the ghost? In the study, there was a sudden draft."
    il "The windows were firmly shut. Could’ve been the ghost. Didn’t see it, though."
    show vance scared at right 
    va "The ghost phone did say things. It was creepy!"
    show vance neutral at right 
    va "I couldn’t make out the words...but I, um, ran soon after so I didn’t hear more."

    el "Uhhhhhh…"

    el " ...The EMF beeped?"
    show ilse neutral with ease 
    il "That’s plenty of signs. There’s definitely a ghost present. But if none of us saw it in these rooms,
    it must be upstairs."
    play sound creak_short
    "Ilse takes the lead, wooden steps creaking under their feet."
    hide ilse neutral with dissolve 
    play sound footsteps
    "Vance turns towards the front door, but Elodie grabs him before he can take a step in that direction
    and pushes him up the stairs."
    #show elodie neutral at right with easeinleft  
    hide elodie neutral with dissolve
    hide vance neutral  with dissolve 
    
    #show mc neutral at left with ease 

    "There’s nothing to do but follow."
    hide mc neutral with dissolve 
    
    
    jump ch05


label ch05:
    scene bg hallway with dissolve 
    play music mainbgm volume 0.5 loop
    "The air is clearly different up here. It’s thick and tense; each breath is suffocating."

    show ilse neutral with ease
    "Ilse leads us towards the room at the end of the dark hall and the rest of us follow like obedient little ducklings."
    hide ilse neutral with dissolve 
    "We pass by multiple rooms and I can only wonder why we’re skipping them. Were we going to split up again?"
    scene bg door with dissolve 
    "One door catches my eye. It looks the same as every other door in the house, but for some reason, it feels different."

    "Well, unlike the rest of the rooms we’ve passed upstairs, it’s open just a crack, while the rest seem to be firmly shut."

    "The long vertical black line of the open door begs for my attention."

    "I reach out with my flashlight as if to prod the door wider open."
    
    # TODO: continue this dialogue
    menu:
        "No. I should catch up with the rest of the team.":
            jump catchUpWithTeam
        "A little peek won’t hurt anyone.":
            jump littlePeek
label catchUpWithTeam:
    "No. I should catch up with the rest of the team."
    "I look up to find the hallway empty. Have the others already reached the last room?"
    "I scurry forward into the room. They must be waiting for me…"
    scene bg bedroom2 with dissolve 
    #insert cg here? 
    "Inside the room is my team, alright. But they’ve all collapsed on the ground!"
    show mc scared at left with ease 
    mc "Everyone?" 
    mc "Elodie?"
    mc "Vance?"
    mc "Boss?"
    hide mc scared 
    "{i}Aaauuuueeeeuuuoooogghhh...{/i}"
    "And I’m not alone either..."
    "I turn around to see —"

    #enter ghost    
    show ghost mad with dissolve 
    "The Ghost!"
    hide ghost mad 
    show mc scared at left 
    mc "Aah!" with vpunch 
    hide mc scared 
    show ghost mad 
    g "AhhH - Hhh - - hh"
    hide ghost mad 
    show mc scared at left 
    mc "What...did you do to my team?"
    hide mc scared 
    show ghost mad 
    g "OOoo - - ouuu - u - UUUuu - - - - - tttt"
    hide ghost mad 
    show mc scared at left 
    mc "That...sounds like words. Kind of sounded like ‘out’. Are you...talking to me?"
    hide mc scared 
    show ghost mad with dissolve 
    "The ghost hisses again."
    hide ghost mad with dissolve 
    show mc neutral at left 
    "I’ve got to figure out what it’s trying to say to find out what happened to the others."
    hide mc scared at left with dissolve 
    jump hangman

label littlePeek:
    scene bg bedroom1 with dissolve 
    "I push the door open and nearly run headfirst into another person."
    "Wait. Another person?!"
    show ghost mad with dissolve 
    "\"WwwhhhhooOOO\""
    "The Ghost!"
    hide ghost mad 
    show mc scared at left 
    mc "AAHH!!" with vpunch 
    "I didn’t just nearly run headfirst into it, I did run headfirst straight through it! And it’s angry!"
    "The ghost looms over me as I stumble backwards." 
    hide mc scared 
    show vance scared at right 
    va "Oh no, now you’ve done it!"
    show ilse scared at left  
    il "Run! Before it gets you! We’ll do our best to catch up!"
    hide vance scared 
    hide ilse scared 

    jump begin_chase_room

