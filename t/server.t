use strict;
use warnings;
use 5.10.0;

use FindBin qw($Bin);
use lib "$Bin/../lib";
use Server;
use HTTP::Request;
use LWP::UserAgent;
use Test::More;

my $srv = Server->new;
unless (fork) {
    $srv->run;
    exit 0;
}
# my $req = HTTP::Request->new(GET => 'http://localhost:8080');
sleep 1;
my $ua = LWP::UserAgent->new(timeout => 1);
# my $res = $ua->request($req);
my $res = $ua->get('http://localhost:8080');
ok( $res->is_success );

done_testing();

