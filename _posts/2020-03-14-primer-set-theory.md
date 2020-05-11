---
title: "Primer: Set Theory"
---
Set theory is ubiquitous in modern mathematics. As such, over the course of my studies, I've created a complex patchwork of ideas and notation from various sources without any clear singular thought. This post is my effort to consider all these ideas at once in order to clean up inconsistencies and discover meaningful gaps.

# Interpretation

Sets are often described as collections of objects. However, such a description, while helpful for intuitive understanding, isn't strictly necessary for the theory. Rather, as is the case with many abstract mathematical theories, the theory supports many concrete interpretations (e.g., boolean-valued functions rather than collections of objects).

# History 

The seminal work in set theory occured in the late 19th century and can be attributed to two primary figures: Georg Cantor and Richard Dedekind. This early work now belongs to what is known as naïve set theory. The next major development occured around 1900 when Ernst Zermelo and Bertrand Russell independently discovered what is now known as Russel's Paradox. This discovery motivated considerable effort to create a consistent axiomatic system of sets -- ultimately leading to well known results such as Zermelo-Fraenkel set theory (which utilized the axiom of choice to remove paradoxes) and the Neumann-Gödel-Bernays set theory (which used classes to remove paradoxes). {% cite ferreiros2019early %} {% cite randall2017alternative %}

# Preliminaries

Before developing basic set ideas some simple terminology is needed. For this purpose we will borrow from {% cite halmos1974measure %}. First, we will always assume that there is some universal set \\( X \\) called the *space* whose elements will be called *points*. Next, we will define \\( \empty \\) to be the unique empty set without any points. Finally, we will construct sets with expressions of the form \\(\lbrace\, z : \pi(z) \,\rbrace \\) which can be read as the set of all \\(z\\) which satisify \\(\pi(z)\\).

# Relations

Set theory uses two fundamental relations: (1) *membership*, which expresses that an element is in a set and is written \\( x \in X \\) and (2) *subset*, which expresses that a set is contained within another set and is defined such that \\( A \subseteq X \iff \forall a \in A,\, a \in X\\). A common additional relation built from these is *equality* which is defined so that \\(A = B \iff A \subseteq B \text{ and } B \subseteq A\\).

# Operations

Set theory posesses two fundamental operations: (1) *union*, an operation to combinine two sets and discarding duplicate elements, defined \\( A \cup B := \lbrace\,z : z \in A \text{ or } z \in B \,\rbrace\\) and (2) *negation*, an operation to select the set of all things not in a set, defined \\(\neg A := \lbrace\,z : \text{ not } z \in A,\rbrace\\). In addition, a common operation created from the two fundamentals is *intersection*, defined \\(A \cap B := \neg( \neg A \cup \neg B)\\).

# Cardinality

Perhaps one of the most important results in set theory is the ability to compare the size of sets (i.e., their *cardinality*). The notation to refer to a set's cardinality is \\( \|X\| \\). For finite sets the cardinality equals the number of elements within the set. For infinite sets, comparison becomes trickier but can be done through bijective mapping, where two sets whose elements can be mapped one to one are considered the same size. Via this technique it can be shown that the cardinality of the natural numbers \\(\N\\) is equal to the cardinality of the even numbers via the bijection \\(n \mapsto 2n\\). So, we can write \\(\|\N\| = \|\lbrace\,2n:n\in\N\,\rbrace\|\\). 

# Algebras

Occasionally authors will talk about an *algebra of sets* or a *field of sets*. When this is done it is in reference to some set of sets which is closed under a finite number of union and negation operations. A closely related object is a \\(\sigma\\)-algebra. A \\(\sigma\\)-algebra is also an *algebra of sets* but it requires closure under countably infinite unions and negations. The countably infinite condition of \\(\sigma\\)-algebras allows for the use of limits and classical analysis. Two examples of algebras are now given: (1) perhaps the simplest algebra of sets is the set \\(\lbrace\, X,\,\empty\,\rbrace\\) and (2) perhaps the most common algebra is the powerset of \\(X\\) sometimes written \\(2^X\\) in reference to interpreting each subset of \\(X\\) as a function that maps an element to either 0 or 1.

# Terminology

Due to the ubiquity of sets there is considerable terminology. Here are just some common set descriptors:
 * *Open* -- a set which doesn't contain any of its boundary points (e.g., its infimum or supremum)
 * *Closed* -- a set which does contain its boundary points (e.g., its minimum or maximum)
 * *Discrete* - there is no clear definition of a discrete set but a good working one is any countable set
 * *Finite* -- a set with a non-infinite cardinality (i.e., less than or equal to \\(\|\N\|\\))
 * *Infinite* -- a set with a cardinality greater than or equal to \\(\|\N\|\\) (i.e., \\(\aleph_0\\))
 * *Bounded* -- a set with finite measure in some sense (however it still may have infinite cardinality)
 * *Countably Infinite* -- any set which can be bijectively mapped to \\(\N\\)
