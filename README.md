Dodecal is a custom programming language designed for demonstration and educational purposes.  
It uses a syntax inspired by Python mixed with a simple assembly‑style command structure.
 
 Syntax Examples and Command List

| Command | Type of Processing | Arguments (in order) | Function |
|--------|---------------------|-----------------------|----------|
| add    | integer/variable    | a / b / var           | Add two integers and store the sum in a variable |
| sub    | integer/variable    | a / b / var           | Subtract two integers and store the difference in a variable |
| mul    | integer/variable    | a / b / var           | Multiply two integers and store the product in a variable |
| div    | integer/variable    | a / b / var           | Divide two integers and store the quotient in a variable |
| print  | text/int/variable   | text / var / int      | Print text or a variable to the terminal/console |
| printn | text/int/variable   | text / var / int      | Print text or a variable without a newline |
| set    | text/int/variable   | text / var / int      | Set a variable to another variable or integer |
| input  | text/int/variable   | var  / user‑prompt    | Take input from the user and store it in a variable |
| label  | n/a                 | n/a                   | Create a jump target that can be referenced later |
| goto   | n/a                 | n/a                   | Jump to a label and resume execution from there |
| if     | text/int/variable   | left / op / right     | Run a one‑line if statement; if the condition is true, the next command is executed |



This language is not designed to be a fully functional production language.  
It exists as a demonstration of how interpreters tokenize, parse, and execute instructions at a low level.

This is an open‑source project — feel free to take, redistribute, edit, or inspect the source code.  
There is a 99.99% chance anyone reading this can write code 100× better than I can, so if you find issues, let me know or fix them yourself!
