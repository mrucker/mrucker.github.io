---
layout: post
---
First a formal definition, .NET Anonymous Types are statically type-checked, reference objects created inline. What exactly does that mean though? Are they different from traditional reference type classes like object and string? How is the "type" checked and enforced if they are created inline? Do they have any other special case limitations or abilities that aren't obvious at first? This post will answer these questions and more. While at the same time, hopefully removing some of the mystique around Anonymous Types so they can be used more confidently and effectively in day to day programming.

#Anonymous Types Behave Like Traditional Reference Types#

There are no differences between traditional reference types (e.g. String) and Anonymous Types. Just like traditional reference types, anonymous types can be passed by reference and assigned a null value.

#Type-Checking Is Enforced Just As With Any Other Type#

Anonymous Types have compile time type-checking enforced just like any other .NET type. Normally, type checking is performed by referring to a Type's class definition to see what is and isn't allowed for a Type. Anonymous Types don't have class files, since they are defined inline, but they still have a Type. An Anonymous Type's Type is equal to the order, name, and Types of its properties.

#Anonymous Types Are Still Part Of The Common Type System#

Anonymous Types inherit from System.Object just as almost every other .NET Type does.

#Anonymous Type Properties Are Read-Only#

Anonymous types themselves aren't read-only but their properties are. This means an Anonymous Type can be assigned to another Anonymous Type as long as they have the same Type, but their properties can't be assigned to.

#Anonymous Types Can Infer Property Names When Initialized#

At initialization, if a name for a property isn't given, the Anonymous Type will name the property the same as the variable that is being used to assign it. This one is hard to explain in writing but easy to understand when looking at the code example.

#Sample Code#


* [Anonymous Type Examples][1]

[1]: https://github.com/mrucker/AnonymousTypes
