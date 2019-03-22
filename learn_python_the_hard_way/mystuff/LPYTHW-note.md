---
### Style Guide for Python Code:
[Reference](https://www.python.org/dev/peps/pep-0008/#code-lay-out)

---

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

### Unicode
1. Put `_*_ coding: utf-8 _*_` at the head of file.

### EX7
1. Comment is translate from code to English. 
2. More than 80 characters in one line is a bad style.
```
print "So, you're %r old %s tall and %r heavy." % (
        age, height, weight
        )
```

### EX8
1. Should I use %s or %r for formatting?
	You should use %s and only user %r for getting debugging information about something. The %r will give you the "raw programmer's" version of variable, also known as the "representation."
2. Why does %r sometimes print things with single-quotes when I wrote them with double-quotes? 
	Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. This is perfectly fine since %r is used for degugging and inspection, so it's not necessary that it be pretty.

### EX9
1. read manual, type `pydoc raw_input` to read the manual of function `raw_input`, `pydoc` can also read the manual of python-keyword/

### EX10
1. Escape sequences  

|Escape|What is does.|
|---|---|
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


### EX11
1. raw_input()
	1. `age = raw_input('--->')` or `age = raw_input()`;
	2. `x = int(raw_input())`;
	3. `age = raw_input("How old are you? ")`;
2. `,` at the end of print line, e.g.`print "How old are your?",`. This is so that print doesn't go to next line. 

### EX12
1. [TBD] Read document of `open`, `file`, `os`, `sys`;

### EX13
1. modules

### EX15
1. class file()
	1. U mode: This mode is translate different kind of newlines in different platform to a `\n`.
	2. Methods:
		1. close, read, readline, truncate, write(stuff).


### EX18
1. function:
	1. checklist:
		* start with def
		* function name only have char and _
		* after ( to put your argument , ): to close parenthesis
		* 4 spaces to indent
		* no indent to end function
	2. *args ?
		* tell python to take all the arguments to the function and then put them in args as a list.
		
### EX20

1. file.seek()			--->	move to new file position, 
								defualt is file first byte.
2. file.read() 			---> 	read all the content of file
3. fiee.readline() 		---> 	read current line of content



