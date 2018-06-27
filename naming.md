## `:%s/true/True`, every f\*\*\*\*\*\* time
Why? I guess the reason is `True` and `False` are classes? I found this on the
[internet](https://stackoverflow.com/questions/521476/why-true-false-is-capitalized-in-python)

PEP 285:
>
    Should the constants be called 'True' and 'False' (similar to None) or 'true' and 'false' (as in C++, Java and C99)?
    => True and False.
    Most reviewers agree that consistency within Python is more important than consistency with other languages.

OK, but why are built-in constants are camel case? `None` is strange enough, 
why should `true` and `false` be like it?

I'm quite confused about built-in constants and keywords, built-in constants 
are also keywords I guess, so why don't you stick to the convention of the 
keywords?

Plus, users don't care about whether true and false are built-in constants, 
there're no meaning to distinguish a constant `True` and a plain `true`, 
nobody would use `true` in Python anyway.

Oh, a word just came up, it's __doctrine__. It seems people behind the PEP 
recite Guido's poem of philosophy before writing every word. And, what the 
f\*\*\* is a user?


## `throw Ex`... wait, that's `raise`


## `def async a`... wait, what? that's `async def`!
Why? Guido just defined a function asynchronously?