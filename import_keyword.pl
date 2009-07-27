use strict;
use warnings;

use Perl6::Say;
use File::stat;
use DateTime;
use lib "./lib";
use Keyword;
use Data::Dumper;
use File::Basename;

# my $keyword = Keyword->retrieve(keyword => "hoge");

# print Dumper($keyword);
# say $keyword->{content};
# $keyword->content("hogehoge");

# Keyword->create(
# 		keyword => "hgoefdjaffafasfa",
# 		content => "fdsfasfasfsaf",
# 	       );

my $keyword_base = "/Users/syou6162/hatena_keyword/syou6162";

opendir( DIR, $keyword_base ) or die "can't opendir $keyword_base : $!";

while ( defined( my $file = readdir(DIR) ) ) {
    my $file_with_full_path = $keyword_base . "/" . $file;
    next
      unless
        -f $file_with_full_path; # ディレクトリ関係のものは飛ばす
    open FILE, $file_with_full_path or die "can't open $file : $!";
    my $buf;
    read( FILE, $buf, ( -s $file_with_full_path ) );
    my ( $name, $dir, $ext ) = fileparse( $file, ('\.txt') );
    unless ( Keyword->retrieve( keyword => $name ) ) {
        my $last_edit = DateTime->from_epoch(
            time_zone => 'Asia/Tokyo',
            epoch     => stat($file_with_full_path)->mtime
        )->strftime('%Y-%m-%d %H:%M:%S');
        Keyword->create(
            keyword   => $name,
            content   => $buf,
            last_edit => $last_edit
        );
    }
    close(FILE);
}

