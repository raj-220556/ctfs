# process

checked different ways

```bash
$ cat cat.jpg | strings | grep "pico"
$ less cat.jpg
No identify available
Install ImageMagick to browse images
```

Hint: Look at the details of file

```bash
$ file img 
img: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
# No use of zsteg
$ zsteg img 
[!] #<ZPNG::NotSupported: Unsupported header "\xFF\xD8\xFF\xE0\x00\x10JF" in #<File:img>>
```
- but here zsteg gives me idea `Unsupported header`

so i checked header `\FF\D8\FF` ok it says it is JPEG file

```bash
$ cp cat.png img
$ ghex img
```
 Removed header completely of `img` file
 
```bash
$ file img
img: data
$ less img
# Hey it gives different from perivous data so checked
# Again <cc:license rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/> looks suspicous
```

```bash
$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
picoCTF{the_m3tadata_1s_modified}
```
