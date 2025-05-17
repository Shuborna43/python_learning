1. regex: ab -> a immediately followed by bytearray
2. regex: a|b -> either a or b or both 
3. regex: a? -> 0 or 1 or multible a [? mark is called optional]
4. regex: ab?c -> a and c are fixed/must (e.g. ac), b is optional and 0 or multiple b can be there but the position of b should be between a and c, e.g. abc.  
5. regex: (ab)? -> 0 or 1 or multiple groups of ab 
6. regex: a* -> 0 or more a's 
7. regex: (ab)* -> 0 or more groups of ab 
8. regex: a(bc)*d -> ad with 0 or more bc groups between. a and d must. 
9. regex: ab*c -> a and c must. o or more b's. position of b should be between a and c.
10. regex: a+ -> 1 or more a's. 
11. regex: ab+c -> at least 1 b is must. a and c are must. so one pattern of abc should be there. 
12. regex: a{2} -> exactly 2 consicutive a's.  
13. regex: ab{2}c -> abbc fixed 
14. regex: ab{2} -> abb fixed 
15. regex: (ab){2} -> abab fixed 
16. regex: a{,5} -> between 0 and 5 a's 
17. regex: a{2,} -> atleast 2 a's 
18. regex: a{2,5} -> 2 to 5 a's 
19. regex: ab{2,5}c -> a 2 to 5 b's c, abbc-----abbbbbc
20. regex: . (period)-> any single character except new line (/n) 
21. regex: a.b -> ab with exactly one character between them except new line (\n).  
22. regex: a.*b -> ab with o or more characters between them except new line (/n).
23. regex: ^a -> starts with a
24. regex: a$ -> ends with a 
25. regex: ^abc$ -> starts and ends with abc. abc fixed. e.g. abc
26. regex: [aeiou]: atleast one of the characters of the list is present.open
27. regex: ^[aeiou]$: only one charater of the list  e.g. only a, onlye, only i, only o, only u. 
28. regex: [a-z]-> contains any single charater between lowercase a and z. 
29. regex: ^[a-z]$ -> any one character between lowercase a and z. 
30. regex: ^[a-z]{2,3}$ -> any one character between lowercase a and z, 2 or 3 times. 
31. regex: [a-z-] -> contains any single charater between lowercase a and z or a -. 
32. regex: [a-zA-Z]-> contains any single charater between a and z, not case sensitive. 
33. regex: [a-zA-z/d] or [a-zA-Z0-9]:contains any single charater/digit between a and z, not case sensitive.  
34. regex: [^a-z]: contains a charater that is not between lowercase a to z. (^ with in bracket means not accepted )
35. regex [*+$123]: behaves like single character. contains any single charater that is * or + or $ or 1 or 2 or 3.
36. regex: ^[123-567]$: starts and ends with any of the characters in the list. e.g only 1 or only 2 or only 3............or only 7.   