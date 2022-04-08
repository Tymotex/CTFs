# Keygenme

What made this problem challenging was the amount of distractions in the script.
Luckily, the important values containing the flag were provided upfront:

```python
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

To solve this problem quickly, I just chased down the reference for
`key_full_template_trial` and saw that it was being used in the `check_key`
function.

Next, I checked how the `check_key` function was being called and quickly traced
that it was being called when you selected the option:

```
(c) Enter License Key
```

Now, I examined the `check_key` function closely and found these series
of if-statements:
```python
if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
    return False
else:
    i += 1
...
```

It seemed that these are used to validate that the user-inputted key was indeed
the key, but it's obfuscated with the sha256 hashing. It seemed that the
`check_key` function would return true for when all this if-statements passed,
so I supposed that the flag value would have its unknown values simply be each
of these sha256 output characters. I simply printed all of their values like
this:

```python
print(hashlib.sha256(username_trial).hexdigest()[4])
print(hashlib.sha256(username_trial).hexdigest()[5])
print(hashlib.sha256(username_trial).hexdigest()[3])
print(hashlib.sha256(username_trial).hexdigest()[6])
print(hashlib.sha256(username_trial).hexdigest()[2])
print(hashlib.sha256(username_trial).hexdigest()[7])
print(hashlib.sha256(username_trial).hexdigest()[1])
print(hashlib.sha256(username_trial).hexdigest()[8])

"""
Produces:
5
4
e
f
6
2
9
2
"""
```

I then took these characters and substituted them into the key placeholder
positions in `picoCTF{1n_7h3_|<3y_of_xxxxxxxx}` and obtained the flag.
