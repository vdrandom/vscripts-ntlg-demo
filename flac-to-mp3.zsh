#!/usr/bin/env zsh
read_tags() {
	metaflac $1 --show-tag=ALBUM --show-tag=ARTIST --show-tag=GENRE --show-tag=DATE --show-tag=TITLE --show-tag=TRACKNUMBER --show-tag=TRACKTOTAL |\
		sed s/=/~..~/ |\
		awk -F'~..~' '{print $1"='\''"$2"'\''"}'
}
mime_is() {
	mimetype=$(file -b --mime-type $1)
	if [[ $mimetype == $2 ]]; then
		return 0
	else
		return 1
	fi
}
for i in $argv[@]; do
	if mime_is $i 'audio/x-flac'; then
		local original=$i
		eval $(read_tags $original)
		local out_dir=/home/von/Music/\[UNSORTED\]/$ARTIST/$ALBUM
		[[ -d $out_dir ]] || mkdir -p $out_dir
		local converted=$out_dir/${i%.*}.mp3
		flac -c -d $original | lame -V0 --add-id3v2 --pad-id3v2 --ignore-tag-errors \
			--ta $ARTIST --tt $TITLE --tl $ALBUM --tg ${GENRE:-12} --tn ${TRACKNUMBER:-0} --ty $DATE \
			- $converted
	else
		return 1
	fi
done
exit 0
