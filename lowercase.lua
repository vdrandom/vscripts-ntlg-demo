#!/usr/bin/env lua
require('os')
require('lfs')

function lowercase(basename, basedir)
	if basedir == nil then
		basedir = ''
	end
	local lowercased = string.lower(basename)
	local path_orig = basedir .. basename
	local path_new = basedir .. lowercased
	if path_orig == path_new then
		print(path_orig .. ' is already lowercase!')
		return 1
	else
		print('Renaming: ' .. path_orig .. ' -> ' .. path_new)
		os.rename(path_orig,path_new)
	end
end

function is_dir(name)
	local ftype = lfs.symlinkattributes(name, "mode")
	if ftype == "directory" then
		return true
	else
		return false
	end
end

function find_and_rename(path)
	for basename in lfs.dir(path) do
		if basename ~= "." and basename ~= ".." then
			local basedir = path .. '/'
			local filename = basedir .. basename
			if is_dir(filename) then
				find_and_rename(filename)
			end
			lowercase(basename, basedir)
		end
	end
end

function test_and_execute(dir)
	if is_dir(dir) then
		find_and_rename(dir)
		lowercase(dir)
	else
		print(dir .. ' is not a directory or does not exist!')
	end
end
local i = 1
while arg[i] do
	test_and_execute(arg[i])
	i = i + 1
end
