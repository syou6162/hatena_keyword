#!/opt/local/bin/perl
use warnings;
use strict;

use lib "./lib";
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use HTML::Template;
use Template;
use HTML::FillInForm;
use Keyword;
use Text::Hatena;
use DateTime::Format::MySQL;

my $query  = CGI->new;
my @params = $query->param;

if ( defined( $query->param("keyword") ) ) {
    if ( my $keyword =
        Keyword->retrieve( keyword => $query->param("keyword") ) )
    {
        print $query->header( -charset => "utf-8" );
        my @keywords = @{ Keyword->retrieve_all->sort(
                sub {
                    my ( $a, $b ) = @_;
                    DateTime::Format::MySQL->parse_datetime( $b->{last_edit} )
                      <=> DateTime::Format::MySQL->parse_datetime(
                        $a->{last_edit} );
                }
            )
          }[ 0 .. 14 ];
        my $param = {
            keywords => \@keywords,
            keyword  => $keyword->{keyword},
            content  => Text::Hatena->parse( $keyword->{content} ),
        };
        my $template = new Template();
        my $output   = "";
        $template->process( 'keyword.tt', $param, \$output, );
        print $output;
    }
    else {    # queryはきたけど、DBにはなかった
        print "Location: ./create_new_keyword.cgi?keyword="
          . $query->param("keyword") . "\n\n";
    }
}
else {
    print "Location: ./show_page.cgi\n\n";
}

exit;
