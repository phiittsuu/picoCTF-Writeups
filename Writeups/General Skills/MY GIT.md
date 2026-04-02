tags:  #easy #generalSkills #picoCTF2026
extra tags: #git

# PROBLEM_NAME
_I have built my own Git server with my own rules! You can clone the challenge repo using the command below. `git clone ssh://git@foggy-cliff.picoctf.net:50468/git/challenge.git` Here's the password: `d9df7038` Check the README to get your flag!_

_hints:_
- _How do you specify your Git username and email?_
## Solution
Starting the instance gives us a git repo to clone with the password. Simply copy the command into the terminal to clone the repo.
![[Screenshot 2026-04-02 at 4.33.28 pm.png]]
We can go into the repo using `cd challenge`, and then we can list the files in the repo using the command `ls`.
![[Screenshot 2026-04-02 at 4.36.23 pm.png]]
We can open the README file using any application such as vscode, or in the terminal using `cat`.
![[Screenshot 2026-04-02 at 4.37.11 pm.png]]
We can see from the description that we need to push the `flag.txt` file into master using the given username and email.  First, we can create a `flag.txt` file. We can do this using `touch flag.txt`. If we use `ls`, we can see now that the file is in the repo.
![[Screenshot 2026-04-02 at 6.56.18 pm.png]]
Now, we can add the file using `git add` and create a commit for it. We can change the author of who is committing by using `-author`.
![[Screenshot 2026-04-02 at 6.58.28 pm.png]]
Now, we can push this file into master using `git push origin master`, and type in the original password. It should return saying this was successfully done, as well as the flag.
![[Screenshot 2026-04-02 at 6.59.47 pm.png]]
## Flag
_note that flag may differ_
||`picoCTF{1mp3rs0n4t4_g17_345y_e522152d}`||