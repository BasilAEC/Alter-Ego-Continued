label cookae:
$ ae = True

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

jump aeend
