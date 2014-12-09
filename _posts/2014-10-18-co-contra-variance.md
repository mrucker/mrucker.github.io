---
layout: post
title: Co-Contra-Variance
---
Contravariance and Covariance is an advanced language feature in .NET. While it isn't ever necessary, it can add a really nice flair of finesse to a library. It is also a great example of the power of the .NET framework and how much careful thought has gone into crafting it. This article will start with a general introduction to basic Polymorphism concepts (needed to understand this feature) then move on to the specifics of contravariance and covariance.

#Polymorphism#

In a nutshell polymorphism is a tool of abstraction. It allows developers to be specific when needed and vague when specificity isn't needed. This control comes from type checker enforced relationships among types. For the most part these relationships have to be explicitly defined by the developer. However, in the case of contravariance and covariance the type checker is able to infer more complex type relationships than a developer has explicitly defined.

#Code#
To make this a little more clear let's look at a simple example.

Let's say we are working with the following three types.

{% highlight C# %}
public class Animal: Object { }
public class Beaver: Animal { }
public class Dragon: Animal { }
{% endhighlight %}

We have created a base Animal type which inherits from Object and two Animal subtypes: Beaver and Dragon. In standard type polymorphism then, any subtype can be assigned to any of its supertypes. For our types that would look like this:

{% highlight C# %}
//Legal assignments
Object o1 = new Animal();
Animal a1 = new Beaver();
Animal a2 = new Dragon();

//Illegal assignments
Beaver b1 = new Object();
Dragon d1 = new Beaver();
Dragon d2 = new Animal();
{% endhighlight %}

All these relationships were explicitly defined by the developer using the `ClassName: Parent` syntax. In general, no type relationships can be inferred unless there is an explicit relationship. This is known as Nominal Typing (.NET is a Nominally Typed language).

#Co-Contra-Variance#
Contravariance and Covariance, while different sides of the same coin, aren't equally approachable. At least for me, Covariance was pretty straight forward to learn and use (in fact I bet you've used it without even knowing it). Contravariance on the other hand, has feels like I'm using double negatives. I lose track of what it is I'm actually saying when using it.

##Covariance##

To look at Covariance let's say we have the following types:

{% highlight C# %}
public class Cry { }
public class Maw: Cry { }
public class Baa: Cry { }

public class Animal<out T> where T: Cry
{
  public T MakeCry() { }
}

public class Sheep: Animal<Baa> { }
public class Llama: Animal<Maw> { }
{% endhighlight %}

In this case Covariance would allow the following assignments:

{% highlight C# %}

Animal<Cry> a1 = new Animal<Baa>();
Animal<Cry> a2 = new Sheep();
Animal<Baa> a3 = new Sheep();
{% endhighlight %}

Notice that we never explicitily defined that Sheep is a subtype of Animal<Cry>. We only said that it was a subtype of Animal<Baa>. However thanks to Covariance, the type checker performs two separate type checks:

1. Is Sheep of type Animal
2. Is Baa of type Cry

In this case we did define both of those relationships explicitly.

##Contravariance##

Contravariance works the same way except in reverse (at least in regards to the generic types, the root type is still checked in the normal way).

{% highlight C# %}
public class Food { }
public class Fish: Food { } 
public class Kelp: Food { }

public class Animal<in T> where T: Food
{
  public void Eat(T food) { }
}

public class Eater: Animal<Food> { }
public class Otter: Animal<Kelp> { }
public class Eagle: Animal<Fish> { }
{% endhighlight %}

Which would allow the following assignments

{% highlight C# %}
//Legal assignments
Animal<Kelp> a1 = new Eater();
Animal<Fish> a2 = new Animal<Food>();

//Illegal assignements
Eater e = new Otter();
Otter o = new Eater();
{% endhighlight %}

In this case the type checker performs the following checks:

1. Is Eater of type Animal
2. Is Kelp of type Food

#Conclusion#
Contravariance and Covariance are powerful and useful features when needed. They allow for exponentially more variability in type assignment without adding much complexity for the developer. Perhaps the biggest drawback is that Contravariance is very hard to make sense of. It smacks of the same problem that Little-Endian runs into: one has to think in two different directions at once. For more reading on this subject I recommend Jon Skeet[^1], Wikipedia[^2] and MSDN[^3].

[^1]:[C# In Depth 3rd Edition by Jon Skeet](http://www.amazon.com/Depth-3rd-Edition-Jon-Skeet/dp/161729134X)
[^2]:[Covariance and contravariance (computer science)](http://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science))
[^3]:[Covariance and Contravariance FAQ](http://blogs.msdn.com/b/csharpfaq/archive/2010/02/16/covariance-and-contravariance-faq.aspx)
