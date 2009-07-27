#!/opt/local/bin/perl
use warnings;
use strict;

use lib "./lib";
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use HTML::Template;
use Template;
use DateTime;
use HTML::FillInForm;
use Perl6::Say;
use Keyword;
use Text::Hatena;
use Data::Dumper;
use DateTime::Format::MySQL;
use Sidebar;
use Model;

my $query  = CGI->new;
my @params = $query->param;

my $param = { keywords => Sidebar->recent_keywords };

my $template = new Template();
my $output   = "";

print $query->header( -charset => "utf-8" );

if ( $query->param("keyword") && $query->param("content") )
{    # 完了した場合

    if ( my $keyword =
        Keyword->retrieve( keyword => $query->param("keyword") ) )
    {    # すでに登録してあった
        Model->update( $keyword, $query->param("content") );
    }
    else {
        Model->update( $keyword, $query->param("content") );
    }
    ${ %{$param} }{"keyword"} = $query->param("keyword");
    ${ %{$param} }{"content"} = $query->param("content");

}
elsif ( defined( $query->param("keyword") ) ) {    # 新規登録にきた場合
    if ( my $keyword =
        Keyword->retrieve( keyword => $query->param("keyword") ) )
    {    # すでに登録してあった
        ${ %{$param} }{"keyword"} = $query->param("keyword");
        ${ %{$param} }{"content"} = $keyword->{content};
    }
    else {    # まだ登録はしてなかった
        ${ %{$param} }{"keyword"} = $query->param("keyword");
        ${ %{$param} }{"content"} = "";
    }
}
$template->process( 'create_new_keyword.tt', $param, \$output );
print $output;

exit;
