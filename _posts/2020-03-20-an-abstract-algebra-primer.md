---
layout: post
---

Abstract algebra is the formal and systematic study of algebraic structures. An algebraic structure can be defined as a system made up of two components: (1) a set (often called the domain) and (2) a collection of functions mapping the set into itself (often called operations){% cite pinter2010book %}. 

According to {% cite kramer1982nature %} abstract algebra is "abstract" not because it relaxes the rules of more traditional algebras, but rather because it has been developed from postulates that are true given fundamental axioms. Such an approach abstracts the study of algebraic structures away from the concrete interpretations that inspired its development.

# What Is An Algebra

Even though this post is primarily concerned with abstract algebra, we will begin by defining some different uses of the word algebra in an effort to give some more clarity to this post and also help the reader when consuming other content that may not clearly define what is meant by "algebra".

In abstract algebra the term "algebra" seems to refer to either an algebreic structure with a formal name that includes the term algebra (e.g., see the use of "algebra" in reference to a boolean algebra in {% cite halmos1974measure %}) or to a vector space \\(V\\) over a field \\(F\\) with the addition of a biliniar operation \\( * : V \times V \to V\\) {% cite hazewinkel2004algebras %}. Other algebraic structures (e.g., magmas, groups, rings and fields) do not appear to be ever referred to as "algebras".

In informal usage the term algebra tends to denote specific models of algebraic structures. For example, matrix algebra often refers to a ring whose domain is a set of matrices and whose operations are matrix addition and matrix multiplication. Classical algebra (i.e., equations with real valued variables) generally refers to a field with \\(\Reals\\) for a domain. And boolean algebra is a more full featured ring with \\(\lbrace\,1,0\,\rbrace\\) for a domain and for operations has "exclusive or" and "and". It should be noted that this is all simply my interpretation. None of the above connections are actually formally defined anywhere.

Finally, it is worth considering how the above abstract definition differs from from the idea of a "space" within modern mathematics. My answer at this time is that spaces tend to be structures that combine an algebra with some function mapping the domain into a new codomain. The biggest problem with this answer are vector spaces, which, according to my answer, should be called an algebra rather than a space. Perhaps what makes a vector space a "space" is the fact that it has a definition of dimensionality (i.e., the minimum number of basis required to span the space)?

# How Did We Get Here

The first step down the road to modern abstract algebra began in the 16th century with Rafael Bombelli's development of imaginary numbers. These new numbers temporarily forced mathematicians to rethink how fundamental operations worked (e.g., what did it mean to multiply \\(a + bi\\) by \\(c + di\\)). Reconsidering operations was only short-lived though as issues with imaginary operations were quickly resolved satisfactorily and mathematicians turned their attention back to solving equations.

Equation solving continued to dominate mathematics until the publication of two works in the early 19th century: (1) Niels Abel {% cite pinter2010book %} showed that no general solution existed for polynomials of degree greater than 4 and (2) Carl Friedrich Gauss {% cite kramer1982nature %} proved the fundamental theorem of algebra (i.e., every non-zero single variable n degree polynomial with complex coefficients has exactly n complex roots {% cite wiki2020fundamental %}). With these two achievements there seemed little left to do with equations and mathematicians began searching for new problems.

This search came to an end for some when the door cracked open by imaginary numbers in the 16th century was finally flung wide open by William Rowan Hamilton. Inspired by imaginary number's two dimensions Hamilton developed four dimensional numbers, which he called quaternions. After years of effort Hamilton realized that the only way to define a satisfactory product in four dimensions was to relax the commutative property on multiplication (i.e. \\(A * B \text{ does not have to equal } B * A\\)) creating the first known ring. He published his work in 1843 {% cite kramer1982nature %}. 

At almost the same time that Hamilton was developing quaternions George Boole was developing boolean algebra, another new computational system with new rules. Boole published his work in 1847 {% cite pinter2010book %}. With the dual developments of quaternions and boolean algebra it became clear there was much work to do in exploring and defining new computational systems, and abstract algebra as we know it today was born.

# Operations

The basic building blocks of algebraic structures are operations. Operations are defined via axioms that describe how the operations interact. In what follows a few of the most common operation axioms are listed. Given some set \\(A\\) and two binary operation \\(\diamond\text{ and }\rhd\\):
 * \\(\diamond\\) has closure on \\(A\\) if \\(\forall x,y \in A\\):
   * \\( x \diamond y \in A \\)
 * \\(\diamond\\) is associative if \\(\forall x,y,z \in A\\): 
   * \\((x \diamond y) \diamond z = x \diamond (y \diamond z) \\)
 * \\(\rhd\\) is distributive over \\(\diamond\\) if \\(\forall x,y,z \in A\\):
   * left: \\(x \rhd (y \diamond z) = (x \rhd y) \diamond (x \rhd z)\\)
   * right: \\((y \diamond z) \rhd x = (y \rhd x) \diamond (z \rhd x)\\)
 * \\(\diamond\\) is commutative if \\(\forall x,y,z \in A\\): 
   * \\(y \diamond z = z \diamond y\\)

# Sets

Along with the operation axioms it is also possible for an algebraic structure to have axioms describing its domain. These axioms are often in reference to the structure's operations. Two common examples follow. Given some set \\(A\\) and two binary operation \\(\diamond\text{ and }\rhd\\):
 * \\(A\\) contains an identity element \\(i\\) for \\(\diamond\\) if \\(\forall x \in A \\):
   * \\( x \diamond i = x \\)
 * \\(A\\) contains an inverse element for \\(\diamond\\) if \\(\forall x,y \in A,\ \exists y^- \in A\\) s.t.:
   * \\( x \diamond y \diamond y^- = x \\)

# Structures

With common operation and set axioms defined above it becomes possible to define some fundamental structures in abstract algebra. Naming these structures, though it means having to learn them, makes communicating about them easier. Perhaps four of the more important ones are:
 * Magma: 
   * a binary operation with closure
 * Group: 
   * a binary operation with closure, associativity, identity and inverse
 * Rings:    
   * a binary operation with closure, associativity, commutativity, identity and inverse
   * a binary operation with closure, associativity, distributivity and identity
 * Fields:
   * a binary operation with closure, associativity, commutativity, identity and inverse
   * a binary operation with closure, associativity, commutativity, identity, inverse and distributivity

In addition, it is sometimes useful to combine a simple algebraic structure with a field. When this is done the preposition "over" is often used. For example, "a vector space \\(V\\) over the field \\(F\\)," is a commutative group V combined with the field \\(F\\) via a single operation \\( * : F \times V \to V \\) that is commutative and distributive. While I have seen "over" used in other ways when describing algebraic structures, it seems incredibly rare.
