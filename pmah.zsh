#!/usr/bin/env zsh
# poor man's aur helper
uri='https://aur4.archlinux.org'
for i in jq curl; do
	whence $i &>/dev/null || { printf "missing %s!\n" $i >&2; exit 1 }
done
updates=()
pacman -Qm | while read package version; do
	eval upstream=$(curl -s "$uri/rpc.php?type=info&arg=$package"|jq '.results.Version?')
	if [[ -n $upstream && $version != $upstream ]]; then
		printf "%s :: %s -> %s\n" $package $version $upstream
		updates+=$package
	fi
done
print "Do you want to download the pkgbuilds here? (C-c to cancel)"
read none
for i in $updates; do
	git clone "$uri/$i.git"
done
