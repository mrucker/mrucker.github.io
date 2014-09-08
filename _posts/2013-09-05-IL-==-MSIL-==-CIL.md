---
layout: post
---
In the .NET world IL, MSIL, and CIL all refer to the compiled output of .NET languages. 

* IL - Intermediate Language
* MSIL - Microsoft Intermediate Language
* CIL - Common Intermediate Language

In most cases CIL is the best nomenclature to use of the three. This is because IL can have other meanings in other contexts ([see][1]), and MSIL isn't mentioned in the standards (see page 314 of [ECMA-335][2]).

As a side note CIL isn't able to be executed directly. Instead it relies on a second compiler to turn it into proper assembly code for the machine it is running on. There are currently three main CIL to Assembly compilers: Microsoft's CLR (aka JIT), Microsoft's NGEN pre-compiler and Xamarin's Mono project (also a JIT).

[1]: http://en.wikipedia.org/wiki/Intermediate_language
[2]: http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-335.pdf
