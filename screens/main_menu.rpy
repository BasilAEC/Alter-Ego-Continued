
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "gui/main_menu_background.png"

    vbox:
        xalign 0.5
        yalign 0.5
        yoffset 50
        spacing 50

        textbutton _("-CLICK TO START-") action ShowMenu("load") text_font 'fonts/jiyunotsubasa.ttf'

define config.main_menu_music = 'audio/alterego.wav'
