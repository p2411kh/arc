# arc

tar, zip и unzip в одной команде.

```
arc -t czf out.tar.gz dir/
arc -z -r out.zip dir/
arc -u out.zip -d dest/
```

## Установка

```
./configure --prefix=$HOME/.local
make && make install
```
