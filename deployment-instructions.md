# clays-magic-funhouse-ctf Deployment

## Challenge Information

Link: https://github.com/claythess/CTF_4770

Difficulty: Easy/Medium

Category/Categories: Remote code injection/Reverse Shell

Author: Clay Hess

Description:

```
Participants will need to find a way to discover the website pages, inject code into a vulnerable prompt, and setup a remote shell 
to discover the flag on the filesystem.
```

## Dependencies

- Python v3.x
- Flask

## First-Time Setup
```
git clone https://github.com/claythess/CTF_4770.git
pip install Flask
```

## Starting up the Challenge

I was unable to get this to work in wsl. I recommend running on a linux machine.

```
python ctf.py
```

It should say "* Running on http://x.x.x.x" - distrubute this IP to challenge participants. Do not distribute anything else
to the participants.