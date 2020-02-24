FROM perl:5.30

WORKDIR /usr/src/wallme
COPY . .
ENV PERL5LIB=/usr/src/wallme/local/lib/perl5
CMD [ "perl", "main.pl" ]

