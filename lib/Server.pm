use strict;
use warnings;
use 5.10.0;

use FindBin qw($Bin);
use lib "$Bin/local/lib/perl5";
package Server;
use parent qw(HTTP::Server::Simple::CGI);
 
sub handle_request {
    my ($self, $cgi) = @_;
    print 'HTTP/1.0 200 OK\r\n';
    exit 0;
}

1;

