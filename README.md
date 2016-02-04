# Syntax

Syntax is an in-development command-line utility to make writing CSS easier. Syntax is written in Python and is designed for speed and ease of use. Syntax is planned to have: variables, functions, nested elements, and uses an indented syntax similar to Python. Currently it is not suggested to use Syntax as a replacement to the preprocessor you are using right now, as it is missing some key features such as functions and calculations, though feedback and testing is appreciated.


##Usage

To use Syntax, you first need to tell Syntax what directory to use. To do this, type `dir [directory]`.

After this, you can start listening for changes in that directory, type `watch`. Then Syntax will now start looking for .syn/.syntax files, and will create or modify their CSS counterparts.


##Example File

```
@myVariable: 10%

body
  padding: @mayVariable
  p
    font-size: @myVariable
```
