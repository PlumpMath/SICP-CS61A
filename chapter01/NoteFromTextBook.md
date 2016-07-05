#1.3Defining new function
- The name of a function is repeated twice, once in the frame and again as part of the function itself. The name appearing in the function is called the **intrinsic name**. The name in a frame is a **bound name**.
- We say that the scope of a local name is limited to the body of the user-defined function that defines it. 
- some concept
  + The domain is any single real number.
  + The range is any non-negative real number.
  + The intent is that the output is the square of the input.
-------------------------------
#1.4design functions
- Documentation
- Default Argument values 
-----------------------
#1.5Statment
- Together, a header and an indented suite of statements is called a clause. A compound statement consists of one or more clauses:
- Python includes several false values, including 0, None, and the boolean value False.
- "5 is greater than or equal to 5", and corresponds to the function ge in the operator module.
-  "0 equals -0", and corresponds to eq in the operator module.
- pred, curr = curr, pred + curr
  * All of the expressions to the right of = are evaluated before any rebinding takes place.
- An assert statement has an expression in a boolean context, followed by a quoted line of text (single or double quotes are both fine, but be consistent) that will be displayed if the expression evaluates to a false value.
- When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:python3 -m doctest <python_source_file>

----------------
#1.6HighOrderFunction
- Lexical scope. Locally defined functions also have access to the name bindings in the scope in which they are defined.
- intricate 
- When a user-defined function is called, its local frame extends its parent environment.
- Because they "enclose" information in this way, locally defined functions are often called closures.
- currying is useful when we require a function that takes in only a single argument

---------------------

#1.7recursive function
- Syntactic specification gives syntax for calling (number of arguments).
- Semantic specification tells what it does:
  - Preconditions are requirements on the caller.
  - Postconditions are promises from the function’s implementor.
- Theorem (Noetherian Induction): Suppose ≺ is a well-founded
relation and P is some property (predicate) such that whenever
P(y) is true for all y ≺ x, then P(x) is also true. Then
P(x) is true for all x.

---------------------------------

