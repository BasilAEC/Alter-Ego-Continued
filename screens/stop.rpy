
label neuend:

scene bg es side
with fade
stop music

"You have reached the end of Wanderer."

"There are five scenarios but four endings in total."

"The destination is the same, it is the path that's different."

"Go try them all."

"If you have seen everything, then please don't forget to critique this project."

"visit {a=https://www.reddit.com/user/TheOneWhoWandered/}{color=#7DF9FF}u/TheOneWhoWandered on reddit{/color}{/a} to see the project's current status. Contact me if you need or want to say anything regarding the project."

"No, Es doesn't cook anything in this build."

"She will in the next build. Probably..."

"Hopefully."

"Until next time."

"Exit Harlequin, stage left."

return

label idend:

scene bg es dom
with fade
stop music

stop sound
"You have reached the end of ID."

"There are five scenarios but four endings in total."

"The destination is the same, it is the path that's different."

"Go try them all."

"If you have seen everything, then please don't forget to critique this project."

"visit {a=https://www.reddit.com/user/TheOneWhoWandered/}{color=#7DF9FF}u/TheOneWhoWandered on reddit{/color}{/a} to see the project's current status. Contact me if you need or want to say anything regarding the project."

"No, Es doesn't cook anything in this build."

"She will in the next build. Probably..."

"Hopefully."

"Until next time."

"Exit Harlequin, stage left."

return
label seend:

scene bg es lib
with fade
stop music

"You have reached the end of SuperEgo."

"There are five scenarios but four endings in total."

"The destination is the same, it is the path that's different."

"Go try them all."

"If you have seen everything, then please don't forget to critique this project."

"visit {a=https://www.reddit.com/user/TheOneWhoWandered/}{color=#7DF9FF}u/TheOneWhoWandered on reddit{/color}{/a} to see the project's current status. Contact me if you need or want to say anything regarding the project."

"No, Es doesn't cook anything in this build."

"She will in the next build. Probably..."

"Hopefully."

"Until next time."

"Exit Harlequin, stage left."

return

label aeend:

scene bg es prom
with fade
stop music

"You have reached the end of Es."

"There are five scenarios but four endings in total."

"The destination is the same, it is the path that's different."

"Go try them all."

"If you have seen everything, then please don't forget to critique this project."

"visit {a=https://www.reddit.com/user/TheOneWhoWandered/}{color=#7DF9FF}u/TheOneWhoWandered on reddit{/color}{/a} to see the project's current status. Contact me if you need or want to say anything regarding the project."

"No, Es doesn't cook anything in this build."

"She will in the next build. Probably..."

"Hopefully."

"Until next time."

"Exit Harlequin, stage left."

return

init:
    $ style.hyperlink_text = Style(style.say_dialogue) # inherits from the default dialog look, so it'll look like the rest of the dialogue, and we'll just have to change the look of the link hovered
    $ style.hyperlink_text.hover_bold = True # make it bold when hovered.
