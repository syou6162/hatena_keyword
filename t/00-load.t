#!perl -T

use Test::More tests => 1;

BEGIN {
	use_ok( 'Keyword' );
}

diag( "Testing Keyword $Keyword::VERSION, Perl $], $^X" );
