#!/bin/sh
#compton &
nitrogen --restore &
#qtile
bash $HOME/sbar.sh &
exec dwm 
