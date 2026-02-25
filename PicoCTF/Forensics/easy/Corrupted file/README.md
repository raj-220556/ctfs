## Process 
check that hint he says that `file header` corupted and it is `JPEG`

check hexdump data of file
```bash
$ xxd file
```

To to edit hexdump data use `ghex` editor 
```bash
$ ghex file
```

- change first `5c 78` to `ff d8`

Now it is a img file open it.

you saw a flag

![flag](file)
