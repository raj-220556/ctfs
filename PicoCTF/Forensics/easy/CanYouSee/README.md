## Process

To check the metadata of a file. use popular `exiftool` it gives lots of information about image
 
To install tool:
 
```bash
 sudo apt install libimage-exiftool-perl
```
 
use like 
```bash
 unzip unknown.zip
 exiftool ukn_reality.jpg
```
```
ExifTool Version Number         : 12.76
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2026:02:26 21:24:56+05:30
File Access Date/Time           : 2026:02:26 21:25:02+05:30
File Inode Change Date/Time     : 2026:02:26 21:24:56+05:30
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```

Here Attribution URL is suspicous.

```bash
$ echo cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg== | base64 -d
picoCTF{ME74D47A_HIDD3N_d8c381fd}
```
