---
layout: post
sources: 
- http://martinfowler.com/bliki/HeaderInterface.html
- http://martinfowler.com/bliki/RoleInterface.html
---
When factoring interfaces, most approaches fall into one of two patterns: [Header Interfaces](http://martinfowler.com/bliki/HeaderInterface.html) or [Role Interfaces](http://martinfowler.com/bliki/RoleInterface.html). This post will contrast the two patterns with the hope of giving insight into the strengths and weaknesses of interface factoring.

# Header Interface #

## Pattern ##

One interface contains all public members for a class. Similar to C++ header files.


{% highlight C# %}
public class GroceryStore : IGroceryStore 
{
    public void SellProduce(IProduce produce);
    public void RefundProduce(IProduce produce);
    
    public void SellMeat(IMeat meat);
    public void RefundMeat(IMeat meat);

    public decimal TallyTotalSales();
    public decimal TallyTotalRefund();
}

public interface IGroceryStore
{
    void SellProduce(IProduce produce);
    void RefundProduce(IProduce produce);
    
    void SellMeat(IMeat meat);
    void RefundMeat(IMeat meat); 
    
    decimal TallyTotalSales();
    decimal TallyTotalRefunds();
}
{% endhighlight %}

##Analysis##

Header interfaces are easy to create but aren't always the easiest to understand or maintain.

###Pros###

* Very easy to make


###Cons###

* New members on GroceryStore will likely need to be added to IGroceryStore as well.
* Semantics of code aren't always clear


#Role Interfaces

##Pattern

A class is broken into many interfaces. Each interface represents a different role:


{% highlight C# %}
public class GroceryStore :IProduceDepartment ,IMeatDepartment, ITally
{
    public void SellProduce(IProduce produce);
    public void RefundProduce(IProduce produce);
    
    public void SellMeat(IMeat meat);
    public void RefundMeat(IMeat meat);

    public decimal TallyTotalSales();
    public decimal TallyTotalRefunds();
}

public interface IMeatDepartment 
{
    void SellMeat(IMeat meat);
    void RefundMeat(IMeat meat);
}

public interface IProduceDepartment 
{
    void SellProduce(IProduce produce);
    void RefundProduce(IProduce produce);
}

public interface ITally
{
    decimal TallyTotalSales();
    decimal TallyTotalRefunds();
}
{% endhighlight %}

##Analysis

This pattern is harder to implement than header interfaces, but often pays off by being more understandable and easier to maintain. The challenge comes from having many small interfaces instead of one big interface, since there are often many sensible ways to create the "role" interfaces. For example, another option for the sample code could have have been an ICheckout with all sale methods and an ICustomerService with all refund methods.

###Pros

* Easier to know exactly what you need to mock out for testing
* More clear what a method's purpose is (e.g. void CloseRegisters(ITally tally))

### Cons

* Harder to make than the Header Interface
* If project changes considerably might need to rename/reorganize interfaces
