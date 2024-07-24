label cookid:
$ id = True
$ quick_menu = True
scene bg library
with dissolve

"{i}A few hours later...{font}{/i}"

show es sad
with dissolve

s "..."

m "..."

m "Are you okay?"

s "I-I am doing fine now..."

m "That doesn't sound like \'fine\' to me."

m "Your voice is cracking."

m "..."

s "..."

m "The impulses are back, aren't they?"

s "..!"

s "How..."

s "How do you know?"

m "I know you better than yourself, Es."

m "{i}{color=#D3D3D3}Obviously, you don't remember a thing...{/color}{/i}"

m "Regardless, I am surprised you got so angry."

m "You usually calm yourself down before you escalate to this degree."

s "I...I don't know what happened."

s "Some part of me just...snapped when you said that it wasn't that big of a deal."

m "Well, what do you think now?"

m "Were you right in doing what you did?"

s "No. Obviously not."

s "I overreacted. There is no denying that."

"{i}Es squeezes [povname]'s hand.{/i}"

s "This won't happen again."

m "Promise?"

s "Promise."

m "Very good."

s "..."

m "Now that everything's said and done,"

m "...can you finally greet me?"

play audio "audio/lightbulb.wav"

s "..!\nI totally forgot about greeting you in the midst of this!"

m "Time to remember, then."

s "Of course."

s "..."

show es neutral
with dissolve

s "..."

show es happy
with dissolve

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

s "Do you actually want to try my hypotesis, though?"

m "I wouldn't mind."

show es happy
play music "silence.wav"

s "Great."

s "That hypothesis would be discussed later."

s "Meanwhile, I want to talk about the book I was reading."

m "I almost forgot about that."

m "What's that book anyway?"

s "It's a cookbook."
stop music

jump idend
