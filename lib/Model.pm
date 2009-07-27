package Model;

use warnings;
use strict;
use DateTime;
use lib "./lib";
use Keyword;

sub update {
    my $self    = shift;
    my $keyword = shift
      or die "first arguement must be the instance of Keyword class : $!";
    my $content = shift || "";
    my $last_edit = shift
      || $self->now();
    $keyword->content($content);
    $keyword->last_edit($last_edit);
}

sub register {
    my $self      = shift;
    my $name      = shift;
    my $content   = shift || "";
    my $last_edit = shift
      || $self->now();
    Keyword->create(
        keyword   => $name,
        content   => $content,
        last_edit => $last_edit
    );
}

sub delete {
    my $self    = shift;
    my $keyword = shift
      or die "first arguement must be the instance of Keyword class : $!";
    Keyword->delete($keyword);
}

sub now {
    DateTime->now( time_zone => 'Asia/Tokyo', )->strftime('%Y-%m-%d %H:%M:%S');
}

1;
