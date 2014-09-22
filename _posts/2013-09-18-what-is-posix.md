---
layout: post
title : What is POSIX?
---
POSIX stands for Portable Operating System Interface (for uniX) and is a family of standards maintained by the Austin Group. Its purpose is to support application portability between POSIX Operating Systems (POSIX-OS). This post will look at what exactly does portability mean and how POSIX supports that portability. Most of what is included here only considers POSIX.1-2008[^1].

#POSIX Portability Means#

* With minimal effort most executables can be used on other POSIX-OS's.
* With minimal effort most script files can be used on other POSIX-OS's.
* With minimal effort most C projects can compile on other POSIX-OS's.

#POSIX Portability Doesn't Mean#

* An executable will "just work" when copied to another POSIX-OS.
* A data file will open correctly when copied to another POSIX-OS.

#How POSIX Enables Portability#
POSIX promotes portability by defining three separate programming interfaces. These interfaces work together to create a seamless whole:

1. C Headers
2. Shell Command Language
3. Shell Utilities

Porting procedures for executables will depend on which POSIX interfaces the executable uses. A C program using the C Headers will simply need to be recompiled. A script file using Shell Command Language will need its shell interpreter path updated. And, Shell Utilities shouldn't need anything as these will be executable applications already in the POSIX environment.

In many cases porting may require more than simply updating a shell interpreter path or recompiling. It isn't uncommon for applications to have dependencies beyond POSIX. In these cases POSIX makes it so there are only one or two project dependencies to install instead of the fifteen.

[^1]: <http://pubs.opengroup.org/onlinepubs/9699919799/>
[^2]: <http://pubs.opengroup.org/onlinepubs/9699919799/>
