package DataBase;
use base qw(DBIx::MoCo::DataBase);
__PACKAGE__->dsn('dbi:mysql:dbname=test');
__PACKAGE__->username('');
__PACKAGE__->password('');
1;


