
Identified a buffer overflow vulnerability on line 21.

Looks like all I had to do was overwrite each of `c1`, `c2`, `c3`, `c4`, `c5`, `c6` to
be 'C', 'O', 'O', 'K', 'I', 'E'.


I took advantage of having access to `buff.c` by adding the following `printf`
statements to help me verify that I could overwrite the variables with the 
correct values:
```c
printf("c1 = %c\n", c1);
printf("c2 = %c\n", c2);
printf("c3 = %c\n", c3);
printf("c4 = %c\n", c4);
printf("c5 = %c\n", c5);
printf("c6 = %c\n", c6);
```

It seemed that I had to send a string of length 26 characters 
I did not calculate this length, I determined it by manual experimentation. I
believe that the way you determine this is by adding the the buffer size, 
which is 16, the size of the `buffer` variable that points to the buffer on
the stack, which is 8, and then 2 additional bytes for padding - I'm not 
confident is this is the correct reasoning, however.

Now, passing in 26 'a' characters followed by 'COOKIE' in reverse will fill
up variables `c1` to `c6` with 'COOKIE' and pass the check that will output
the flag: `aaaaaaaaaaaaaaaaaaaaaaaaaaEIKOOC`.

