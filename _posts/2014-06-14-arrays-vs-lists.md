---
layout: post
---
Two of the most important data structures in all programming languages are Arrays and Lists(aka linked lists). These structures are so common that nearly every programming language provides some level of direct support for them. What is the difference between Arrays and Lists? When should a developer use one over the other? And how are they implemented under the hood?

#The Difference Is Their Lookup Interface#

The primary difference between Arrays and Lists is their lookup interfaces. For example, an Array will allow direct lookup of any item in the collection (usually through an index). While a List will only allow lookup of the next or previous item in the List. An important thing to notice here is that these interfaces don't restrict how the actual lookup is handled. An Array can be used to implement a List: every time you move to the next item an internal index is incremented. And a List can be used to implement an Array: an index lookup is handled by traversing the correct number of nodes from the beginning of the List.

#Use What Is Most Understandable Not Most Performant#

The three goals I try to keep in mind when choosing how to write code are understandability, repetition, and performance. In regards to using an Array vs a List here is how it breaks down:

* Understandability: It depends on what is being done with the collection of objects. If random access of values is occurring the Array interface makes it more clear what is going on. If the collection is only being iterated over then a List makes it more clear this is the case. I think this should be the number one consideration.

* Repetition: For these two data structures I don't feel it matters too much either way. Both are very similar. An Array may allow for less code if a lot of specific index look ups need to be done. Outside of that I imagine most code would be the same length with either structure.

* Performance: This is probably the last consideration when choosing between the two for two reasons. One, since the primary difference is one of interface, every programming language can implement these differently making it challenging to know what actually is the best performance wise. And two, most general use code probably isn't performance critical enough to make a difference.

#Implementation Depends On The Language#

Because Arrays and Lists are primarily interfaces there is no way to know how they are implemented. Every programming language can implement them differently. In fact updates to existing could even change their implementation between updates. If implementation has to be known then a deeper reading of the programming language's documentation will be required to learn it.
