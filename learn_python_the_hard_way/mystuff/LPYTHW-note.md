### Preface
1. The hard way is easier
	1. Go through each exercise.
	2. Type in each sample exactly.
	3. Make it run.
2. Three most essential skills that a beginner needs:
	1. reading and writing: get to know the language symbols.
	2. attention to details: separates good from the bad in any profession.
	3. spotting differences: training yourself to notice mistakes, bugs, and other problems.
3. Do Not Copy-Paste
4. If you run into a Study Drill you can't do or a lesson you just do not understand, the skip it and come back to it later. 

### EX7
1. Comment is translate from code to English. 
2. More than 80 characters in one line is a bad style.

### EX8
1. Should I use %s or %r for formatting?
	You should use %s and only user %r for getting debugging information about something. The %r will give you the "raw programmer's" version of variable, also known as the "representation."
2. Why does %r sometimes print things with single-quotes when I wrote them with double-quotes? 
	Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. This is perfectly fine since %r is used for degugging and inspection, so it's not necessary that it be pretty.

### EX9
1. read manual, type `pydoc raw_input` to read the manual of function `raw_input`, `pydoc` can also read the manual of python-keyword/

### EX10
1. Escape sequences
|---|---|
|Escape|What is does.|
|`\\`|Backslash(\)|
|`\'`|Single-quote(')|
|`\"`|Double-quote(")|
|`\a`|ASCII bell(BEL)|
|`\b`|ASCII backspace(BS)|
|`\f`|ASCII formfeed(FF)|
|`\n`|ASCII linefeed(LF)|
|`\r`|ASCII carriage return(CR)|
|`\t`|ASCII horizotal tab(TAB)|
|`\v`|ASCII vertical tab(VT)|
|`\uxxxx`|Character with 16-bit hex value xxxx(Unicode only)|
|`\Uxxxxxxxx`|Character with 32-bit hex value xxxxxxxx(Unicode only)|
|`\N{name}`|Character named name in the unicode database(Unicode only)|
|`\ooo`|Character with octal value|
|`\xhh`|Character with hex value|



