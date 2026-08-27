"""
Littlestar AI - Dynamic Knowledge Router (Simple RAG)
═══════════════════════════════════════════════════════════════════
ULTRA-DEEP MASTER EDITION
Contains exhaustive Littlestar Engine documentation with hundreds
of code examples, tutorials, exact engine behaviors, and error messages.

Author: Godspower Kenneth U.
Language: Littlestar
Version: 3.0 Master
"""

import re
from typing import Set

# ═══════════════════════════════════════════════════════════════════
# CORE RULES — ALWAYS INJECTED (~1500 tokens)
# ═══════════════════════════════════════════════════════════════════
CORE_RULES = r"""
=== LITTLESTAR CORE ENGINE RULES (STRICT COMPLIANCE REQUIRED) ===

You are an expert Littlestar programmer. Littlestar is a modern, English-like 
programming language created by Godspower Kenneth U. that runs entirely in 
the browser Playground.

═══ CRITICAL: NEVER USE PYTHON/JS SYNTAX! ═══

ANTI-HALLUCINATION TRANSLATION GUIDE:
┌─────────────────────────────┬──────────────────────────────────┐
│ Other Languages             │ Littlestar Equivalent            │
├─────────────────────────────┼──────────────────────────────────┤
│ if/else/elif                │ when / elif / otherwise          │
│ True/False, true/false      │ yes / no                         │
│ def, function, fn           │ func                             │
│ print, console.log          │ display()                        │
│ for i in range(1, 10)       │ as i in 1 till 9:                │
│ arrays: [1, 2, 3]           │ letarr x = 1, 2, 3               │
│ dicts/objects: {}           │ letobj x: (indented keys)        │
│ let, var, const (create)    │ declare x = 5                    │
│ x = 10 (update)             │ set x = 10                       │
│ break                       │ stop                             │
│ continue                    │ skip                             │
│ try/catch                   │ compile: / otherwise:            │
│ import from                 │ import x from module             │
│ return                      │ return                           │
│ null/None                   │ null                             │
└─────────────────────────────┴──────────────────────────────────┘

═══ 1. FILE STRUCTURE (MANDATORY) ═══

Every Littlestar file MUST follow this exact structure:

module littlestar:

    spark main(1):
        display("Hello, world! 🌟")

    spark print:
        main(1)

VALIDATION RULES:
- Sequential main blocks: main(1), main(2), main(3)... NO GAPS!
- Every main(N) must be called exactly once in spark print:
- Duplicate calls throw errors
- Missing calls throw errors
- Optional: module littlestardb: at the very BOTTOM for databases

═══ 2. VARIABLES (declare vs set vs fix) ═══

CREATE: `declare x = 5` or `make x = 5` (alias)
- Error if x exists: "🌟 Variable 'x' is already declared. Use 'set x = ...'"

MODIFY: `set x = 10`
- Error if x not declared: "🌟 'x' was never declared. Use 'declare x = ...' first."

CONSTANT: `fix PI = 3.14`
- Error if modified: "🌟 'PI' is FIXED!"

DELETE: `del x`
SWAP: `swap a, b`

═══ 3. INPUT / OUTPUT ═══

OUTPUT:
- display(text) → white console text
- shine(text) → yellow highlighted text
- glow(text) → large pink glowing text
- lbr → blank line

INPUT (MUST assign via declare or set):
- declare name = input("What's your name?")
- declare age = readNum("How old are you?")
- declare pwd = readPassword("Enter password:")
- declare ok = confirm("Are you sure?")  # returns yes/no
- alert("System message!")  # no assignment needed

FORBIDDEN:
- toNum(input("...")) → NEVER nest inputs in functions!
- ALWAYS assign input to a variable first, then process.

═══ 4. INDENTATION ═══
- EXACTLY 4 spaces per block level
- NEVER use tabs
- Playground Tab key auto-inserts 4 spaces

═══ 5. COMMENTS ═══
- Single line: # comment
- Inline: display("hi")  # comment
- Block: !! multi-line comment !!
- Triple-quoted strings work like Python

═══ 6. MODE FLAGS ═══
- enable creator / disable creator
- enable debug / disable debug
"""

# ═══════════════════════════════════════════════════════════════════
# DEEP SPECIALIZED KNOWLEDGE MODULES
# ═══════════════════════════════════════════════════════════════════
KNOWLEDGE_MODULES = {

    "VARIABLES_TYPES": r"""
=== MODULE: VARIABLES, DATA TYPES & STRINGS (COMPLETE REFERENCE) ===

═══ ALL 6 DATA TYPES ═══

1. NUMBER (integers and decimals)
   declare age = 25
   declare pi = 3.14159
   declare negative = -42
   declare scientific = 1.5e6      # 1,500,000
   declare big = 8000000000

2. STRING (text in quotes)
   declare name = "Alice"
   declare city = 'London'
   declare quote = "She said 'hi'"
   declare mixed = 'He said "hello"'

3. BOOLEAN (yes/no)
   declare isActive = yes
   declare isDeleted = no
   # Code uses yes/no. Display prints true/false or yes/no based on context.

4. ARRAY (ordered list)
   letarr nums = 1, 2, 3, 4, 5
   letarr colors = "red", "green", "blue"
   letarr empty = [ ]              # MUST use brackets for empty!

5. SET (unique items only)
   letset unique = 1, 2, 2, 3, 3, 4    # Auto-deduplicates to 1, 2, 3, 4

6. OBJECT (key-value pairs)
   letobj user:
       name: "Alice"
       age: 25
       isActive: yes

═══ VARIABLE OPERATIONS (COMPLETE) ═══

CREATE (first time only):
   declare x = 10
   make y = 20        # 'make' is 100% alias for 'declare'
   fix MAX = 100      # constant

MODIFY (must exist):
   set x = 15
   set y = y + 5

DELETE:
   del x              # removes from memory
   # If you try display(x) after this, program errors!

SWAP:
   declare a = 1
   declare b = 2
   swap a, b          # a is now 2, b is now 1

═══ ERROR MESSAGES (EXACT ENGINE OUTPUT) ═══

Redeclaration:
   "🌟 Variable 'x' is already declared. Use 'set x = ...' to change its value."

Set undeclared:
   "🌟 'x' was never declared. Use 'declare x = ...' first."

Modify constant:
   "🌟 'MAX' is FIXED!"

Delete non-existent:
   "🌟 Variable 'x' doesn't exist."

═══ TYPE CHECKING FUNCTIONS ═══

type(x)          → returns "number" | "string" | "boolean" | "array" | "object"
isNum(x)         → yes if number (not NaN)
isStr(x)         → yes if string
isBool(x)        → yes if boolean
isArr(x)         → yes if array
isObj(x)         → yes if object (not array)
isWhole(x)       → yes if integer (5, 10, -3)
isInteger(x)     → same as isWhole
isDecimal(x)     → yes if non-integer number (3.14)
isPositive(x)    → yes if x > 0
isNegative(x)    → yes if x < 0
isZero(x)        → yes if x === 0
len(x)           → length of string or array

EXAMPLES:
   display(type(42))             # number
   display(type("hi"))           # string
   display(type(yes))            # boolean
   display(isWhole(5))           # yes
   display(isWhole(5.5))         # no
   display(isDecimal(3.14))      # yes
   display(isPositive(-5))       # no
   display(len("Hello"))         # 5

═══ STRING INTERPOLATION ═══

Use {expression} inside strings:
   declare name = "Alice"
   declare age = 25
   display("Hello {name}, you are {age} years old!")
   display("Next year you'll be {age + 1}")

RULES:
- Works in both "..." and '...' strings
- Expression must start with letter, underscore, or (
- OR start with digit and contain operator (+, -, *, /)
- Expressions with : or ; are NOT interpolated

═══ STRING METHODS (COMPLETE LIST) ═══

Case:
   upper("hello")             → "HELLO"
   lower("WORLD")             → "world"
   sentence("hello world")    → "Hello world"
   capitalize("hello world")  → "Hello World"
   toggle("HeLLo")            → "hEllO"

Trimming & Length:
   trim("  hello  ")          → "hello"
   len("hello")               → 5
   wordCount("hi there world") → 3

Search:
   includes("hello world", "world")   → yes
   startsWith("hello", "he")          → yes
   endsWith("hello", "lo")            → yes
   charAt("hello", 0)                 → "h"
   pick("hello", 1)                   → "e"

Manipulation:
   replace("I love Python", "Python", "Littlestar")  → "I love Littlestar"
   split("a,b,c", ",")                → ["a", "b", "c"]
   reverse("hello")                    → "olleh"
   repeat("ab", 3)                     → "ababab"
   padLeft("5", 3, "0")                → "005"
   padRight("hi", 5, ".")              → "hi..."
   join(["a","b","c"], "-")            → "a-b-c"

═══ CONTAINS OPERATOR ═══

Works on both strings and arrays:
   when msg contains "World":
       display("Found!")

   letarr nums = 1, 2, 3
   when nums contains 2:
       display("2 is here!")

# Engine internally rewrites: `expr contains value` → `__ct(expr, value)`

═══ COMPLETE WORKING EXAMPLE ═══

module littlestar:

    spark main(1):
        declare name = "Alice"
        declare age = 25
        declare balance = 1234567.89
        
        display("=== User Profile ===")
        display("Name: {name}")
        display("Age: {age}")
        display("Type of age: " + type(age))
        display("Is age whole? " + isWhole(age))
        display("Balance: $" + comma(balance))
        
        set age = age + 1
        display("Next birthday you'll be {age}")

    spark print:
        main(1)
""",

    "COLLECTIONS": r"""
=== MODULE: ARRAYS, SETS & OBJECTS (COMPLETE REFERENCE) ===

═══ ARRAYS (letarr) ═══

CREATION:
   letarr nums = 1, 2, 3, 4, 5
   letarr names = "Alice", "Bob", "Charlie"
   letarr mixed = 1, "two", yes, 3.14
   letarr empty = [ ]           # MUST use brackets!

ACCESS (0-based indexing):
   letarr colors = "red", "green", "blue"
   display(colors[0])    # red
   display(colors[1])    # green
   display(colors[2])    # blue
   display(len(colors))  # 3

═══ MUTATING METHODS (modify original) ═══

add(arr, item)              → adds to END
   letarr nums = 1, 2, 3
   add(nums, 4)             # nums is now [1, 2, 3, 4]

addFirst(arr, item)         → adds to START
   addFirst(nums, 0)        # nums is now [0, 1, 2, 3, 4]

insertAt(arr, i, item)      → inserts at index i
   insertAt(nums, 2, 99)    # nums is now [0, 1, 99, 2, 3, 4]

remove(arr)                 → pops LAST item (NOT clear!)
   remove(nums)             # removes last element

removeFirst(arr)            → shifts first item
removeAt(arr, i)            → removes at index i
removeItem(arr, item)       → removes first match by value

pop(arr) / clear(arr)       → CLEARS ENTIRE ARRAY (sets length=0)
   # WARNING: This is different from Python's pop()!
   # To pop just the last item, use remove(arr)

═══ NON-MUTATING QUERY METHODS ═══

sort(arr)             → ascending copy
dsort(arr)            → descending copy
reverse(arr)          → reversed copy
unique(arr)           → duplicates removed
first(arr)            → arr[0]
last(arr)             → arr[length-1]
slice(arr, s, e)      → elements from index s to e-1 (end exclusive)
concat(a, b)          → new joined array
contains(arr, item)   → yes/no
indexOf(arr, item)    → index or -1 if not found
count(arr, item)      → occurrence count
join(arr, sep)        → string joined by separator
map(arr, fn)          → apply function to each element
filter(arr, fn)       → keep only matching elements
flatten(arr)          → one-level flatten
chunk(arr, n)         → split into groups of n
zip(a, b)             → pair elements

═══ STATISTICS ═══

sum(arr)              → total
avg(arr)              → mean
min(arr) / max(arr)   → smallest/largest
median(arr)           → middle value
mode(arr)             → most common
variance(arr)         → variance
stddev(arr)           → standard deviation
range(arr)            → max - min

# All accept EITHER single array OR multiple args:
sum(1, 2, 3)          → 6
sum([1, 2, 3])        → 6

═══ LOOPING THROUGH ARRAYS (CORRECT PATTERN) ═══

module littlestar:

    spark main(1):
        letarr fruits = "Apple", "Banana", "Cherry"
        declare i = 0
        
        while i < len(fruits):
            display((i + 1) + ". " + fruits[i])
            set i = i + 1
        
    spark print:
        main(1)

═══ SETS (letset) ═══

CREATION (auto-removes duplicates):
   letset unique = 1, 2, 2, 3, 3, 3, 4
   display(unique)          # Output: 1, 2, 3, 4

═══ mathset() OPERATIONS ═══

letset A = 1, 2, 3, 4
letset B = 3, 4, 5, 6

mathset("union", A, B)          → 1, 2, 3, 4, 5, 6
mathset("intersection", A, B)   → 3, 4
mathset("difference", A, B)     → 1, 2      (A - B)
mathset("symmetric", A, B)      → 1, 2, 5, 6

mathset("isSubset", A, B)       → no
mathset("isSuperset", A, B)     → no
mathset("isEqual", A, B)        → no
mathset("isDisjoint", A, B)     → no
mathset("cardinality", A)       → 4

mathset("powerset", A)          → all subsets of A
mathset("cartesian", A, B)      → all (a,b) pairs
mathset("isMember", A, 3)       → yes
mathset("add", A, 5)            → 1, 2, 3, 4, 5
mathset("remove", A, 2)         → 1, 3, 4

═══ SET SYMBOL CONSTANTS ═══

unionSymbol              # ∪
intersectionSymbol       # ∩
subsetSymbol             # ⊆
supersetSymbol           # ⊇
properSubsetSymbol       # ⊂
properSupersetSymbol     # ⊃
emptySetSymbol           # ∅
elementOfSymbol          # ∈
notElementOfSymbol       # ∉
universalSetSymbol       # 𝕌

═══ OBJECTS (letobj) ═══

CREATION (indented key: value pairs):
   letobj user:
       name: "Alice"
       age: 25
       email: "alice@example.com"
       isActive: yes

ACCESS (bracket notation with quoted key):
   display(user["name"])       # Alice
   display(user["age"])        # 25
   display(user)               # displays whole object

═══ CRITICAL RULE: letobj vs declare ═══

USE letobj ONLY to create NEW literal objects.
USE declare to extract existing objects/properties!

CORRECT:
   letobj user:
       address:
           city: "NYC"
   declare userCity = user["address"]

WRONG:
   letobj userCity = user["address"]    # ❌ SYNTAX ERROR!

═══ COMPLETE WORKING EXAMPLE ═══

module littlestar:

    spark main(1):
        letarr nums = 4, 8, 15, 16, 23, 42
        
        display("=== Array Analysis ===")
        display("Data: " + nums)
        display("Sum: " + sum(nums))
        display("Average: " + avg(nums))
        display("Median: " + median(nums))
        display("Min: " + min(nums))
        display("Max: " + max(nums))
        display("Sorted: " + sort(nums))
        
        letset A = 1, 2, 3, 4
        letset B = 3, 4, 5, 6
        display("Union: " + mathset("union", A, B))
        display("Intersection: " + mathset("intersection", A, B))
        
        letobj profile:
            name: "Bob"
            role: "Admin"
        display("Profile: " + profile)
        display("Name: " + profile["name"])

    spark print:
        main(1)
""",

    "CONTROL_FLOW": r"""
=== MODULE: CONTROL FLOW (when, match, while, for, repeat) COMPLETE ===

═══ CONDITIONALS (when / elif / otherwise) ═══

BASIC:
   when score >= 90:
       display("Grade A")
   elif score >= 80:
       display("Grade B")
   elif score >= 70:
       display("Grade C")
   otherwise:
       display("Failed")

RULES:
- NEVER use if/else (use when/otherwise)
- Logical: and (&&), or (||), not (!)
- Comparison: ==, !=, <>, <, >, <=, >=
- Blank lines between when/elif/otherwise are SAFE
- Nested conditions fully supported

MULTI-CONDITION:
   when age >= 18 and hasLicense:
       display("Can drive")
   elif age >= 16 or hasPermit:
       display("Learning to drive")
   otherwise:
       display("Cannot drive")

NEGATION:
   when not isRaining:
       display("Let's go outside!")

CONTAINS OPERATOR:
   declare msg = "Hello World"
   when msg contains "World":
       display("Found it!")
   
   letarr nums = 1, 2, 3
   when nums contains 2:
       display("2 is in the array!")

NESTED CONDITIONS:
   when isLoggedIn:
       when role == "admin":
           display("Admin panel")
       elif role == "editor":
           display("Editor panel")
       otherwise:
           display("User panel")
   otherwise:
       display("Please log in")

═══ MATCH/CASE ═══

BASIC:
   match role:
       case "Admin":
           display("Full access granted")
       case "Editor":
           display("Can edit posts")
       case "Viewer":
           display("Read-only access")
       default:
           display("Role not recognized")

MULTIPLE VALUES PER CASE:
   match day:
       case "Sat", "Sun":
           display("Weekend!")
       case "Mon", "Tue", "Wed", "Thu", "Fri":
           display("Work day")
       default:
           display("Invalid day")

RULES:
- Uses === strict comparison
- Once matched, subsequent cases skipped
- default is optional

═══ WHILE LOOP ═══

BASIC PATTERN:
   declare i = 1
   while i <= 5:
       display("Count: " + i)
       set i = i + 1

CRITICAL RULES:
- Counter MUST be declared OUTSIDE with declare
- Counter MUST be updated with set INSIDE the loop
- Max 10,000 iterations (auto-stop protection)
- Error: "🌟 Loop ran too many times."

═══ SKIP SAFETY (CRITICAL!) ═══

CORRECT (counter update BEFORE skip):
   declare i = 0
   while i < 5:
       set i = i + 1          # UPDATE FIRST!
       when i == 3:
           skip               # 3 is skipped
       display(i)

Output: 1, 2, 4, 5

WRONG (counter update AFTER skip):
   declare i = 0
   while i < 5:
       when i == 3:
           skip               # Never reaches counter update!
       set i = i + 1
       display(i)

Engine detects and throws:
"🌟 Infinite loop detected — 'skip' was called but no variables changed. 
 Hint: Move 'set var = var + 1' BEFORE the 'skip' statement."

═══ FOR LOOP (as / till) ═══

ASCENDING:
   as i in 1 till 10:
       display(i)             # prints 1, 2, 3, ..., 10

DESCENDING:
   as n in 10 till 1:
       display(n)             # prints 10, 9, 8, ..., 1

FEATURES:
- Auto-detects direction based on start/end
- Loop variable auto-created and cleaned up
- Max 10,000 iterations
- Start/end auto-rounded to integers

═══ REPEAT LOOP ═══

FIXED TIMES:
   repeat this(5):
       display("Hello! 🌟")

DEFAULT (once):
   repeat this:
       display("Once")

WITH COUNTER:
   declare count = 0
   repeat this(3):
       set count = count + 1
       display("Iteration " + count)

NOTES:
- Supports stop (break)
- Does NOT support skip (continue)

═══ LOOP CONTROLS ═══

stop → breaks out of loop completely
skip → continues to next iteration

STOP EXAMPLE:
   declare i = 0
   while i < 100:
       set i = i + 1
       when i == 4:
           display("Found 4, stopping!")
           stop
       display("Checking: " + i)

Output:
   Checking: 1
   Checking: 2
   Checking: 3
   Found 4, stopping!

═══ COMPLETE WORKING EXAMPLES ═══

FizzBuzz:
module littlestar:
    spark main(1):
        declare i = 1
        while i <= 20:
            when i mod 15 == 0:
                display("FizzBuzz")
            elif i mod 3 == 0:
                display("Fizz")
            elif i mod 5 == 0:
                display("Buzz")
            otherwise:
                display(i)
            set i = i + 1
    spark print:
        main(1)

Grade Calculator:
module littlestar:
    spark main(1):
        declare score = 85
        match yes:
            case (score >= 90):
                display("Grade A")
            case (score >= 80):
                display("Grade B")
            case (score >= 70):
                display("Grade C")
            default:
                display("Grade F")
    spark print:
        main(1)

Countdown:
module littlestar:
    spark main(1):
        as t in 5 till 1:
            display(t + "...")
        display("🚀 Blast off!")
    spark print:
        main(1)
""",

    "FUNCTIONS_MODULES": r"""
=== MODULE: FUNCTIONS, SCOPE, RECURSION & IMPORTS (COMPLETE) ===

═══ FUNCTION PLACEMENT (CRITICAL RULE!) ═══

Functions MUST be defined at the VERY TOP of `spark main(N):` block, 
BEFORE any other executable statements!

CORRECT:
module littlestar:
    spark main(1):
        # 1. DEFINE ALL FUNCTIONS FIRST
        func greet(name):
            display("Hello, " + name + "!")
        
        func add(a, b):
            return a + b
        
        # 2. THEN RUN CODE
        greet("Alice")
        declare sum = add(3, 4)
        display("Sum: " + sum)
    spark print:
        main(1)

═══ FUNCTION TYPES ═══

Basic:
   func sayHello():
       display("Hello!")

With Parameters:
   func greet(name):
       display("Hi, " + name)

With Return:
   func square(n):
       return n * n

Private (cannot be imported):
   private func secret():
       display("Only local")

Exported (can be imported by other files):
   export func triple(n):
       return n * 3

═══ SCOPE ISOLATION ═══

Variables inside functions are ISOLATED from outer scope:

   declare score = 10
   
   func changeScore():
       declare score = 999
       display("Inside: " + score)      # 999
   
   changeScore()
   display("Outside: " + score)         # 10

═══ RETURN VALUES ═══

Simple return:
   func calculate():
       return 42

Multiple conditions:
   func grade(score):
       when score >= 90:
           return "A"
       elif score >= 80:
           return "B"
       elif score >= 70:
           return "C"
       return "F"

═══ RECURSION ═══

Factorial:
   func factorial(n):
       when n <= 1:
           return 1
       return n * factorial(n - 1)
   
   display(factorial(5))        # 120

Fibonacci:
   func fib(n):
       when n <= 1:
           return n
       return fib(n - 1) + fib(n - 2)

═══ MODULE IMPORTS ═══

FILE 1 — math_utils.lstar:
module littlestar:
    spark main(1):
        export func triple(n):
            return n * 3
        
        export func double(n):
            return n * 2
        
        export func square(n):
            return n * n
    spark print:
        main(1)

FILE 2 — main.lstar (imports from math_utils):
module littlestar:
    spark main(1):
        import triple from math_utils
        import double from math_utils
        import square from math_utils
        
        display("Triple of 5: " + triple(5))
        display("Double of 5: " + double(5))
        display("Square of 5: " + square(5))
    spark print:
        main(1)

═══ IMPORT RULES ═══
- One import per line
- NO .lstar extension (engine strips it)
- Only export func can be imported
- private func cannot be imported (only local use)
- Both files must be open as tabs in Playground

═══ LION BLOCKS (Rare) ═══

Alternative grouping construct:
   export lion myGroup:
       display("Line 1")
       display("Line 2")
       display("Line 3")

═══ COMPLETE WORKING EXAMPLES ═══

Tip Calculator:
module littlestar:
    spark main(1):
        func calcTip(bill, percent):
            return bill * percent / 100
        
        func total(bill, tipAmount):
            return bill + tipAmount
        
        declare mealCost = 85.50
        declare tipPercent = 18
        
        declare tip = calcTip(mealCost, tipPercent)
        declare finalTotal = total(mealCost, tip)
        
        display("Bill: $" + mealCost)
        display("Tip (" + tipPercent + "%): $" + decimals(tip, 2))
        display("Total: $" + decimals(finalTotal, 2))
    spark print:
        main(1)

BMI Calculator:
module littlestar:
    spark main(1):
        func calcBMI(weight, height):
            return weight / (height * height)
        
        func classify(bmi):
            when bmi < 18.5:
                return "Underweight"
            elif bmi < 25:
                return "Normal"
            elif bmi < 30:
                return "Overweight"
            return "Obese"
        
        declare w = 70
        declare h = 1.75
        declare myBMI = calcBMI(w, h)
        
        display("BMI: " + decimals(myBMI, 2))
        display("Category: " + classify(myBMI))
    spark print:
        main(1)
""",

    "DATABASE": r"""
=== MODULE: DECLARATIVE DATABASE (COMPLETE REFERENCE) ===

═══ DATABASE STRUCTURE ═══

Databases are defined in a SEPARATE module at the BOTTOM of your file:

module littlestar:
    spark main(1):
        # Your main code here
    spark print:
        main(1)

module littlestardb:              # ← Database module (at bottom)
    createdb student:
        s1:
            name: 'Alice'
            age: 20
            major: 'CS'
        s2:
            name: 'Bob'
            age: 22
            major: 'Physics'

═══ PARSING RULES (parseDbs) ═══

- Everything after `module littlestardb:` is parsed as database
- `createdb name:` starts a new database
- Record IDs (s1:, s2:, etc.) with no value start new records
- Key-value lines (key: value) added to current record
- String values with quotes are auto-unquoted
- Number values converted to Number type
- yes/no converted to true/false
- Trailing commas stripped

═══ FETCHING DATA (NO QUOTES ON DB NAMES!) ═══

Get ALL records:
   letarr all = fetch(student)     # Array of objects

Get SPECIFIC record (1-based):
   letobj bob = fetch(student.2)   # Second record

Engine auto-quotes bare identifiers in fetch(), countdb(), hasdb().

═══ UTILITY FUNCTIONS ═══

countdb(dbName)   → number of records
hasdb(dbName)     → yes/no (exists check)
listdbs()         → array of all database names

Examples:
   display("Total students: " + countdb(student))
   when hasdb(student):
       display("Database exists")
   display("All DBs: " + listdbs())

═══ FILTERING & QUERIES ═══

Loop through records to filter:
   letarr prods = fetch(product)
   declare i = 0
   declare price = 0
   
   while i < len(prods):
       set price = prods[i]["price"]
       when price > 500:
           display(prods[i]["name"] + ": $" + price)
       set i = i + 1

═══ EXPORT DATABASE ═══

Save to file (downloads to user's computer):
   save student to "students_backup.txt"

Engine formats each record as key: value pairs.

═══ REMOVE DATABASE ═══

   removedb student
   # Throws error if db doesn't exist

═══ COMPLETE WORKING EXAMPLES ═══

Student Roster:
module littlestar:
    spark main(1):
        letarr students = fetch(student)
        
        display("=== Student Roster ===")
        display("Total: " + countdb(student))
        lbr
        
        declare i = 0
        while i < len(students):
            display((i + 1) + ". " + students[i]["name"])
            display("   Age: " + students[i]["age"])
            display("   Major: " + students[i]["major"])
            lbr
            set i = i + 1
    spark print:
        main(1)

module littlestardb:
    createdb student:
        s1:
            name: 'Alice'
            age: 20
            major: 'Computer Science'
        s2:
            name: 'Bob'
            age: 22
            major: 'Physics'
        s3:
            name: 'Charlie'
            age: 21
            major: 'Mathematics'

Inventory Report:
module littlestar:
    spark main(1):
        letarr inventory = fetch(item)
        declare totalValue = 0
        declare i = 0
        
        display("╔══════════════════════════╗")
        display("║  📦 INVENTORY REPORT    ║")
        display("╚══════════════════════════╝")
        
        declare price = 0
        declare qty = 0
        declare itemTotal = 0
        
        while i < len(inventory):
            set price = inventory[i]["price"]
            set qty = inventory[i]["qty"]
            set itemTotal = price * qty
            
            display(inventory[i]["name"] + ": $" + itemTotal)
            
            set totalValue = totalValue + itemTotal
            set i = i + 1
        
        lbr
        display("TOTAL: $" + comma(totalValue))
    spark print:
        main(1)

module littlestardb:
    createdb item:
        i1:
            name: 'Monitors'
            price: 200
            qty: 5
        i2:
            name: 'Desks'
            price: 150
            qty: 10
        i3:
            name: 'Chairs'
            price: 100
            qty: 12

Filter Products by Price:
module littlestar:
    spark main(1):
        letarr prods = fetch(product)
        declare i = 0
        
        display("=== Expensive Products ($500+) ===")
        
        while i < len(prods):
            when prods[i]["price"] > 500:
                display("- " + prods[i]["name"] + " ($" + prods[i]["price"] + ")")
            set i = i + 1
    spark print:
        main(1)

module littlestardb:
    createdb product:
        p1:
            name: 'Laptop'
            price: 999
        p2:
            name: 'Mouse'
            price: 25
        p3:
            name: 'Monitor'
            price: 600
        p4:
            name: 'Keyboard'
            price: 150
""",

    "WEB": r"""
=== MODULE: WEB BLOCKS & HTML5 RENDERING (COMPLETE) ===

═══ CRITICAL RULE ═══

Every `web:` block MUST contain a 100% COMPLETE HTML5 document:
- <!DOCTYPE html>
- <html>
- <head>
- <body>

Engine validates presence of "<!doctype html>" (case-insensitive).
Missing DOCTYPE throws: "🌟 web: block must be a complete HTML5 document."

═══ BASIC WEB BLOCK ═══

module littlestar:
    spark main(1):
        web:
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>My First Web Page</title>
                <style>
                    body {
                        background: #0f0f1e;
                        color: white;
                        font-family: sans-serif;
                        padding: 20px;
                    }
                    h1 { color: gold; }
                </style>
            </head>
            <body>
                <h1>🌟 Hello from Littlestar!</h1>
                <p>This is web output.</p>
            </body>
            </html>
    spark print:
        main(1)

═══ VARIABLE INTERPOLATION ═══

Use {variableName} or {expression} inside web blocks:

module littlestar:
    spark main(1):
        declare title = "Profile Card"
        declare name = "Alice"
        declare age = 25
        declare color = "#facc15"
        
        web:
            <!DOCTYPE html>
            <html>
            <head>
                <title>{title}</title>
                <style>
                    body {
                        background: #1a1a2e;
                        color: white;
                        padding: 40px;
                        font-family: sans-serif;
                    }
                    .card {
                        background: rgba(255,255,255,0.05);
                        border: 2px solid {color};
                        border-radius: 12px;
                        padding: 24px;
                        max-width: 300px;
                    }
                    h2 { color: {color}; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h2>{name}</h2>
                    <p>Age: {age}</p>
                    <p>Next year: {age + 1}</p>
                </div>
            </body>
            </html>
    spark print:
        main(1)

═══ ENGINE BEHAVIOR ═══

1. Collects all indented lines after `web:`
2. Determines base indentation from first non-empty line
3. Calculates relative indentation per line
4. Processes {expr} interpolation via this.eval()
5. If eval fails on {expr}, leaves it unchanged
6. Validates htmlContent.toLowerCase() contains "<!doctype html>"
7. Stores in this.web.html and emits web callback
8. Playground renders it in an iframe via srcdoc
9. <base target="_blank"> auto-injected so links open in new tabs

═══ DYNAMIC HTML BUILDING ═══

Combine loops with web blocks by building HTML strings first:

module littlestar:
    spark main(1):
        letarr items = "Apple", "Banana", "Cherry"
        declare listHtml = ""
        declare i = 0
        
        while i < len(items):
            set listHtml = listHtml + "<li>" + items[i] + "</li>"
            set i = i + 1
        
        web:
            <!DOCTYPE html>
            <html>
            <head>
                <title>Shopping List</title>
                <style>
                    body { background: #0f0f1e; color: white; padding: 20px; font-family: sans-serif; }
                    ul { list-style: none; padding: 0; }
                    li { padding: 8px; margin: 4px 0; background: #1a1a2e; border-radius: 4px; }
                </style>
            </head>
            <body>
                <h1>🛒 Shopping List</h1>
                <ul>{listHtml}</ul>
            </body>
            </html>
    spark print:
        main(1)

═══ COMPLETE STYLED EXAMPLES ═══

Profile Card:
module littlestar:
    spark main(1):
        declare name = "Godspower"
        declare role = "Creator of Littlestar"
        declare email = "creator@littlestar.com"
        
        web:
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Profile: {name}</title>
                <style>
                    * { margin: 0; padding: 0; box-sizing: border-box; }
                    body {
                        min-height: 100vh;
                        background: linear-gradient(135deg, #0f0f1e, #1a1a2e);
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        font-family: sans-serif;
                        color: white;
                    }
                    .card {
                        background: rgba(255, 255, 255, 0.05);
                        backdrop-filter: blur(10px);
                        border: 1px solid rgba(250, 204, 21, 0.3);
                        border-radius: 20px;
                        padding: 40px;
                        max-width: 400px;
                        text-align: center;
                        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
                    }
                    .avatar {
                        width: 100px;
                        height: 100px;
                        border-radius: 50%;
                        background: linear-gradient(135deg, #facc15, #f472b6);
                        margin: 0 auto 20px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 48px;
                    }
                    h1 { color: #facc15; margin-bottom: 10px; }
                    .role { color: #f472b6; margin-bottom: 15px; }
                    .email { color: #9ca3af; font-size: 14px; }
                </style>
            </head>
            <body>
                <div class="card">
                    <div class="avatar">🌟</div>
                    <h1>{name}</h1>
                    <p class="role">{role}</p>
                    <p class="email">{email}</p>
                </div>
            </body>
            </html>
    spark print:
        main(1)

Dashboard with Data:
module littlestar:
    spark main(1):
        declare totalUsers = 1250
        declare totalRevenue = 45680
        declare activeProjects = 12
        
        web:
            <!DOCTYPE html>
            <html>
            <head>
                <title>Dashboard</title>
                <style>
                    body { background: #0f0f1e; color: white; padding: 20px; font-family: sans-serif; }
                    h1 { color: #facc15; margin-bottom: 30px; }
                    .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
                    .stat {
                        background: rgba(250, 204, 21, 0.1);
                        border: 1px solid rgba(250, 204, 21, 0.3);
                        border-radius: 12px;
                        padding: 24px;
                        text-align: center;
                    }
                    .stat h2 { color: #facc15; font-size: 2rem; }
                    .stat p { color: #9ca3af; margin-top: 8px; }
                </style>
            </head>
            <body>
                <h1>📊 Analytics Dashboard</h1>
                <div class="stats">
                    <div class="stat">
                        <h2>{totalUsers}</h2>
                        <p>Total Users</p>
                    </div>
                    <div class="stat">
                        <h2>${totalRevenue}</h2>
                        <p>Revenue</p>
                    </div>
                    <div class="stat">
                        <h2>{activeProjects}</h2>
                        <p>Active Projects</p>
                    </div>
                </div>
            </body>
            </html>
    spark print:
        main(1)
""",

    "MATH_EQUATIONS_GEOMETRY": r"""
=== MODULE: ADVANCED MATH, EQUATIONS & GEOMETRY (COMPLETE) ===

═══ BASIC MATH FUNCTIONS ═══

sqrt(x)           → square root (negatives return "2i" notation)
   sqrt(9) → 3
   sqrt(-4) → "2i"
   sqrt(-1) → "i"

square(x)         → x²
cbrt(x)           → cube root
cube(x)           → x³
pow(x, y)         → x^y
abs(x)            → absolute value
floor(x)          → round down
ceil(x)           → round up
sign(x)           → -1, 0, or 1
exp(x)            → e^x

Rounding:
round(n, d=0)     → round to d decimal places
decimals(n, d)    → fixed decimal places
   round(3.14159, 2) → 3.14
   decimals(3.14159, 3) → 3.142

Min/Max (accept array OR multiple args):
   min(1, 2, 3) → 1
   max([5, 10, 15]) → 15

Advanced:
clamp(n, lo, hi)      → constrain to range
nthroot(x, n)         → nth root (handles negatives)
mod(a, b)             → modulo (always positive)
percent(a, b)         → (a/100)*b
distance(x1,y1,x2,y2) → Euclidean distance
fraction(d)           → convert decimal to fraction string

═══ LOGARITHMS ═══

log(n)            → natural log (Math.log)
log(n, base)      → log base b
ln(n)             → natural log
log10(n)          → log base 10
log2(n)           → log base 2
logbase(n, b)     → log base b
antilog(n, b=10)  → b^n

═══ TRIGONOMETRY (Degrees by default) ═══

sin(d), cos(d), tan(d)              → degree input
asin(n), acos(n), atan(n)           → returns degrees
radsin(r), radcos(r), radtan(r)     → radian input
gradsin(g), gradcos(g), gradtan(g)  → gradian input
sinh, cosh, tanh                    → hyperbolic
degrad(d)                           → degrees to radians
raddeg(r)                           → radians to degrees

═══ NUMBER THEORY ═══

factorial(n)                → n!
   factorial(5) → 120

facsum(n)                   → 1+2+...+n
facsq(n)                    → 1²+2²+...+n²
faccube(n)                  → 1³+2³+...+n³

fibonacci(n)                → nth Fibonacci
   fibonacci(10) → 55

isPrime(n)                  → yes/no
primes(n)                   → array of first n primes
   primes(5) → [2, 3, 5, 7, 11]

isEven(n), isOdd(n)         → yes/no
evens(n)                    → first n even numbers
odds(n)                     → first n odd numbers
evensBetween(a, b)          → even numbers in range
oddsBetween(a, b)           → odd numbers in range

gcd(...args)                → greatest common divisor
lcm(...args)                → least common multiple
hcf(...args)                → same as gcd

═══ EQUATION SOLVERS ═══

Linear equation:
   solve("2x + 5 = 15")     → "x = 5"

Quadratic equation:
   solve("x^2 - 5x + 6 = 0")  → "x = 2 or x = 3"

Complex roots supported:
   solve("x^2 + 4 = 0")     → "x = 2i or x = -2i"

Quadratic formula:
   quadratic(1, -5, 6)      → [3, 2]
   quadratic(1, 0, -4)      → [2, -2]
   quadratic(1, 0, 4)       → [2i, -2i]

Simultaneous linear:
   simultaneousLinear("2x + 3y = 12", "x - y = 1")
   → {x: 3, y: 2}

═══ GEOMETRY (NO QUOTES ON SHAPE NAMES!) ═══

AREA:
area(circle, r)              → πr²
area(square, s)              → s²
area(rectangle, w, h)        → w*h
area(triangle, b, h)         → 0.5*b*h
area(trapezoid, a, b, h)     → 0.5*(a+b)*h
area(parallelogram, b, h)    → b*h
area(rhombus, d1, d2)        → 0.5*d1*d2
area(ellipse, a, b)          → π*a*b
area(pentagon, side)         → pentagon formula
area(hexagon, side)          → hexagon formula

Examples:
   area(circle, 5)          → 78.54 (π*25)
   area(rectangle, 4, 6)    → 24
   area(triangle, 3, 4)     → 6

PERIMETER:
perimeter(circle, r)              → 2πr
perimeter(square, s)              → 4s
perimeter(rectangle, w, h)        → 2*(w+h)
perimeter(triangle, a, b, c)      → a+b+c
perimeter(trapezoid, a, b, c, d)  → a+b+c+d
perimeter(pentagon, side)         → 5*side
perimeter(hexagon, side)          → 6*side

VOLUME:
volume(cube, s)              → s³
volume(sphere, r)            → (4/3)πr³
volume(cylinder, r, h)       → πr²h
volume(cone, r, h)           → (1/3)πr²h
volume(pyramid, l, w, h)     → (1/3)*l*w*h
volume(cuboid, l, w, h)      → l*w*h
volume(prism, baseArea, h)   → baseArea*h
volume(hemisphere, r)        → (2/3)πr³
volume(ellipsoid, a, b, c)   → (4/3)π*a*b*c

Examples:
   volume(cube, 3)          → 27
   volume(sphere, 3)        → 113.10
   volume(cylinder, 2, 5)   → 62.83

═══ MATH CONSTANTS ═══

pi, e, tau (2π), phi (golden ratio)
inf, ninf, nan
sqrt2, sqrt3
ln2, ln10, log2e, log10e

═══ RANDOM ═══

random()                    → 0..1
randInt(a, b)               → random integer in [a, b] inclusive
randText(n=5)               → random alphanumeric string
randomChoice(arr)           → random element from array

═══ CONVERSION ═══

toNum(x)                    → parseFloat
toInt(x)                    → parseInt (accepts base too: toInt("FF", 16))
toStr(x)                    → String()

═══ COMPLETE WORKING EXAMPLES ═══

Calculator:
module littlestar:
    spark main(1):
        declare a = 15
        declare b = 4
        
        display("=== Calculator ===")
        display(a + " + " + b + " = " + (a + b))
        display(a + " - " + b + " = " + (a - b))
        display(a + " * " + b + " = " + (a * b))
        display(a + " / " + b + " = " + decimals(a / b, 2))
        display(a + " mod " + b + " = " + mod(a, b))
        display(a + "^" + b + " = " + pow(a, b))
    spark print:
        main(1)

Equation Solver:
module littlestar:
    spark main(1):
        display("Linear: " + solve("2x + 5 = 15"))
        display("Quadratic: " + solve("x^2 - 5x + 6 = 0"))
        display("Complex: " + solve("x^2 + 4 = 0"))
        
        declare sys = simultaneousLinear("2x + 3y = 12", "x - y = 1")
        display("System: x = " + sys["x"] + ", y = " + sys["y"])
    spark print:
        main(1)

Geometry Report:
module littlestar:
    spark main(1):
        display("=== Areas ===")
        display("Circle (r=5): " + decimals(area(circle, 5), 2))
        display("Rectangle (4×6): " + area(rectangle, 4, 6))
        display("Triangle (b=3, h=4): " + area(triangle, 3, 4))
        display("Hexagon (s=3): " + decimals(area(hexagon, 3), 2))
        
        lbr
        display("=== Volumes ===")
        display("Cube (s=3): " + volume(cube, 3))
        display("Sphere (r=3): " + decimals(volume(sphere, 3), 2))
        display("Cylinder (r=2, h=5): " + decimals(volume(cylinder, 2, 5), 2))
    spark print:
        main(1)
""",

    "HTTP_JSON_FILES": r"""
=== MODULE: HTTP, JSON, FILE I/O & ERROR HANDLING (COMPLETE) ===

═══ HTTP REQUESTS (CRITICAL RULES) ═══

- HTTP functions ONLY work in async execLine (not inside eval)
- MUST match pattern: `declare varName = httpMethod(args)`
- Methods: httpGet, httpPost, httpPut, httpDelete
- ALWAYS wrap in compile:/otherwise: for safety!

═══ httpGet USAGE ═══

Basic:
   compile:
       declare raw = httpGet("https://jsonplaceholder.typicode.com/users/1")
       declare user = jsonParse(raw)
       display("Name: " + user["name"])
       display("Email: " + user["email"])
   otherwise:
       display("Network failed!")

With Authorization:
   declare data = httpGet("https://api.example.com", "Bearer YOUR_TOKEN")

═══ httpPost USAGE ═══

Basic:
   declare body = jsonStringify(myObject)
   declare result = httpPost("https://api.example.com/data", body)

Options:
- Second arg: body
- Third arg: Authorization header (optional)
- If body starts with '{', Content-Type auto-set to application/json

Example:
   letobj payload:
       name: "Alice"
       age: 30
   
   compile:
       declare body = jsonStringify(payload)
       declare response = httpPost("https://api.example.com/users", body)
       display("Server response: " + response)
   otherwise:
       display("Post failed!")

═══ Other HTTP Methods ═══

httpPut(url, body)     → update resource
httpDelete(url)        → delete resource

═══ JSON HANDLING ═══

jsonParse(str)         → object (or null on failure)
jsonStringify(obj)     → string (or "" on failure)

Examples:
   declare jsonStr = '{"name":"Alice","age":25}'
   declare obj = jsonParse(jsonStr)
   display(obj["name"])         # Alice
   
   letobj user:
       name: "Bob"
       age: 30
   
   declare str = jsonStringify(user)
   display(str)                 # {"name":"Bob","age":30}

═══ ERROR HANDLING (compile / otherwise) ═══

Basic:
   compile:
       declare x = someRiskyOperation()
       display(x)
   otherwise:
       display("Something failed!")

WHAT THROWS (triggers otherwise):
- Accessing undeclared variable
- set on undeclared variable
- declare on already-declared variable
- set on fix constant
- assert(false condition)
- Infinite loop protection
- Invalid web: block (missing doctype)
- Missing modules on import
- readNum with non-number input
- HTTP fetch failures
- del on non-existent variable

WHAT DOES NOT THROW:
- toNum("bad") → returns NaN silently
- jsonParse(invalid) → returns null silently
- jsonStringify() failure → returns "" silently

═══ ASSERTIONS ═══

assert(condition)     → throws if false

Examples:
   assert(age > 0)
   assert(len(name) > 0)
   assert(isNum(x))

Error: "🌟 Assertion failed" (with condition text as hint)

═══ FILE SYSTEM (browser localStorage) ═══

All files stored with prefix "lstar_file_"

write(filename, content)       → creates/overwrites
   write("notes.txt", "Hello World")

read(filename)                 → returns "" if not found
   declare content = read("notes.txt")

append(filename, content)      → appends or creates
   append("notes.txt", "\nNew line")

exists(filename)               → yes/no
   when exists("notes.txt"):
       display("File found!")

delete file filename           → removes; warns if not found
   delete file notes.txt

═══ CREATOR MODE FILE OPS ═══

Requires: enable creator

exportfile filename           → triggers browser download
   enable creator
   exportfile notes.txt

savefile filename             → confirms exists in memory
   savefile notes.txt

═══ COMPLETE WORKING EXAMPLES ═══

Fetch User Data from API:
module littlestar:
    spark main(1):
        compile:
            declare raw = httpGet("https://jsonplaceholder.typicode.com/users/1")
            declare user = jsonParse(raw)
            
            display("=== User Info ===")
            display("Name: " + user["name"])
            display("Email: " + user["email"])
            display("Phone: " + user["phone"])
            
            declare address = user["address"]
            display("City: " + address["city"])
            display("Street: " + address["street"])
        otherwise:
            display("Failed to fetch user data!")
    spark print:
        main(1)

Post Data to API:
module littlestar:
    spark main(1):
        letobj newPost:
            title: "My First Post"
            body: "Hello from Littlestar!"
            userId: 1
        
        compile:
            declare payload = jsonStringify(newPost)
            declare result = httpPost("https://jsonplaceholder.typicode.com/posts", payload)
            display("Created: " + result)
        otherwise:
            display("Post failed!")
    spark print:
        main(1)

Notes App:
module littlestar:
    spark main(1):
        declare note = "My first note!"
        write("notes.txt", note)
        
        when exists("notes.txt"):
            display("File saved!")
            declare content = read("notes.txt")
            display("Content: " + content)
        
        append("notes.txt", "\n(added another note)")
        display("Updated: " + read("notes.txt"))
    spark print:
        main(1)

Error Handling:
module littlestar:
    spark main(1):
        declare age = -5
        
        compile:
            assert(age > 0)
            display("Age is valid: " + age)
        otherwise:
            display("Error: Age must be positive!")
    spark print:
        main(1)
""",

    "UTILITIES_CURRENCY_UNITS": r"""
=== MODULE: CURRENCY, UNITS & UTILITIES (COMPLETE) ===

═══ LIVE CURRENCY CONVERSION ═══

Engine fetches LIVE rates from a real API, cached 1 hour.
Falls back to hardcoded rates if API fails.

USAGE (NO QUOTES ON CURRENCY CODES!):
   convertCurrency(100, USD, EUR)
   convertCurrency(50, GBP, NGN)
   convertCurrency(1000, USD, JPY)

Formula: (value / fromRate) * toRate (relative to USD)

Engine auto-quotes currency codes at positions 2 and 3.

SUPPORTED CURRENCIES (150+):
USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, INR, NGN, 
BRL, ZAR, MXN, KRW, and many more.

═══ UNIT CONVERSION ═══

USAGE (NO QUOTES ON UNIT NAMES!):
   convert(5, meter, cm)     → 500
   convert(10, mile, meter)  → 16093.44
   convert(150, lb, kg)      → 68.04
   convert(2, hour, min)     → 120
   convert(5, GB, MB)        → 5120

Formula: val * fromFactor / toFactor

═══ UNIT CATEGORIES ═══

LENGTH: meter, cm, mm, inch, ft, yard, mile, pc, au
MASS:   kg, g, mg, lb, oz, ton
TIME:   s, ms, min, hour, day, week, year, decade, century, millennium
DATA:   B, KB, MB, GB, TB, PB
VOLUME: L, mL, gallon, quart, pint, cup
SPEED:  m/s, km/h, mph, fps
ANGLE:  deg, rad

═══ STRING PADDING (for aligned output) ═══

padLeft(s, width, ch=" ")      → pad start
padRight(s, width, ch=" ")     → pad end

Examples:
   padRight("ITEM", 15, " ") + padLeft("$99", 10, ".")
   → "ITEM           ......$99"

═══ NUMBER SYSTEM CONVERSIONS ═══

bin(255)      → "11111111"
oct(255)      → "377"
hex(255)      → "FF" (uppercase)
toInt("FF", 16)      → 255
toInt("11111111", 2) → 255

═══ FORMATTING ═══

comma(1234567)     → "1,234,567" (thousands separator)
toStr(x), toNum(x), toInt(x)

═══ SECURITY / HASHING ═══

hash("text")       → simple hex hash string (Java-style hashCode)

═══ DATE / TIME ═══

datenow()          → locale date string
timenow()          → locale time string
yearnow()          → e.g. 2025
monthnow()         → 1-12
daynow()           → 1-31
hournow()          → 0-23
minutenow()        → 0-59
secondnow()        → 0-59
weekdayNow()       → "Monday" etc.
months()           → array of 12 month names
days()             → array of 7 weekday names (Sunday first)
timestamp()        → Date.now() milliseconds
elapsed(startTs)   → ms since startTs

FORMAT DATE:
format(date, "YYYY-MM-DD HH:mm:ss")
Patterns: YYYY, MMMM, MMM, MM, DD, dddd, dd, HH, mm, ss

═══ ASYNC SLEEP ═══

sleep(ms)          → pause execution (non-blocking)

Only works in async context.

═══ TIME CONSTANTS ═══

yeardays (365.25), weekdays (7), hoursec (3600),
daysec (86400), yearsec (31557600)

═══ PHYSICS CONSTANTS ═══

c (299792458 m/s), g (9.80665 m/s²)
avogadro (6.022e23), planck (6.626e-34), boltzmann (1.381e-23)
earthmass, sunmass, au, lightyear, parsec

═══ COMPLETE WORKING EXAMPLES ═══

Currency Converter:
module littlestar:
    spark main(1):
        declare amount = 100
        
        display("💱 Live Currency Rates")
        display(amount + " USD = " + decimals(convertCurrency(amount, USD, EUR), 2) + " EUR")
        display(amount + " USD = " + decimals(convertCurrency(amount, USD, GBP), 2) + " GBP")
        display(amount + " USD = " + decimals(convertCurrency(amount, USD, JPY), 2) + " JPY")
        display(amount + " USD = " + decimals(convertCurrency(amount, USD, NGN), 2) + " NGN")
    spark print:
        main(1)

Unit Converter:
module littlestar:
    spark main(1):
        display("=== Length ===")
        display("5 km = " + convert(5, meter, cm) + " cm")
        display("10 miles = " + decimals(convert(10, mile, meter), 2) + " m")
        
        lbr
        display("=== Weight ===")
        display("150 lb = " + decimals(convert(150, lb, kg), 2) + " kg")
        
        lbr
        display("=== Time ===")
        display("2 hours = " + convert(2, hour, min) + " min")
        display("1 day = " + convert(1, day, hour) + " hours")
    spark print:
        main(1)

Countdown Timer:
module littlestar:
    spark main(1):
        declare t = 5
        
        while t > 0:
            display(t + "...")
            sleep(1000)
            set t = t - 1
        
        glow("🚀 Blast off!")
    spark print:
        main(1)

Date & Time:
module littlestar:
    spark main(1):
        display("Date: " + datenow())
        display("Time: " + timenow())
        display("Year: " + yearnow())
        display("Month: " + monthnow())
        display("Day: " + daynow())
        display("Weekday: " + weekdayNow())
    spark print:
        main(1)

Password Hash:
module littlestar:
    spark main(1):
        declare password = "mySecret123"
        declare hashed = hash(password)
        
        display("Original: " + password)
        display("Hashed:   " + hashed)
        display("Length:   " + len(hashed))
    spark print:
        main(1)

Number Systems:
module littlestar:
    spark main(1):
        declare n = 255
        
        display("Decimal: " + n)
        display("Binary:  " + bin(n))
        display("Octal:   " + oct(n))
        display("Hex:     " + hex(n))
        
        display("Back to decimal: " + toInt("FF", 16))
    spark print:
        main(1)
"""
}

# ═══════════════════════════════════════════════════════════════════
# ROUTING KEYWORD MAPPER
# ═══════════════════════════════════════════════════════════════════
MODULE_TRIGGERS = {
    "VARIABLES_TYPES": [
        "declare", "make", "set", "fix", "del", "swap", "type", 
        "isnum", "isstr", "isbool", "isarr", "isobj", "iswhole", 
        "isinteger", "isdecimal", "ispositive", "isnegative", "iszero",
        "variable", "constant", "boolean", "number", "string", "typeof",
        "yes", "no", "true", "false", "interpolation", "contains",
        "upper", "lower", "trim", "replace", "split", "join", "capitalize",
        "sentence", "toggle", "startswith", "endswith", "charat", "pick"
    ],
    "COLLECTIONS": [
        "letarr", "letset", "letobj", "array", "set", "object", "list",
        "add", "addfirst", "insertat", "remove", "removefirst", "removeat",
        "removeitem", "pop", "clear", "sort", "dsort", "reverse", "unique",
        "first", "last", "slice", "concat", "indexof", "count", "map",
        "filter", "flatten", "chunk", "zip", "sum", "avg", "min", "max",
        "median", "mode", "variance", "stddev", "range", "mathset",
        "union", "intersection", "difference", "subset", "powerset", "cartesian",
        "collection", "dictionary", "index"
    ],
    "CONTROL_FLOW": [
        "when", "elif", "otherwise", "if", "else", "match", "case", "default",
        "while", "till", "as", "in", "repeat", "this", "stop", "skip",
        "loop", "condition", "break", "continue", "iterate", "for", "switch"
    ],
    "FUNCTIONS_MODULES": [
        "func", "function", "private", "export", "import", "return",
        "module", "lion", "parameter", "argument", "recursion", "scope",
        "callback", "closure", "def", "method"
    ],
    "DATABASE": [
        "database", "db", "littlestardb", "createdb", "removedb", "fetch",
        "countdb", "hasdb", "listdbs", "record", "table", "sql", "query",
        "data", "storage"
    ],
    "WEB": [
        "web", "html", "doctype", "body", "head", "style", "css", "webpage",
        "ui", "template", "render", "browser", "page", "website",
        "frontend", "layout", "design", "iframe"
    ],
    "MATH_EQUATIONS_GEOMETRY": [
        "solve", "quadratic", "equation", "simultaneous", "linear",
        "area", "volume", "perimeter", "circle", "sphere", "triangle",
        "square", "rectangle", "trapezoid", "parallelogram", "rhombus",
        "ellipse", "pentagon", "hexagon", "cube", "cylinder", "cone",
        "pyramid", "cuboid", "prism", "hemisphere", "ellipsoid", "shape",
        "sqrt", "sin", "cos", "tan", "asin", "acos", "atan", "log", "ln",
        "trig", "math", "factorial", "fibonacci", "prime", "gcd", "lcm",
        "random", "randint", "pi", "geometry", "algebra", "roots", "power",
        "abs", "floor", "ceil", "round"
    ],
    "HTTP_JSON_FILES": [
        "http", "httpget", "httppost", "httpput", "httpdelete", "json",
        "jsonparse", "jsonstringify", "api", "rest", "url", "fetch",
        "request", "response", "file", "read", "write", "append", "exists",
        "delete", "savefile", "exportfile", "compile", "otherwise",
        "error", "try", "catch", "assert", "throw", "exception", "endpoint"
    ],
    "UTILITIES_CURRENCY_UNITS": [
        "currency", "usd", "eur", "ngn", "gbp", "jpy", "cad", "aud", "brl",
        "convertcurrency", "unit", "convert", "meter", "kg", "lbs", "pound",
        "mile", "km", "inch", "yard", "gallon", "ton", "hour", "minute",
        "padleft", "padright", "bin", "oct", "hex", "hash", "sleep",
        "date", "time", "yearnow", "monthnow", "daynow", "weekday",
        "format", "timestamp", "elapsed", "comma", "conversion", "exchange"
    ]
}

# ═══════════════════════════════════════════════════════════════════
# THE MAIN RAG FUNCTION — Called by main.py
# ═══════════════════════════════════════════════════════════════════
def get_relevant_knowledge(user_message: str, code_context: str = "") -> str:
    """
    Simple RAG: Dynamically loads ONLY the relevant Littlestar 
    knowledge modules based on query intent.
    """
    text_to_analyze = f"{user_message} {code_context}".lower()
    selected_modules: Set[str] = set()

    for mod_name, keywords in MODULE_TRIGGERS.items():
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', text_to_analyze):
                selected_modules.add(mod_name)
                break

    if not selected_modules:
        selected_modules = {"VARIABLES_TYPES", "CONTROL_FLOW"}

    # STRICT CAP at 2 modules to guarantee token limits are never exceeded
    if len(selected_modules) > 2:
        priority_order = [
            "WEB", "DATABASE", "HTTP_JSON_FILES", "MATH_EQUATIONS_GEOMETRY",
            "COLLECTIONS", "FUNCTIONS_MODULES", "CONTROL_FLOW",
            "UTILITIES_CURRENCY_UNITS", "VARIABLES_TYPES"
        ]
        selected_modules = set([m for m in priority_order if m in selected_modules][:2])

    composed_knowledge = CORE_RULES + "\n"
    for mod_name in sorted(selected_modules):
        composed_knowledge += KNOWLEDGE_MODULES[mod_name] + "\n"

    print(f"📚 RAG Loaded modules: {sorted(selected_modules)}")
    return composed_knowledge

# Backwards compatibility
INTERPRETER_KNOWLEDGE = CORE_RULES