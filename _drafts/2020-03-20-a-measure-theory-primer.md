---
layout: post
---
Set theory is ubiquitous in modern mathematics. As such, over the course of my studies, I've created a complex patchwork of ideas and notation from various sources without any clear singular thought. This post is my effort to consider all these ideas at once in order to clean up inconsistencies and discover meaningful gaps.

# Interpretation

Sets are often described as collections of objects. However, such a description, while helpful for intuitive understanding, isn't strictly necessary for the theory. Rather, as is the case with many abstract mathematical theories, the theory supports many concrete interpretations (e.g., boolean-valued functions rather than collections of objects).

# History 

The seminal work in set theory occured in the late 19th century and can be attributed to two primary figures: Georg Cantor and Richard Dedekind. This early work now belongs to what is known as naïve set theory. The next major development occured around 1900 when Ernst Zermelo and Bertrand Russell independently discovered what is now known as Russel's Paradox. This discovery motivated considerable effort to create a consistent axiomatic system of sets -- ultimately leading to well known results such as Zermelo-Fraenkel set theory (which utilized the axiom of choice to remove paradoxes) and the Neumann-Gödel-Bernays set theory (which used classes to remove paradoxes). {% cite ferreiros2019early %} {% cite randall2017alternative %}

# Preliminaries

Before developing basic set ideas some simple terminology is needed. For this purpose we will borrow from {% cite halmos1974measure %}. First, we will always assume that there is some universal set \\( X \\) called the *space* whose elements will be called *points*. Next, we will define \\( \empty \\) to be the unique empty set without any points. Finally, we will construct sets with expressions of the form \\(\lbrace\, z : \pi(z) \,\rbrace \\) which can be read as the set of all \\(z\\) which satisify \\(\pi(z)\\).

# \\(\sigma\\)-algebra

Set theory uses two fundamental relations: (1) *membership*, which expresses that an element is in a set and is written \\( x \in X \\) and (2) *subset*, which expresses that a set is contained within another set and is defined such that \\( A \subseteq X \iff \forall a \in A,\, a \in X\\). A common additional relation built from these is *equality* which is defined so that \\(A = B \iff A \subseteq B \text{ and } B \subseteq A\\).

# Measurable Sets

# Measurable Functions

# Terminology

