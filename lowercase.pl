#!/usr/bin/env perl
use strict;
use warnings;
use File::Copy;
use File::Find;
use Cwd 'cwd';
use feature 'say';

sub pathname {
	return my $pathname = $File::Find::dir . '/' . $_[0];
}

sub lowercase {
	if ($_ eq '.') {
		return 0;
	}
	my $original = $_;
	$_ =~ s/(^.*)/\L$1/g;
	my $lowercased = $_;
	if ($original eq $lowercased) {
		say 'No need to rename ' . $original . ', it is already in lower case.';
		return 0;
	}
	say 'Renaming ' . pathname($original) . ' to ' . pathname($lowercased) . '...';
	move("$original", "$lowercased");
}

finddepth(\&lowercase, @ARGV);
say 'Everything done.';
exit 0;

