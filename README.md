
# Wall Me

Push notifications sent directly to your terminal. Just what you needed 👍

## Tests

Build the test container

```
docker build --file Dockerfile.pytest --tag wallme-pytest .
```

Alias `docker run` so something nicer

```
export WORKDIR=$PWD
alias pytest="docker run -it --rm -u $(id -u) \
--workdir /work \
--volume  $WORKDIR:/work \
--env     USER_EMAIL=test@example.com \
--env     PYTHONPATH=/work \
wallme-pytest"
```

Now run

```
pytest
```

