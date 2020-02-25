
# Wall Me

Push notifications sent directly to your terminal. Just what you needed 👍

## 

Test

```
export WORKDIR=$PWD
prove="docker run -it --rm -u $(id -u) \
--workdir /work \
--volume  $WORKDIR:/work \
--env     USER_EMAIL=test@example.com \
benlittle6/pytest"
```

