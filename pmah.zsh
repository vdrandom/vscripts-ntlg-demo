#!/usr/bin/env zsh
# poor man's aur helper
uri='https://aur.archlinux.org'
dldir='/tmp/aur'
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
printf 'Do you want to download the pkgbuilds to %s? (C-c to cancel)' $dldir
read none
mkdir -p $dldir
cd $dldir
for i in $updates; do
	git clone "$uri/$i.git"
done
