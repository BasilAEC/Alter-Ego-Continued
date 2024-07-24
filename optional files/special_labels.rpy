## Special Labels ##############################################################
##
## These are special labels that Ren'Py automatically recognizes if they
## are included with the game. Read more here:
## https://www.renpy.org/doc/html/label.html#special-labels
##

## Splash Screen ###############################################################
##
## Put the splash screen code here. It runs when the game is launched.
##

define splash_txt = "{font=fonts/font.ttf}Where ID is,\nthere ego shall be.{/font}"

define sigmund = "{font=fonts/font.ttf}-Sigmund Freud.{/font}"

label splashscreen:

    scene black
    with Pause (2)
    
    show text splash_txt with dissolve
    with Pause (3)

    hide text with dissolve
    with Pause (1)

    show text sigmund with dissolve
    with Pause (3)

    hide text splash_txt with dissolve
    with Pause (2)

    return
## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return
