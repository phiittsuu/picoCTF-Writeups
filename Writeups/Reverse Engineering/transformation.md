tags: #easy #reverseEngineering #picoCTF2021
extra tags: #bitShift

# transformation
_I wonder what this really is... [enc](https://challenge-files.picoctf.net/c_wily_courier/674625d8d402913559bbf26af30624c1612390df8e263ca54c32748ccb4afefe/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])_

_hints:_
- _You may find some decoders online_
## Solution
From the description, we see a snippet of code written in Python. This is likely the method of encoding, and features moving bits, more specifically, joining 8-bit characters into 16-bits characters. Opening the `enc` file we can see a series of (Chinese) characters.

```灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽```

In Python, we can do the transformation directly from the string. We can write a simple (script) to decode by reversing the bit joining. We do this by shifting the first set by 8, and then AND `0xFF` to get the least significant byte.

```python
def main():
	enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽"
	flag = ''.join([chr(ord(c) >> 8) + chr(ord(c) & 0xFF) for c in enc])
	print(flag)

if __name__ == "__main__":
	main()
```

Running the script outputs the flag.
## Flag
_note that flag may differ_
||`picoCTF{16_bits_inst34d_of_8_b7f62ca5}`||