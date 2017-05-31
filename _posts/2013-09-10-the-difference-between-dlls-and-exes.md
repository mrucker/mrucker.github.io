---
layout   : post
---
This question came up after learning that .NET projects can reference code from dll's and exe's. While .NET prompted the question the answer applies to all dll's and exe's, so .NET will be mostly left out. The goal is to provide a more detailed (and at the same time simpler) view of the Windows environment through the comparison.

# Simple Exe Explanation #

Let's begin with the exe since it can work completely independently. Assume there is a simple console application called HelloWorld.exe. This application, when executed, will print out the words "Hello, World!" and then wait for keyboard input before exiting. In order to achieve this HelloWorld.exe needs three things:

1. Code - Instructions telling the computer to write a string to the console and then wait for user input.
2. Data - The string we'd like to display in the console ("Hello, World!" in this case).
3. Hand Off - A way to give the Code and Data to the Operating System so it can execute.

No matter how complex an exe gets it will always basically contain the above three things. Are dll's any different?

# Simple Dll Explanation #

A dll is clearly different from an executable because it can't run on its own. To examine dlls then, assume there is a simple HelloWorld.dll that contains instructions to print "Hello, World!" and then to wait for keyboard input before continuing. This dll can't do much on its own other than sit on your machine. So, also assume there is a simple HelloWorld.exe file that references the HelloWorld.dll, runs its instructions, and then exits. In order for this to work the HelloWorld.dll needs three things:

1. Code - Instructions telling the computer to write a string to the console and then wait for user input.
2. Data - The string we'd like to display in the console ("Hello, World!" in this case).
3. Hand Off - A way to give the Code and Data to an executing process so it can execute.

No matter how complex a dll gets it will only ever contain the above three things.

# Comparing Exe to Dll #

Looking at the simple explanations above, dll's and exe's appear to be very similar. Both contain code, data, and a way to "hand off". The only real difference seems to be in the Hand Off. Even there, however, there isn't a huge difference. The dll is handing off to a host process and the executable is handing off to the operating system (Windows).

Microsoft also seems to have thought dll's and exe's were similar because both are actually stored using the same file format: PE (Portable Executable)[^1]. For more information on the PE format see Matt Pietrek's excellent article in the February 2002 issue of MSDN Magazine[^3]

So, if both are stored in the same format and contain basically the same three elements what's the difference? As alluded to above it is in the hand off. Because the operating system can't be modified exe files have to be able to tell the OS where to begin executing code. This is called an entry point. Dlls on the other hand don't have entry points. Their hand off code is placed into whatever host process that references them at compile time. So the difference is simply that:

* Exe's contain an entry point to tell the Operating System where to begin execution
* Dll's don't contain entry points. Instead, their entry points exist in the host process that references them.


# Sample Code #
The sample code[^2] uses PowerShell to perform a binary comparison of four identical projects. Two of the projects output as exe's and two of the projects output as dll's. There is an incredible amount of similarity between the exe's and dll's, as we would expect if entry points really are the only difference.

[^1]: <http://en.wikipedia.org/wiki/Portable_Executable>
[^2]: <https://github.com/mrucker/.NET-Studies/tree/master/CompareDotNetExeAndDll>
[^3]: <http://msdn.microsoft.com/en-us/magazine/cc301805.aspx>
