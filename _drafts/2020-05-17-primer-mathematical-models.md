---
title: 'Primer: Mathematical Models'
---

A mathematical model is any description of real world phenomenona with mathematical techniques. Models can range from localized (e.g., the energy I consume) to universal (e.g., the energy stored in matter), small (e.g., the movement of electrons around an atom) to large (e.g., the movement of planets around the sun) and concrete (e.g., the distance to work) to abstract (e.g., spacetime). In general, mathematical models have three uses: (1) predicting outputs, (2) determining inputs, and (3) describing the relationship between inputs and outputs. In what follows we will explore a few simple models to gain a greater understanding of their usages and characteristics.

# Single Function Models

## Deterministic

Perhaps the simplest of all models is the single function deterministic model. This model can be written as \\[ f(x) = y, \\] where \\(x\\) is the model's input variable, \\(y\\) is model's output variable and \\(f\\) is the function relating \\(x\\) to \\(y\\). Models of this type can describe phenomena such as time to money, speed to distance, and altitude to pressure.

The three uses of mathematical models can be seen by fixing two of the model's components and solving for the third: to predict outputs fix \\(f\\) and \\(x\\) and solve for \\(y\\) (e.g., basic arithmetic), to determine inputs fix \\f(\\) and \\(y\\) and solve for \\(x\\) (e.g., simple algebra), and to describe the relationship between inputs and outputs fix \\(x\\) and \\(y\\) and determine \\(f\\) (e.g., modern supervised learning).

## Stochastic

By definition mathematical functions only return a single output for any input. Unfortunately, many phenomena are inherently stochastic potentially producing many different outputs for a fixed input. To deal with this mathematics has introduced the random variable: \\[ X = f(\omega), \\] where \\(X\\) is the random variable, \\(\omega\\) is considered a random event, and \\(f\\) maps an event \\(\omega\\) to . This convention pushes all "uncertainty" into \\(\omega\\) allowing \\(X\\) to continue to have only one output for each input.

# Multifunction Models

## Multifunction Deterministic
The next logical step for deterministic models is to consider the case of systems of equations. For example, 

$$ 
    \begin{aligned} 
      f(a,b) &= y_1\\
      g(a,b) &= y_2\\ 
    \end{aligned}.
$$

Models of this kind can be used for phenomena such as the movement of a pendulum through time, chemical outputs given mixtures of inputs, and ordering food from a menu to feed a group of friends.

## Multifunction Stochastic

# Designing Models
Designing mathematical models is an interesting problem that requires careful selection of measures, objects and perspectives.

In addition to picking an appropriate mathematical model One interesting challenge that can already be seen with this simple model is the mapping real world phenomena into mathematical quantities. For example, consider a model where \\(x\\) is an amount of liquid \\(y\\) is the percentage that a container is filled and \\(f\\) maps these two. Such a model is fairly simple when using volume to represent liquid quantity. However, now assume that volume simply isn't known and instead weight is used to determine liquid quantity. In this case a separate \\(f\\) would need to be determined for different types of liquid due to changing densities. This simple example shows that even for the same phenomena changing the measurement can impact the model considerably.
