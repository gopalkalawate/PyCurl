# PyCurl Programming Language

## Detailed Syntax Guide

### Function Definitions

#### Single-Line Functions
Single-line functions can be defined using a compact syntax:
```
FUN functionName(parameters) -> expression
```
Example:
```
FUN singleLineFunction() -> PRINT("Hello, World!")
FUN add(a,b) -> RETURN a + b
```

#### Multi-Line Functions
Multi-line functions use a more verbose syntax with curly braces or END keyword:
```
FUN functionName(parameters){
    # Function body
    STATEMENTS
    RETURN value
}

# Alternative syntax
FUN functionName(parameters)
    # Function body
    STATEMENTS
    RETURN value
END
```

Examples:
```
# Curly brace style
FUN multiLineFunction(a,b){
    VAR result = a + b
    PRINT(result)
    RETURN result
}

# END keyword style
FUN multiLineFunction(a,b)
    VAR result = a + b
    PRINT(result)
    RETURN result
END
```

### String Manipulation

#### String Creation
```
VAR str1 = "Hello"
VAR str2 = "World"
```

#### String Operations
1. Concatenation
```
PRINT(str1 + str2)  # Combines strings
# Result: "HelloWorld"
```

2. Repetition
```
PRINT(str1 * 3)  # Repeats string
# Result: "HelloHelloHello"
```

#### Key String Behaviors
- Strings can be added together
- Strings can be multiplied by integers
- Division and subtraction are not standard operations

### List Manipulation

#### List Creation
```
VAR list1 = [1, 2, 3, 4]
VAR list2 = [5, 6]
```

#### List Operations
1. List Concatenation
```
PRINT(list1 + list2)  
# Result: [1, 2, 3, 4, 5, 6]
```

2. Adding Elements
```
PRINT(list1 + 7)  
# Result: [1, 2, 3, 4, 7]
```

3. Removing Elements
```
PRINT(list1 - 2)  
# Likely removes the element at index 2
# Result: [1, 3, 4]
```

4. List Multiplication
```
PRINT(list1 * list2)  
# Concatenates lists
# Result: [1, 2, 3, 4, 5, 6]
```

5. Indexing
```
PRINT(list1 / 2)  
# Likely returns element at index 2
# Result: 3
```

### Control Structures

#### Conditional Statements
```
IF condition THEN
    # Code block
ELSE IF another_condition THEN
    # Another code block
ELSE
    # Default block
END
```

#### Loops
```
# Range-based FOR loop
FOR i = 1 TO 10 THEN
    PRINT(i)
END

# Alternative syntax with brackets
FOR i = 1 TO 10 {
    PRINT(i)
}

# WITH STEP
FOR i = 1 TO 10 STEP 2 {
    PRINT(i)
}
```

### Variable Declaration
```
VAR variableName = value
```

### Comments
```
# This is a single-line comment
```

## Important Notes
- Language syntax is custom and may differ from standard programming languages
- Some operations (like list division) might have unique interpretations
- Error handling and precise behavior may vary

## Example Program
```
FUN exampleProgram()
    VAR greeting = "Hello"
    VAR names = ["Alice", "Bob"]
    
    FOR i = 0 TO LEN(names)
        PRINT(greeting + ", " + name)
    END
END
```

## Planned Features & Roadmap
- Improved error handling
- More robust type checking
- Additional built-in functions
- Enhanced list and string manipulation

## Contributing
Interested in improving PyCurl? Check our contribution guidelines!
