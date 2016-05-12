#!/usr/bin/env zsh
pacman -Q|while read package _; do
	pkg_size=$(pacman -Qi $package|grep 'Installed Size'|awk '{print $4$5}')
	printf "%s %s\n" $pkg_size $package
done
exit 0
