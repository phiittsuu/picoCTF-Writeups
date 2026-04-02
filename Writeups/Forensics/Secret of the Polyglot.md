tags: #easy #forensics #picoCCTF2024
extra tags: #fileFormat #polyglot

# Secret of the Polyglot
_The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file? Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/97/flag2of2-final.pdf)._

_hints:_
- _This problem can be solved by just opening the file in different ways_

## Solution
When the file is first downloaded, it can be seen that the file is a pdf file. Opening this file reveals the second half of the flag (as stated by the name of the file)
![[Screenshot 2026-04-02 at 7.19.50 pm.png]]
By the challenge description and the hint, it can be inferred that the file is actually of multiple file types. We can try different common file types until the file successfully opens. In this case, we change the file type from `.pdf` to `.png`. This then opens as an image instead, giving the first half of the flag.
![[Screenshot 2026-04-02 at 7.21.24 pm.png]]
## Flag
_note that flag may differ_
||`picoCTF{f1u3n7_1n_pn9_&_pdf_724b1287}`||