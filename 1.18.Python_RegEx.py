# RegEx can be used to check if a string contains the specified search pattern.

'''
Metacharacters
[]	A set of characters	"[a-m]"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
'''

import re


def TrueFalse(key, result):
	if result:
		print(f"Yes!, We found this. The key is:{key}")
	else:
		print(f"No! We don't found this. The key is: {key}")

txt = "The quick brown fox jumps over the lazy dog"
x = re.search("fox" ,txt)
TrueFalse("x", x)

y = re.search("^The.*lazy", txt)
TrueFalse("y", y)

z = re.findall("ov", txt)
TrueFalse("z", z)
