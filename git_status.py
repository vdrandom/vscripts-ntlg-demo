#!/usr/bin/python3
import os
import pygit2

def test_status(num, stat_key):
    if num & stat_key:
        return 1
    else:
        return 0

if os.path.isdir(".git"):
    repo = pygit2.Repository(".git")
    files = repo.status()
    staged = 0
    unstaged = 0
    confl = 0
    for filename in files:
        staged += test_status(files[filename], pygit2.GIT_STATUS_INDEX_NEW)
        staged += test_status(files[filename], pygit2.GIT_STATUS_INDEX_DELETED)
        staged += test_status(files[filename], pygit2.GIT_STATUS_INDEX_MODIFIED)
        unstaged += test_status(files[filename], pygit2.GIT_STATUS_WT_NEW)
        unstaged += test_status(files[filename], pygit2.GIT_STATUS_WT_DELETED)
        unstaged += test_status(files[filename], pygit2.GIT_STATUS_WT_MODIFIED)
        confl += test_status(files[filename], pygit2.GIT_STATUS_CONFLICTED)
    result = str()
    if staged > 0:
        result += 's' + str(staged)
    if unstaged > 0:
        result += '+' + str(unstaged)
    if confl > 0:
        result += 'x' + str(confl)
    if not result:
        result += '.'
    print(result)
