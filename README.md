# PyCurl Programming Language

## 📘 Overview

PyCurl is a custom programming language designed to provide a unique and intuitive coding experience. Blending elements from various programming paradigms, PyCurl offers a simple yet powerful syntax for developers.

## 🚀 Features

- Custom function definitions
- Flexible control structures
- Dynamic typing
- String and list manipulation
- Simple print and return statements
- Unique syntax for loops and conditionals

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- Terminal/Command Prompt

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/gopalkalawate/PyCurl.git
   cd pycurl
   ```

2. Ensure Python 3.7+ is installed

## 🖥️ Running Programs

1. Launch the interpreter:
   ```bash
   python shell.py
   ```

2. Run a PyCurl program:
   ```
   RUN("yourprogram.pyCurl")
   ```

## 📝 Language Syntax

### 1. Function Definitions

#### Single-Line Functions
```
FUN singleLineFunction() -> PRINT("Hello")
FUN add(a,b) -> RETURN a + b
```

#### Multi-Line Functions
```
FUN multiLineFunction(a,b){
    VAR result = a + b
    PRINT(result)
    RETURN result
END
```

### 2. Variable Declaration
```
VAR name = "PyCurl"
VAR number = 42
VAR list1 = [1, 2, 3]
```

### 3. String Operations
```
VAR str1 = "Hello"
VAR str2 = "World"

PRINT(str1 + str2)      # Concatenation
PRINT(str1 * 3)         # Repetition
```

### 4. List Operations
```
VAR list1 = [1, 2, 3, 4]
VAR list2 = [5, 6]

PRINT(list1 + list2)    # List concatenation
PRINT(list1 + 7)        # Add element
PRINT(list1 - 2)        # Remove element
PRINT(list1 * list2)    # List multiplication
```

### 5. Conditional Statements
```
FUN checkValue(a,b){
    IF a == b THEN
        PRINT("Equal")
    ELSE IF a > b THEN
        PRINT("First larger")
    ELSE
        PRINT("Second larger")
    END
}
```

### 6. Loops
```
# Range-based loop
FOR i = 1 TO 10 THEN
    PRINT(i)
END

# Bracket-based loop
FOR i = 1 TO 10 {
    PRINT(i)
}

# Loop with step
FOR i = 1 TO 10 STEP 2 {
    PRINT(i)
}
```

## 📋 Example Program

```
FUN mainProgram(){
    VAR greeting = "Hello"
    VAR names = ["Alice", "Bob", "Charlie"]
    
    FOR name IN names THEN
        PRINT(greeting + ", " + name)
    END
}

mainProgram()
```

## 🔍 Language Characteristics

- Dynamic typing
- Flexible function definitions
- Unique list and string manipulation
- Simple control structures
- Interpreted language

## 🚧 Limitations

- Experimental language
- Limited error handling
- Performance may vary
- Not suitable for production environments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📜 License

Distributed under the MIT License.

## 📞 Contact

Your Name - kalawategopal25@gmail.com

Project Link: [https://github.com/yourusername/pycurl](https://github.com/gopalkalawate/PyCurl)

## 🗺️ Roadmap

- Enhance error handling
- Add more built-in functions
- Improve performance
- Develop standard library
- Create comprehensive documentation

## 🔬 Technical Details

- Interpreter written in Python
- Custom parsing and execution engine
- Supports basic programming constructs
- Extensible design for future improvements

## 🎓 Learning Resources

- Syntax Guide
- Example Programs
- Community Forums
- Contribution Guidelines

**Happy Coding with PyCurl!** 🐍✨
