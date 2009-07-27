package Sidebar;
use warnings;
use strict;

use lib "./lib";
use Template;
use DateTime;
use Keyword;
use DateTime::Format::MySQL;

sub recent_keywords {
    my $self     = shift;
    my $num      = shift || 9;
    my @keywords = @{ Keyword->retrieve_all->sort(
            sub {
                my ( $a, $b ) = @_;
                DateTime::Format::MySQL->parse_datetime( $b->{last_edit} )
                  <=> DateTime::Format::MySQL->parse_datetime(
                    $a->{last_edit} );
            }
        )
      }[ 0 .. $num ];
    return \@keywords;
}

1;
