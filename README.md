
# Wall Me

Push notifications sent directly to your terminal. Just what you needed 👍

## Tests

Build the test container

```
docker build --file Dockerfile.pytest --tag wallme-pytest .
```

Alias `docker run` so something nicer

```
WORKDIR=$PWD
SVC_ACCT_CREDENTIALS=<path to json creds>
alias pytest="docker run -it --rm -u $(id -u) \
--workdir /work \
--volume  $WORKDIR:/work \
--env     USER_EMAIL=test@example.com \
--env     PYTHONPATH=/work \
--volume  $SVC_ACCT_CREDENTIALS:/credentials.json \
--env     GOOGLE_APPLICATION_CREDENTIALS=/credentials.json  \
wallme-pytest"
```

Now run

```
pytest
```

