tags: #medium #forensics #picoCTF2022
extra tags: #pcap
# Packets Primer
_Download the packet capture file and use packet analysis software to find the flag.
- [Download packet capture](https://artifacts.picoctf.net/c/196/network-dump.flag.pcap)_

_hints:_
- _Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product._

## Solution
Open the pcap file using a packet analysing software such as [Wireshark](https://www.wireshark.org/). We are met with something like this (note: the colouring and amount of information shown may differ - you can change these in settings)

![[Screenshot 2026-04-06 at 10.46.01 pm.png]]

From here, we can see that information was sent through TCP stream between two IP addresses. To follow the stream, we can click on a packet (the first one), and right click -> follow -> TCP. From here, we can see the flag is in the first stream.

![[Screenshot 2026-04-06 at 10.45.39 pm.png]]

We can now just copy the flag out.
## Flag
_note that flag may differ_
||`picoCTF{p4ck37_5h4rk_01b0a0d6}`||