# static-canary
Solving a problem where it asks for the length of the input string. 
With trial and error, we find that the program seg faults at 128 A's. So the offset is 128 and we need to bruteforce the firsdt byte of the canary. So initially sent in 129 and ran a bruteforce to find the first byte.
As the output of the program returned "hacker detected", we're guessing the wrong byte. 
When we guess the right one it's "you said something". Based on this logic, we find the first byte. Now, the first byte is added to the offset and the length is 130. 

python -c 'print("148"+"\n"+"A"*128+"7a8c"+"A"*12+"\xc6\x86\x04\08")' > input.txt

It is upon trial and error that we find the gap between the canary and the win function to be 12 bytes
