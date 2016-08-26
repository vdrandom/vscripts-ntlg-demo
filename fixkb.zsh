#!/usr/bin/env zsh
pkill xxkb
setxkbmap -layout us,ru -variant altgr-intl,typewriter -option ctrl:nocaps,grp:win_space_toggle,grp_led:caps,compose:menu
xkbcomp $DISPLAY - | egrep -v "group . = AltGr;" | xkbcomp - $DISPLAY 2>/dev/null
xxkb & disown
