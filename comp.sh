#!/usr/bin/zsh
compton_lockfile=/tmp/compton.lock
if [[ -e ${compton_lockfile} ]]; then
		kill $(pgrep compton)
		rm ${compton_lockfile}
else
		touch ${compton_lockfile}
		compton --vsync drm --unredir-if-possible --paint-on-overlay -cGCb -t-5 -l-5 -r4 -o.55 -m.95
fi
exit 0
