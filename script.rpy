# Greetings. If you are here I assume you want to make a fork of this project.
# To erase the existing script. Delete the code of script.rpy, cookae.rpy. stop.rpy and cookid.rpy

# I hope you make something good.
define s = Character('Es', color="#FFFFFF", callback=callback) #usecallback for bip noise
define m = Character('[povname]', color="#FFFFFF", what_font = "fonts/GenEiKoburiMin6-R.ttf", what_size = 30,)
define narrator = Character(what_font = "fonts/font.ttf") #GenEiKoburiMin6-R
define bi = Character('???', color="#FFFFFF", what_font = "fonts/GenEiKoburiMin6-R.ttf",what_size = 30,)
image es angry = "es angry.png"
image es neutral = "es neutral.png"
image es dom = "es dom.png"
image es happy = "es happy.png"
image es left = "es left.png"
image es right = "es right.png"
image es sad = "es sad.png"
image es very happy close = "es very happy close.png"
image es very happy open = "es very happy open.png"
image co1 = "bg es prom.png"
image co2 = "bg es cat.png"
image co3 = "bg es school.png"
image co4 = "bg es dom.png"
image co5 = "bg es lib.png"
image co6 = "bg es shop.png"

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

label start:

default ae = False
default se = False
default id = False

$ quick_menu = False

image trippy:
    "tripa.jpg"
    0.1 #this part defines how long to wait before next frame
    "tripb.png"
    0.1
    "tripc.png"
    0.1
    "tripd.jpg"
    0.1
    "tripe.jpg"
    0.1
    "tripf.jpg"
    0.1
    repeat

show trippy
play music "audio/silencecursed.mp3"

pause 2
$ quick_menu = True

"..."

"..."

"..."

"..."

"..."

"You came back."

bi "..."

bi "I..."

bi "I can't feel my body."

bi "..."

bi "You did something, didn't you?"

bi "Explain yourself, Ego Rex."

"Listen, dear child."

"I mean no harm."

"Do not be afraid."

"I have noticed..."

"You are still coming."

"You still attend to Es."

bi "I thought you were okay with her presence?"

"I am, child."

"But..."

"She no longer conducts tests."

bi "And?"

"She is satisfied with her current situation."

"You have no reason to come here anymore."

"And yet, you come."

"A lot, even."

"Tell me."

"Why do you continue to visit her?"

menu:

    "I don't answer to delusions.":
        jump id

    "I don't want her to kill herself again.":
        jump se

    "I love her.":
        jump ae

    "It doesn't concern you.":
        jump na

label id:

    $ id = True

    "I see that You and Es are now similar."

    "I had different expectations..."

    bi "You know what happened when I tried to \'reform\' her."

    bi "I was almost killed before restoring time to its previous state."

    bi "Do you want something like {b}{i}that{/i}{/b} happen again?"

    "No, my dear Child."

    "While I would prefer her to dissappear from this world..."

    "I know you will restore the world back to what it was."

    "Like you did before."

    "I can do nothing but to let you go."

    "My dear child,"

    "Go ahead."

    "I will not stop you."

    "Though I have one last thing to ask before I allow you to leave."

    bi "Make it quick."
    jump name_select

label se:

    $ se = True

    "\"Kill herself\"?"

    "Are you referring to when she willed herself to disappear from this world?"

    bi "If you are willing to use an euphemism then so be it."

    bi "You and your heart are made of stone; someone like you wouldn't understand what happened to her on that day."

    "I fail to see it, Child."

    "What there is to understand?"

    "She was a filthy harlot."

    "Impulsive...destructive..."

    "We had a pristine, clean world."

    "Free of imperfecton. Full of rule and order."

    "And you went back to alter it."

    bi "This is exactly what I meant. I almost pity you."

    bi "You know..."

    bi "She wasn't the only one who died that day."

    bi "If your plan is to turn this world \'perfect\' again then I regret to inform you that it isn't going to happen."

    bi "Not now. Not ever."

    "..."

    "I understand."

    "Even if she doesn't want to conform anymore..."

    "She will not destroy this world."

    bi "She would not. Not unless you keep me away from her."

    bi "You have to let me go if you want to save the world, Ego Rex."

    "..."

    "It appears that I have no choice but to comply."

    "Go ahead."

    "I will not stop you."

    "Though I have one last thing to ask before I allow you to leave."

    bi "Make it quick."

jump name_select

label ae:

    $ ae = True

    "You...love Es?"

    bi "Yeah."

    "I don't get it, Child."

    "What's there to like about her?"

    "She's cold or hateful towards the two entities she is aware of."

    "Her behavior doesn't befit a maiden with her beauty either."

    "She has no desirable traits."

    bi "Heh..."

    "..?"

    bi "Hahahaha!"

    bi "You don't actually know her, Façade."

    bi "That was a long time ago."

    bi "Even when she was cold..."

    bi "I found solace with her in the library."

    bi "Reading books, conversing with her about those said books. Sharing our opinions..."

    bi "Debating over the nature of man. I knew myself a little better each time I exited that place..."

    bi "We both found each other."

    "Is that so?"

    "While I do not approve you mingling with Es that much,"

    "She will not destroy this world as long as She is accompanied by you."

    "Forcing You and Es may cause catastrophic damage and you aren't willing to compromise."

    "Go ahead."

    "I will not stop you."

    "Though I have one last thing to ask before I allow you to leave."

    bi "Make it quick."
    jump name_select

label na:

    bi "What makes you think I answer to you, Stone Monarch?"

    "I will not tolerate disobedience."

    bi "What are you gonna do? Banish me?"

    bi "Go ahead."

    "..."

    bi "Just don't forget that she wouldn't tolerate you taking me away from her either."

    bi "I had to reform the past and reshape the future when She destroyed the world."

    bi "She doesn't do well on her own."

    bi "She didn't even knew how bad things were until I came."

    bi "You know you can't stop her."

    bi "Letting Es and me meet is the only way this place retains any sense of order."

    "..!"

    "...I understand."

    "It seems that I will not get any answers about you and Es.."

    "Very well."

    "But before that..."

    "I must know the answer of one question."

    bi "Make it quick."
    jump name_select

label name_select:

    python:
        povname_valid = False
        banned = ["estamer", "esfucker", "ego rex", "arse", "arsehead", "arsehole", "ass", "ass hole", "asshole", "nigga", "nigger", "bastard", "bitch", "shit", "pedo", "pedophile", "motherfucker", "Es", "es"]
        while not povname_valid:
            povname = renpy.input("{font=fonts/font.ttf}It has been a long while since you manifested here, and yet I don't know your name. What is it?{/font}")
            povname = povname.strip()
            if povname.lower() in banned:
                narrator("{font=fonts/font.ttf}Wrong.{/font}", interact=True)
            else:
                povname_valid = True
        if not povname:
            povname = "Maki"

"[povname]..."

"..."

"I will let you be on your way."

"Farewell, my child."

"And you remember..."

"...do the right thing."

show dream b
with dissolve

m "..."

show dream c
with dissolve

m "..."

show dream d
with dissolve

m "..."

scene black
with dissolve

$ quick_menu = False
pause 6

stop music

pause 5

jump cook

label cook:

$ quick_menu = True

m "{i}{color=#D3D3D3}I gently open the door.{/color}{/i}"

play audio "click.wav"

m "..."

$ quick_menu = False
scene bg library
with fade
$ quick_menu = True

m "..."

m "{i}{color=#D3D3D3}The library.{/color}{/i}"

m "{i}{color=#D3D3D3}The same as always.{/color}{/i}"

if se:
    m "{i}{color=#D3D3D3}Es is sitting on her chair. She isn't reading a book. A rare occurance.{/color}{/i}"

    show es sad
    with flash
    play audio "realization.wav"

    m "Es?"

    s "..."

    m "You look distressed. Are you alright?{nw}"

    play audio "badum.wav"
    play music "conform.opus"

    s "I can't fucking take it anymore."

    s "The same fucking day before the same fucking day after."

    s "Nothing fucking changes."

    s "I wake up I read I sleep I wake up I read I sleep I wake up I read I sleep I wake up I read I sleep I wake up I read I sleepI wake up I read I sleep I wake up I read I sleepI wake up I read I sleepI wake up I read I sleepI wake up I read I sleep I wake up I read I sleepI wake up I read I sleep I wake up I read I sleep I wake up I read I sleep I wake up I read I sleepI wake up I read I sleepI wake up I read I sleep I wake up I read I sleep{nw}"

    s "WHAT'S THE FUCKING POINT?!"

    s "I am just rotting away in this coffin I call my \'home\'"

    s "Why do you even come here [povname]?"

    s "What's even there to do or see here then just..."

    s "Hallucinate things that don't even exist?!"

    s "I W A N T T O F U C K I N G D I E{nw}"

    play audio "supershock.wav"

    m "{b}ENOUGH!{/b}"

    m "{i}{color=#D3D3D3}I place my hands on Es' shoulders. I shake her while I say,{/color}{/i}"

    m "What has gotten to you? What turned you into...into..."

    m "{i}{color=#D3D3D3}My voice cracks.{/color}{/i}"

    m "{i}This?{/i}"

    s "I...I...wish I knew [povname]."

    s "I just woke up from a horrible nightmare, and my mind got worse and worse the more I tried to think about other things."

    s "I was in a room. I had no...body of my own, and yet I somehow existed."

    s "The room had walls like the pages of a book. The walls are becoming smaller and smaller and smaller and smaller."

    s "They won't stop shrinking they never stop shrinking PLEASE I DON'T WANT TO SUFFOCATE"

    m "..."

    s "[povname] PLEASE stay with me I can't live without you."

    m "..."

    s "I don't know what I am gonna do if you leave."

    m "..."

    s "If no one is there to see you does that mean you don't exist?"

    m "..."

    s "Does that mean I only exist whenever you come here?"

    m "..."

    s "Is that it? Is this my whole purpose?"

    m "..."

    s "Why are you silent?! Answer me, please."

    m "I...I..."

    m "I don't have the answers you seek, Es."

    m "{i}{color=#D3D3D3}I hug Es with all my strength.{/color}{/i}"

    m "What I do know is that you would be fine in the end."

    m "Everything would be fine in the end."

    m "Everything."

    m "Everything..."

    scene black
    with dissolve
    hide es sad
    with dissolve

    m "{i}{color=#D3D3D3}Es later calmed down and got herself together, while I consoled her.{/color}{/i}"

    m "{i}{color=#D3D3D3}She did not kill herself this time.{/color}{/i}"

    m "{i}{color=#D3D3D3}She is now sleeping, safe for the time being.{/color}{/i}"

    m "{i}{color=#D3D3D3}Before that, she told me about the book she was reading prior to her episode.{/color}{/i}"

    m "{i}{color=#D3D3D3}It was a cook book.{/color}{/i}"

    jump seend

m "{i}{color=#D3D3D3}Es is sitting on her chair, reading a book as usual.{/color}{/i}"

show es left
with dissolve
play audio "pageturn.wav"

s "..."

show es right
with dissolve
play audio "realization.wav"

m "{i}{color=#D3D3D3}I can't see the title of the book. The cover is hidden by her hands.{/color}{/i}"

show es left
with dissolve
play audio "pageturn.wav"

m "{i}{color=#D3D3D3}I walk towards her. I am now at a distance where I should be visible to even a blind man.{/color}{/i}"

show es right
with dissolve
play audio "pageturn.wav"

s "..."

m "{i}{color=#D3D3D3}She still isn't noticing me. She is too engrossed in that book.{/color}{/i}"

show es left
with dissolve
play audio "pageturn.wav"

m "..."

m "{i}{color=#D3D3D3}You leave me no choice, Es.{/color}{/i}"

play audio "shoop.wav"

m "{i}{color=#D3D3D3}I try to snatch the book out of her hands...{/color}{/i}"

play audio "deskslam.wav"

m "{i}{color=#D3D3D3}...but she immediately snagged my arm.{/color}{/i}"

m "..."

s "..."

show es neutral
with dissolve

s "..."

s "What are you doing, [povname]?"

m "I...I was trying to—"

if ae:

    s "You know you can just tell me to stop, right?"

    s "Why grab my book like that?"

    s "It is rude."

    m "I am really sorry Es."

    m "I couldn't handle you ignoring me like that."

    s "It isn't that big of a deal, [povname]."

    s "..."

    s "Your face..."

    s "It looks funny."

    s "..?"

    s "You look like you saw a divine figure."

    menu:
        "Yeah, I am looking at a goddess right now.":
            jump god

    label god:
    show es very happy open

    s "...heheheh..."

    show es happy

    s "You are so stupid."

    s "And yet I love you so much."

    s "Why?"

    m "Probably because you're stupid too."

    s "You will not get away from this."

    s "Let me prove to you how I am not stupid."

    s "You called me a goddess."

    s "Now I don't know if I really am a goddess,{nw}"

    m "You are."

    s "What?"

    m "I said,"

    m "You really are a goddess. Crystal clear. Beyond the shadow of doubt."

    s "Shut up [povname]. Let me continue."

    s "Where was I? Yes, goddess."

    s "I actually managed to get hold of books which contain mythologies of different cultures."

    s "I, unfortunately have no idea what cultures exist in our reality and what cultures do not."

    s "With that being said..."

    s "I find it really interesting that how the gods are depicted in these mythologies."

    s "For instance..."

    s "Jesus of Nazareth is a god from a country called \'Israel\'."

    s "In their holy book The Bible, Jesus of Nazareth is depicted as displaying properties like kindness and selflessness."

    s "Apparently He is from the heavens, taking on a mortal form just to take the humans there with him..."

    s "...eventually he died by execution. Said execition was conducted by the same humans he was supposed to take with him."

    s "How ironic."

    m "The disciples didn't appreciate their divine god at all."

    s "I wonder..."

    s "Does {i}my{/i} disciple appreciate their goddess?"

    m "What?"

    m "I don't understand..."

    s "You call your goddess by name? How despicable."

    m "..."

    play audio "realization.wav"
    play music "childish.mp3"

    m "My apologies, goddess."

    s "That's a good start~"

    s "Tell me..."

    s "Will you follow every every command this goddess gives you?"

    menu:

        "Yes.":
            pass

    s "Very good."

    s "The goddess demands her disciple to hold her hand."

    s "Will the disciple comply?"

    menu:

        "Offer the goddess your hand.":
            pass

    m "{i}{color=#D3D3D3}I offer my hand to the goddess.{/color}{/i}"

    s "..."

    pause 2

    s "I am satisfied."

    s "I shall give you my blessing, child."

    play audio "peck.wav"

    m "..!"

    m "{i}{color=#D3D3D3}S-she...{/color}{/i}"

    play audio "bang.wav"

    m "{i}{color=#D3D3D3}She kissed my hand!{/color}{/i}"

    s "..."

    stop music

    show es very happy open

    s "...hahahaha!"

    show es happy

    s "You look so flustered."

    s "I really got you there didn't I?"

    m "What do you mean \"got you\"?"

    s "I was only pretending, [povname]."

    m "..."

    m "..."

    s "This is the second time I pretended to be your lover."

    s "And yet you are still so shy~"

    s "Perhaps if we act more..."

    s "...you will do your part properly?"

    s "..."

    s "Look at that! I was so invested in pretending that I don't know what to do."

    m "You usually greet me when I enter."

    s "Let me fix that for you."

    s "..."

    jump cookae

s "I told you before that you do {b}NOT{/b} touch my book while it is in my hands."

s "It is disrespectful to me and my book."

s "And yet you..."

if id:

    show es angry
    with dissolve

    s "You did not learn. You never learn."

    m "Es..."

    menu:
        "It isn't that big of a deal.":
            jump sdeal

        "Forgive me.":
            jump bdeal

    label sdeal:
        show es happy
        with dissolve

        s "I understand."

        m "{i}{color=#D3D3D3}Es offers me the book she was reading, implying that she wants me to hold it.{/color}{/i}"

        m "{i}{color=#D3D3D3}I take the book and place it on the table that was near to me.{/color}{/i}"

        s "..."

        hide es happy
        with dissolve

        m "..."

        pause 2

        play audio "punch.wav"
        pause 1
        play audio "damage a.wav"
        pause 1
        play audio "kira.mp3"

        m "..!"

        show es angry
        with dissolve

        s "\"It isn't that big of a deal\"?"

        s "First, you enter without announcing your presence."

        s "Second, you try to take away my book — even though I told you not to multiple times."

        s "Third, instead of apologising you claim that \"it isn't that big of a deal\"?"

        s "The audacity!"

        m "{i}{color=#D3D3D3}It..it hurts...{/color}{/i}"

        s "Unfortunately for you [povname], the strike count is now three, and that's means you're out."

        show es dom
        with dissolve
        play audio "supershock.wav"
        play music "hotline.mp3"

        s "I won't let you disrespect me anymore."

        s "You have hurt my ego for long enough."

        m "{i}{color=#D3D3D3}S-she's going to kill me if I don't do anything!{/color}{/i}"

        hide es dom
        with dissolve

        "{i}{font=fonts/font.ttf}Es picks up the book [povname] placed on the table.{font}{/i}"

        m "Es I humbly apologise! I will neve—{nw}"

        show es dom
        with dissolve

        s "The time for apologising is over you fucki—{nw}"

        play audio "audio/objection.wav"

        m "{size=*2}{i}{b}ES PLEASE I AM SORRY!{/b}{/i}{/size}"

        stop music

        s "..."

        s "..."

        s "..."

        show es neutral

        s "I..."

        s "..."

        show es sad

        s "..."

        hide es sad
        with dissolve

        $ quick_menu = False

        scene black
        with dissolve

        pause 3

        jump cookid

        label bdeal:

        s "An apology?"

        m "Yeah. I would like to apologise for my crude behavior."

        s "..."

        s "Go on."

        m "When I came here, I saw you being so deep in that book."

        play music "patience.opus"

        m "I felt...jealous."

        s "Jealous, you say?"

        m "I...I don't really like it when you don't pay attention to me."

        m "That's why I snatch books right off your hands every now and then."

        m "It stings when you read that book, when you can talk to me instead."

        m "I am aware that this behavior is selfish; and I feel a deep sense of shame for it."

        m "I aim to correct this mistake in every possible manner."

        m "In fact, this is why I am asking you,"

        m "Please..."

        m "Forgive me."

        stop music

        s "..."

        show es neutral
        with dissolve

        s "Good job, [povname]."

        s "You really saved your skin."

        s "This could've gone very differently if you hadn't apologised."

        s "Trust me on that one."

        s "Regardless, I accept the apology."

        m "If you're alright with it, can I ask you a question?"

        s "I see no reason to refuse."

        m "Thank you."

        m "Es..."

        m "Were you feeling intense urges your impulses before?"

        s "..!"

        s "How do you know that?"

        m "Just a hunch of mine."

        m "Anyway, this is first time in ages that your impulses overwhelmed you like this."

        m "You used to become angry before but..."

        s "Not to this degree, yes."

        m "Any idea why you became like this out of nowhere?"

        s "I can't think of anything, I am afraid."

        m "Me neither."

        s "..."

        m "..."

        s "Can I say something?"

        m "I am all ears."

        play music "audio/dream.opus"
        show es happy

        s "I would like to apologise, too."

        m "..?"

        s "I had no right to treat you like this."

        s "Not after you have done so much."

        m "Es..."

        s "I would make sure this never happens again by controlling my impulses to the best of my abilities."

        m "Do you accept my apology, [povname]?"

        m "You have to ask?"

        s "Obviously I accept your apology."

        s "Excellent."

        m "Now that everything's said and done,"

        m "...can you finally greet me?"

        play audio "audio/lightbulb.wav"

        s "..!\nI totally forgot about greeting you in the midst of this!"

        m "Time to remember, then."

        s "Of course."

        s "..."

        stop music

        pause 3

        play music "audio/silence.wav"

        s "Welcome back, [povname]."

        s "You remember when I talked about dreaming in different environments once?"

        s "..."

        s "I can see you trying to hold your laugh in."

        show es neutral

        s "Hmph."

        show es happy

        s "Regardless, I have come up with a hypothesis."

        s "I hypothesize that if you and I hold hands and sleep..."

        s "Both of us would be in the same dream."

        s "..."

        stop music

        m "..."

        if ae:
            m "Just say you want me to hold your hand Es."
        else:
            m "That just sounds like an excuse to make me sleep with you."

        show es neutral

        s "..!"

        s "T-that's not what I..."

        if ae:
            m "Just ask if you want me to cuddle you to sle—{nw}"
        else:
            m "I didn't knew you had a thing for me. I am honestly very flatt—{nw}"

        show es very happy open

        s "S-shut up! Don't accuse me of such things."

        s "And don't you {i}dare{/i} say things like that to me ever again."

        pause 1

        s "..."

        pause 1

        m "..."

        show es neutral

        s "Do you actually want to try my hypothesis, though?"

        m "I wouldn't mind."

        show es happy
        play music 'silence.wav'

        s "Great."

        s "That hypothesis would be discussed later."

        s "Meanwhile, I want to talk about the book I was reading."

        m "I almost forgot about that."

        m "What's that book anyway?"

        s "It's a cookbook."

        jump idend

s "hmph."

s "This isn't worth getting angry."

m "I am glad we share the same thoughts."

s "You came at a good time, [povname]."

s "I have some interesting information I want to share with you."

s "If you are willing to listen, that is."

s "Well, are you?"

m "I don't see a reason not to."

s "Remember what I said about this place when we first met?"

s "That it doesn't matter."

s "It may sound hypocritical, but my opinion is now changed."

s "There are only so many books you can read before the boredom comes to haunt you."

s "So I decided to explore."

m "But you were always there when I came to visit?"

s "I explored when you weren't here."

s "I can't go outside like you, but I still wanted something."

s "Is it not fair for a person to see what's around them?"

s "I am now going to share my findings."

s "Are you still in the zone? I hope so, because we are going to take a deep dive."

play music "audio/complex.opus"

s "Let's start with the area we currently are in."

s "It appears to be a library."

s "Reason being the obvious existence of books and some wooden tables and chairs just laying around here."

m "Wait a minute. What is your definition of a library?"

s "Being in this place since my supposed existence I always used books as a reference for what reality is."

s "If something or someone exists in {i}one thousand{/i} books, I consider that a part of the reality."

s "Libraries are a common occurance in literature of all kind."

s "It was one of the first entities I filed in my list of things that exist in reality."

m "isn't it also possible that an entity is just easy to write about?"

m "For instance — from what I have read, there are at least {i}one thousand one hundred and eigty nine{/i} works of literature which contain advanced mechanical robots as part of the plot."

m "These robots in general are autonomous and some of them can even feel human emotions!"

m "I remember one of them in particular."

m "It was a head, and was carried around by a human all the time."

m "But I digress."

m "What I am trying to prove is this,"

m "Is it safe to say that robots like these exist in reality?"

m "There is a real possibility that these robots in literature are but a way for humans to portray their wishful thinking."

m "They don't exist."

s "I would argue that the same can be said for anything."

s "Though I must agree that it is hard to prove that anything is a part of reality."

s "Anyway, back to what I was saying,"

s "The library's dimensions are unclear."

s "I actually started reading a novel while I was walking as a way to measure time."

s "I completed the entire novel and then..."

s "...it felt as if I had made no progress whatsoever."

s "I was far from the starting point and yet everything was as you can expect."

s "The shelves you see here right now are the same shelves that populate that area."

s "At least the books were different..."

s "There is no variation."

s "I obviously started getting tired after walking for so long."

s "I needed a place to rest."

s "But there were nothing but more and more shelves."

s "I became so tired I slept on the floor."

s "That's very undignified of me, I am aware."

s "But I hope you understand why I did that."

s "I really was tired, I couldn't move to save my life."

s "With that being said, when I woke up..."

s "I was in the same place as we are now!"

s "Even though I am glad I didn't have to walk all the way back there, I also found it very insulting."

s "It felt like I was mocked."

s "Mocked for daring to explore, that is."

s "Are you stil here with me, [povname]?"

m "Yeah."

m "That's...very weird."

m "I can't say I know what happened when you were asleep."

m "I have an idea."

m "I say..."

m "You and I go together this time."

m "Perhaps we would find something if both of us walked together?"

s "I...have no reason to tell you no [povname]."

s "I don't mind walking with you."

s "I'll tell you when I decide to explore again."

s "..."

s "..."

stop music

m "..."

s "Why are you looking at me like that?"

s "Did I forgot to do something?{nw}"

s "Ah!"

s "I forgot to greet you."

s "I-I am so sorry [povname]. Let's shelf my ramblings about now."

s "We will discuss more about that later, deal?"

s "Deal."

s "..."

show es happy
with dissolve
play music "silence.wav"

s "Welcome back, [povname]."

s "You remember when I talked about dreaming in different environments once?"

s "..."

s "I can see you trying to hold your laugh in."

show es neutral

s "Hmph."

show es happy

s "Regardless, I have come up with a hypothesis."

s "I hypothesize that if you and I hold hands and sleep..."

s "Both of us would be in the same dream."

s "..."

stop music

m "..."

if ae:
    m "Just say you want me to hold your hand Es."
else:
    m "That just sounds like an excuse to make me sleep with you."

show es neutral

s "..!"

s "T-that's not what I..."

if ae:
    m "Just ask if you want me to cuddle you to sle—{nw}"
else:
    m "I didn't knew you had a thing for me. I am honestly very flatt—{nw}"

show es very happy open

s "S-shut up! Don't accuse me of such things."

s "And don't you {i}dare{/i} say things like that to me ever again."

pause 1

s "..."

pause 1

m "..."

show es neutral

s "Do you actually want to try my hypothesis, though?"

m "I wouldn't mind."

show es happy
play music "audio/silence.wav"

s "Great."

s "That hypothesis would be discussed later."

s "Meanwhile, I want to talk about the book I was reading."

m "I almost forgot about that."

m "What's that book anyway?"

s "It's a cookbook."

jump neuend
