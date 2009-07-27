#!/opt/local/bin/perl
use warnings;
use strict;

use lib "./lib";
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Keyword;

my $query  = CGI->new;
my @params = $query->param;

if ( defined( $query->param("keyword") ) ) {
    if ( my $keyword =
        Keyword->retrieve( keyword => $query->param("keyword") ) )
    {    # すでに登録してあった
        Keyword->delete($keyword);
    }
    else {

        # 登録されてないのに削除しにきたらスルー
    }
}

print "Location: ./show_page.cgi\n\n";

exit;

