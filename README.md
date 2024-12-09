# PyCurl Programming Language

## Overview

PyCurl is a custom programming language with a unique syntax that combines elements of Python and other programming languages. It provides a simple yet expressive way to write code with straightforward control structures and function definitions.

## Features

- Custom function definitions
- Flexible control structures (IF-ELSE, FOR loops)
- Simple print statements
- Support for basic arithmetic operations
- Supports both traditional and bracket-based syntax

## Installation

### Prerequisites
- Python 3.7 or higher
- Terminal/Command Prompt

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pycurl.git
   cd pycurl
   ```

2. Ensure you have the required Python version installed.

## Running Programs

To run a PyCurl program:

1. Open your terminal
2. Navigate to the project directory
3. Run the shell interpreter:
   ```bash
   python shell.py
   ```
4. In the PyCurl terminal, execute your program:
   ```
   RUN("yourprogram.pyCurl")
   ```

## Language Syntax Examples

### Function Definition
```
FUN add(a,b){
    RETURN a + b;
}
```

### Conditional Statements
```
FUN multiLineIFStatement(a,b){
    IF a==b THEN 
        PRINT("THEY are equal")
    ELSE IF a>b THEN
        PRINT("1st number is greater than the 2nd number")
    ELSE 
        PRINT("2nd number is greater than the 1st number")
    END
}
```

### For Loops
```
FOR i = 1 TO 10 THEN
    PRINT(i)
END

# Or with bracket syntax
FOR i = 1 TO 10 {
    PRINT(i)
}
```

### Comments
```
# This is a single-line comment
```

## Example Program

Here's a simple example program in PyCurl:

```
FUN greet(name){
    PRINT("Hello, " + name)
}

greet("World")
```

## Limitations

- The language is a custom implementation
- Error handling might be minimal
- Performance may vary

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/pycurl]((https://github.com/gopalkalawate/PyCurl))
