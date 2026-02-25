## Process 

download file
```bash
wget https://challenge-files.picoctf.net/c_amiable_citadel/1b638a2799b26ff08169f1703b4f0f2738599d68ffafe63b8f6ea303b3d596ab/img.jpg
```

```bash 
$ ls
img.jpg
```

Always first check file properties. It's a good habit
```bash
$ file img.jpg 
img.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9", baseline, precision 8, 640x640, components 3
```
`c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9` looks suspicious.

```bash
$ echo c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9 | base64 -d
steghide:cEF6endvcmQ=
```
It's given password for stegfile
```bash
$ echo cEF6endvcmQ= | base64 -d
pAzzword
```

To Install steghide `sudo apt install steghide`

Extract data from a steg file
```bash
$ steghide extract -sf img.jpg 
Enter passphrase: 
wrote extracted data to "flag.txt".
```

```bash
$ ls
flag.txt  img.jpg
```

```bash 
$ cat flag.txt 
picoCTF{h1dd3n_1n_1m4g3_1c55ccd0}
```
