---
layout: post
---

Abstract algebra is the formal and systematic study of algebraic structures. Algebraic structures are two component systems comprised of a set (often called the domain) and a collection of functions mapping the set into itself (often called operations){% cite pinter2010book %}. 

According to {% cite kramer1982nature %} abstract algebra is "abstract" not because it relaxes the rules of more traditional algebras, but rather because it has been developed from postulates that are true given fundamental axioms. Such an approach abstracts the study of algebraic structures away from the concrete interpretations that inspired its development.

Even though this post is primarily concerned with abstract algebra, we will begin by defining some different uses of the word algebra in an effort to give some more clarity to this post and also help the reader when consuming other content that may not clearly define what is meant by "algebra".

# Algebras

In abstract algebra the term "algebra" seems to refer to either an algebreic structure with a formal name that includes the term algebra (e.g., see the use of "algebra" in reference to a boolean algebra in {% cite halmos1974measure %}) or to a vector space \\(V\\) over a field \\(F\\) with the addition of a bilinier operation \\( * : V \times V \to V\\) {% cite hazewinkel2004algebras %}. Many other algebraic structures (e.g., magmas, groups, rings and fields) do not appear to be ever reffered to as "algebras".

In a more vernacular sense the term algebra tends to denote specific models of algebraic structures. For example, matrix algebra often refers to a ring whose domain is a set of matrices and whose operations are matrix addition and matrix multiplication. Classical algebra (i.e., equations with real valued variables) generally refers to a field with \\(\Reals\\) for a domain. And boolean algebra is a more full featured ring with \\(\lbrace\,1,0\,\rbrace\\) for a domain and for operations has "exclusive or" and "and".

It is also worth considering how the above abstract definition differs from from the idea of a "space" within modern mathematics. My answer at this time is that spaces tend to be structures that combine an algebra with some function mapping the domain into a new codomain. The biggest problem with this answer are vector spaces, which, according to my answer, should be called an algebra rather than a space. Perhaps what makes a vector space a "space" is the fact that it has a definition of dimensionality (i.e., the minimum number of basis required to span the space)?

# History 

The first step down the road to modern abstract algebra began in the 16th century with Rafael Bombelli's development of imaginary numbers. The development of the imaginaries forced mathematicians to rethink how fundamental operations functioned (e.g., what did it mean to multiply \\(a + bi)\\) by \\(c + di\\)). The imaginary number problem was quickly solved using distributive laws, and mathematicians spent the next few hundred years solving previously unsolvable equations without considering further changes to algebraic operations. 

The age of equation solving is considered to end with either the work of Niels Abel {% cite pinter2010book %}, who showed no general solution existed for polynomials of degree greater than 4, or Carl Friedrich Gauss {% cite kramer1982nature %}, who proved the fundamental theorem of algebra (i.e., every non-zero single variable n degree polynomial with complex coefficients has exactly n complex roots {% cite wiki2020fundamental %}). Both results showed there was little left to do in terms of traditional equation solving.

Following the conclusion of the classical age of equation solving two developments in the mid 19th century opened the door to modern abstract algebra: quaternions and boolean algebra. Quaternions were developed by William Rowan Hamilton and are the first known algebraic structure to have a noncommutative product. Boolean algebra was developed by George Booleand showed the benefit of fundamentally rethinking concepts common to classical polynomials. Both of these advancements showed that the future of algebra lay in studying changes to fundamental axioms of algebraic structures. {% cite kramer1982nature %}{% cite pinter2010book %}

# Operations

Given some set \\(A\\) and two binary operation \\(\Box\text{ and }\rhd\\) common operation axioms are:
 * \\(\Box\\) is associative if \\(\forall x,y,z \in A\\): 
   * \\((x \Box y) \Box z = x \Box (y \Box z) \\)
 * \\(\rhd\\) is distributive over \\(\Box\\) if \\(\forall x,y,z \in A\\):
   * left: \\(x \rhd (y \Box z) = (x \rhd y) \Box (x \rhd z)\\)
   * right: \\((y \Box z) \rhd x = (y \rhd x) \Box (z \rhd x)\\)
 * \\(\Box\\) is commutative if \\(\forall x,y,z \in A\\): 
   * \\(y \Box z = z \Box y\\)

# Sets

Given some set \\(A\\) and two binary operation \\(\Box\text{ and }\rhd\\) common set axioms are:
 * \\(A\\) contains an identity element \\(i\\) for \\(\Box\\) if \\(\forall x \in A \\):
   * \\( x \Box i = x \\)
 * \\(A\\) contains an inverse element for \\(\Box\\) if \\(\forall x,y \in A,\ \exists y^- \in A\\) s.t.:
   * \\( x \Box y \Box y^- = x \\)

# Structures

There are many fundamental structures in abstract algebra. Perhaps four of the more important ones are:
 * Magma: 
   * one binary operation with closure
 * Group: 
   * one binary operation with closure, associativity, identity and inverse
 * Rings:    
   * one binary operation with closure, associativity, commutativity, identity and inverse
   * one binary operation with closure, associativity, distributivity and identity
 * Fields:
   * one binary operation with closure, associativity, commutativity, identity and inverse
   * one binary operation with closure, associativity, commutativity, identity, inverse and distributivity

Finally, it is sometimes useful to combine an algebraic structure with a field. When this is done the preposition "over" is often used. For example, in "a vector space \\(V\\) over the field \\(\Reals\\)," V is a group with commutativity which combined with a field via a single operation \\( * : V \times R \to V \\) that is commutative, distributive, has identity and has inverse. It is worth noting that I have seen "over" used in other ways with algebraic structures but it seems incredibly rare.
