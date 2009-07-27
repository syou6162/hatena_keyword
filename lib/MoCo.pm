package MoCo;

use base qw 'DBIx::MoCo';
use DataBase;

__PACKAGE__->db_object('DataBase');

use Cache::Memcached;
my $cache = Cache::Memcached->new;
$cache->set_servers( ["localhost:11211"] );
__PACKAGE__->cache_object($cache);    # Enables caching by memcached

sub moco (@) {
    my $model = shift;
    return __PACKAGE__ unless $model;
    $model = join '::', 'Moco', $model;
    $model->require or die $@;
    $model;
}

1;
