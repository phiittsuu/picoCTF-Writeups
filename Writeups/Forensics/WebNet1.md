tags: #hard #forensics #picoCTF2019
extra tags: #pcap

# PROBLEM_NAME
_We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/picopico.key). Recover the flag._
_hints:_
- _Try using a tool like Wireshark._
- _How can you decrypt the TLS stream?_

## Solution
First, following the TLS stream does not provide any information. This is expected because the TLS stream is currently RSA encrypted and cannot be read.

We are provided the key, so we can use this to decrypt the TLS traffic. If we go to Preferences -> RSA Keys and then import the RSA key, we can then reload Wireshark and it will attempt to use the key to decrypt the traffic. We can see new information come up.

If we now follow the TLS stream, we can see that we can actually read the data, and in stream 0 we can find the flag.

![[Screenshot 2026-06-23 at 10.04.02 pm.png]]

## Flag
_note that flag may differ_
||`picoCTF{honey.roasted.peanuts}`||