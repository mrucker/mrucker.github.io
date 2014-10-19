---
layout: post
---
Contravariance and Covariance was a language feature I was aware of in .NET, thanks to ReSharper, but didn't really understand. Then, while reading through John Skeet's C# In Depth the other night[^1], I was pleasantly surprised (and simultaneously not surprised at all) to find it covered. While it isn't something one needs all the time, it is a great example of the power of the .NET framework and how much careful thought has gone into crafting it. This article will start with a general introduction to basic Polymorphism concepts (needed to understand this feature) then move on to the specifics of contravariance and covariance.

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

All these relationships were explicitly defined by the developer using the `ClassName: Parent` syntax. In general no type relationships can be inferred unless there is an explicit relationship. This is known as Nominal Typing.

An example of that would look something like this:

{% highlight C# %}
public class Animal1: Object
{
  public void Eat(Food f) { }
}

public class Animal2 
{ 
  public void Eat(Food f) { }
}

public Dragon: Animal1 { }

//Illegal despite Animal 1 and 2 
//having identical public interfaces
Animal2 a2 = new Dragon();
{% endhighlight %}


Because Dragon hasn't been explicitly defined as having a relationship to Animal2 no assignment can be made even though we can see that logically the developer probably meant for them to be related. Here is where Contravariance and Covariance comes in.

#Co-Contra-Variance#
Contravariance and Covariance allow for the type checker to infer relationships among generic types. Explicitly named relationships still need to exist but only amongst the separate types that make up the generic and not amongst the generic as a whole.

##Covariance##

{% highlight C# %}
public class Cry { }
public class Maw: Cry { }
public class Baa: Cry { }

public class Animal<out T> where T: Cry
{
  public T MakeCry() { }
}

public class Sheep: Animal<Baa> { }
public class Llama: Animal<Maw[^2]> { }
{% endhighlight %}

Which would allow the following assignments

{% highlight C# %}

Animal<Cry> a1 = new Animal<Baa>();
Animal<Cry> a2 = new Sheep();
Animal<Baa> a3 = new Sheep();
{% endhighlight %}

Notice that we never explicitily defined that Sheep is a subtype of Animal<Cry>. We only said that it was a subtype of Animal<Baa>. However thanks to Covariance, the type checker performs two separate type checks:
1. Is Sheep of type Animal
2. Is <Baa> of type <Cry>

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
1. Is Right type assignable to Left Type
2. Is Left Generic assignable to Right Generic

#Conclusion#
Contravariance and Covariance are powerful and useful features when needed. They allow for exponentially more variability in type assignment without adding much complexity for the developer. Perhaps the biggest drawback is that Contravariance is very hard to make sense of. It smacks of the same problem that Little-Endian runs into: one has to think in two different directions at once.

[^1]:http://www.amazon.com/Depth-3rd-Edition-Jon-Skeet/dp/161729134X 
[^2]:http://en.wikipedia.org/wiki/List_of_animal_sounds
[^3]:http://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)
[^4]:http://blogs.msdn.com/b/csharpfaq/archive/2010/02/16/covariance-and-contravariance-faq.aspx
