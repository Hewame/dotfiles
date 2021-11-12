#!/bin/sh
udiskie -A --notify --smart-tray &
exec /usr/bin/lxsession -s qtile -e qtile &
#nitrogen --restore &
compton &
# clipit: alternative/replacement
diodon &
nm-applet &
lxpolkit &
eval $(gnome-keyring-daemon --start) &
export SSH_AUTH_SOCK &
emacs --daemon &
