tags: #easy #forensics #picoCTF2024
extra tags: #shell #browserWebshellSolvable #qrCode

# Scan Surprise
_I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead? You can download the challenge files here:_
- [challenge.zip](https://artifacts.picoctf.net/c_atlas/3/challenge.zip)
_The same files are accessible via SSH here: `ssh -p 52394 ctf-player@atlas.picoctf.net` Using the password `6dd28e9b`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!_

_hints:_
- _QR codes are a way of encoding data. While they're most known for storing URLs, they can store other things too._
- _Mobile phones have included native QR code scanners in their cameras since version 8 (Oreo) and iOS 11_
- _If you don't have access to a phone, you can also use zbar-tools to convert an image to text_
## Solution
Download the chall zip file and extract the contents. Navigate through the folders until you get to `flag.png`.

Using any device, scan the qr code. This will reveal the flag in text form and will appear in the url.

![[IMG_4208.jpg]]
## Flag
_note that flag may differ_
||`picoCTF{p33k_@_b00_a81f0a35}`||