tags: #easy #reverseEngineering #picoCTF2019
extra tags: #java

# PROBLEM_NAME
_Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://challenge-files.picoctf.net/c_fickle_tempest/379ca32f89b74c70403ef5b6515ae2f1d2405e66735347b70bc2ef8063084688/VaultDoorTraining.java)_

_hints: (none)_
## Solution
Looking at the java source, we can see a comment stating that the password is in the source code. The password can be found  in the `checkPassword` method, and the password contains the flag. In this case, it can be found in the line:
```java
	return password.equals("w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt");
```

We can then wrap the password into the flag format.
## Flag
_note that flag may differ_
||`picoCTF{w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt}`||