tags:  #easy #generalSkills #picoCTF2026
extra tags: 

# Undo
_Can you reverse a series of Linux text transformations to recover the original flag? Additional details will be available after launching your challenge instance._

_hints:_
- _For text translation and character replacement, see [`tr` command documentation](https://man7.org/linux/man-pages/man1/tr.1.html)._

## Solution
First, start the instance for the problem. Connect to the problem in terminal using the given command `nc foggy-cliff.picoctf.net 60363`. (Note: the port number may differ). We are met with this screen.
![[Screenshot 2026-04-02 at 12.30.30 am.png]]
As we can see with the hint, the flag has been encoded with Base 64. This means we need to reverse the base 64 to get the original string using a linux command. The linux command to do this is `base64 -d <<< <str>`. We input this back into the script to get the next step. Note that we only input the linux command required, not the whole command.
![[Screenshot 2026-04-02 at 12.39.18 am.png]]
Now, the text has been reversed. We simply reverse the text again to get it back to the original. The command to reverse the text is `rev`.
![[Screenshot 2026-04-02 at 12.41.26 am.png]]
Now, the flag had the underscores replaced with dashes. To reverse this, simply reverse the dashes with underscores. The command to do this is `tr - _`. This can be found in the `tr` documentation.
![[Screenshot 2026-04-02 at 12.45.23 am.png]]
Now the curly braces were replaced with parenthesis. We can use the same command to reverse this, except we are replacing parenthesis with curly braces. This can be done with `tr () {}`.
![[Screenshot 2026-04-02 at 12.46.21 am.png]]
Now, ROT13 was applied. This means that the alphabet was shifted 13 letters to the front (Caesar cipher). To reverse this, we need to reverse the direction by 13 letters, or alternatively, rotate forward by 26-13 = 13 letters. We can use the `tr` command again to replace letters. for ROT13, any letters from N-Z onwards would rotate back to A-M when using ROT13. Hence, we need to split the way we call the command into replacing `A-MN-Za-mn-z` with `N-ZA-Mn-za-m` to account for this rotation back from Z to A. Essentially, we are saying A-M is to be replaced with N-Z, N-Z is to be replaced with A-Z, etc. This can be shown here.
![[Screenshot 2026-04-02 at 12.52.11 am.png]]
Now, we have successfully completed the challenge and gotten the flag :D
# Flag
_note that flag may differ_
||`picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_dcc1896c}`||