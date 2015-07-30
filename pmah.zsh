#!/usr/bin/env zsh
# poor man's aur helper
for i in jq curl; do
	whence $i &>/dev/null || { printf "missing %s!\n" $i >&2; exit 1 }
done

pacman -Qm | while read package version; do
	eval upstream=$(curl -s "https://aur4.archlinux.org/rpc.php?type=info&arg=$package"|jq '.results.Version?')
	if [[ -n $upstream && $version != $upstream ]]; then
		printf "%s :: %s -> %s\n" $package $version $upstream
	fi
done
