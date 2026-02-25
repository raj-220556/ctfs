
## Solution
Let check metadata of file
```bash
$ head -n 20 confidential.pdf 
%PDF-1.7
%����
1 0 obj
<<
/Type /Pages
/Count 1
/Kids [ 4 0 R ]
>>
endobj
2 0 obj
<<
/Producer (PyPDF2)
/Author (cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0\075)
>>
endobj
3 0 obj
<<
/Type /Catalog
/Pages 1 0 R
>>
```

here Author data looks suspicious so, lets find
```bash
$ echo cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jYTc2YmJiMn0 | base64 -d
picoCTF{puzzl3d_m3tadata_f0und!_ca76bbb2}base64: invalid input
```

