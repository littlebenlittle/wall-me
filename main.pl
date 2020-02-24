use strict;
use warnings;
use 5.10.0;

use FindBin qw($Bin);
use lib "$Bin/lib";
use Server;

my $srv = Server->new;
$srv->run;

