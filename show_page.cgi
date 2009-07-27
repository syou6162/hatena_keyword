#!/opt/local/bin/perl
use strict;
use warnings;

use lib "./lib";
use Keyword;
use File::Basename;
use Template;
use Data::Dumper;
use Template::Plugin::Dumper;
use Perl6::Say;
use DBIx::MoCo::List;
use DateTime::Format::MySQL;

my @keywords = @{ Keyword->retrieve_all->sort(
        sub {
            my ( $a, $b ) = @_;
            DateTime::Format::MySQL->parse_datetime( $b->{last_edit} )
              <=> DateTime::Format::MySQL->parse_datetime( $a->{last_edit} );
        }
    )
  }[ 0 .. 14 ];

my $param = { keywords => \@keywords };

my $template = new Template();
my $output   = "";
$template->process( 'template.tt', $param, \$output, );

print "Content-type: text/html\n\n";
print $output;
exit;
