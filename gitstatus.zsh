#!/usr/bin/env zsh
git_status=''
staged_count=0
unstaged_count=0
untracked_count=0
ifs_temp=$IFS
IFS=
if ! raw_status=$(git status --porcelain -bu 2>/dev/null); then
    exit 1
fi

while read line; do
    if [[ $line[1,2] == '##' ]]; then
        IFS='.'
        read branch _ _ origin <<< $line[4,-1]
    fi
    [[ $line[1,2] =~ '.[MD]' ]] && (( unstaged_count++ ))
    [[ $line[1,2] =~ '[MDARC].' ]] && (( staged_count++ ))
    [[ $line[1,2] == '??' ]] && (( untracked_count++ ))
done <<< $raw_status

(( $unstaged_count > 0 )) && git_status+="u$unstaged_count"
(( $staged_count > 0 )) && git_status+="s$staged_count"
(( $untracked_count > 0 )) && git_status+="+$untracked_count"
[[ -z $git_status ]] && git_status='.'

full_status="[ $branch {$origin} $git_status ]"

printf '%s' $full_status
