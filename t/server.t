use strict;
use warnings;
use 5.10.0;

use FindBin qw($Bin);
use lib "$Bin/../lib";
use lib "$Bin/../local/lib/perl5";
use Server;
use HTTP::Request;
use LWP::UserAgent;
use Test::More;

unless (fork) {
    system "perl main.pl";
    exit 0;
}
sleep 1;
my $ua = LWP::UserAgent->new(timeout => 1);
my $res = $ua->get('http://localhost:8080');
ok( $res->is_success );

done_testing();

