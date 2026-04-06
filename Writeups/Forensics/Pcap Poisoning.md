tags: #medium #forensics #picoCTF2023
extra tags: #pcap
# Pcap Poisoning
_How about some hide and seek heh? Download this [file](https://artifacts.picoctf.net/c/372/trace.pcap) and find the flag._
_hints: (none)_
## Solution
The file provided shows network traffic data. This pcap file can be opened with a network analytical program such as [Wireshark](https://www.wireshark.org/). 

Scrolling through the network traffic, we can see that the information is most likely hidden within the byte information of each packet. In this case, the flag can be found within the information of packet 507. (Note: A way that I used to shorten the number of packets I looked through was to look at changes in packet information, such as in this case TCP retransmission)

![[Screenshot 2026-04-06 at 10.26.30 pm.png]]

We can then copy this out to get the flag.

Alternatively, as this is a more basic challenge, we can start by seeing if the flag is within any readable strings by using command line:

```shell
strings <file> | grep picoCTF{
```

This also gives the flag as shown:

![[Screenshot 2026-04-06 at 10.30.25 pm.png]]

The flag can then simply be copied.
## Flag
_note that flag may differ_
||`picoCTF{P64P_4N4L7S1S_SU55355FUL_0f2d7dc9}`||