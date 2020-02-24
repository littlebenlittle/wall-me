use strict;
use warnings;
use 5.10.0;

package Your::Web::Server;
use base qw(HTTP::Server::Simple::CGI);
 
sub handle_request {
    my ($self, $cgi) = @_;
    print 'HTTP/1.0 200 OK\r\n';
    exit 0;
}

package main;

my $srv = Your::Web::Server->new;
$srv->run;

