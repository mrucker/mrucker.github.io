---
layout: post
---
About two months ago I was asked by my CIO to design a KPI system. I'd never worked on a project quite like it but felt confident we could do it. Little did I know how complicated the task was actually going to be. What follows are the lessons I've learned on my journey to a final solution. It is worth noting I started from scratch -- so, many of my ideas may not be relevant to a project that is adding new indicators to an existing KPI system.

#Math As Programming#
I'm a programmer. When I set out to solve a problem the first thing I do is write code. I consider a problem solvable if I can think of the code I need to write. In the case of KPI's this seemed super easy. We want to track metric X, Y, and Z. Therefore, I need to create a new table and put in logging code to track changes to X, Y and Z. Unfortunately, capturing the data was the easy part.

To explain what I mean let's take a quick trip into mathematical history. Imagine a triangle for which we've captured two of the three interior angles and none of the side lengths. Next, assume our customer only asked us for these two angles. It might seem like we've done sufficient work, but with the information we've captured we severely limited ourselves. 

If we had captured all three angles we could validate our results by making sure they add up to 180 degrees. As it is we just have to hope we're right. Or, what if someday in the future our customer needs to know the side length. Since we are only capturing internal angles there is no way we can know side lengths. If we had captured even one side with our two angles we could solve for all three sides. This problem is known as the Solution of Triangles.

In a very real way the equations that convert information about the triangle into differernt information work like computer programs. Because I didn't define the mathematical relationships between my metrics from the beginning, I spent a lot of time logging data that couldn't be validated or converted to other metrics.

#Understand The Types Of Measurement#
Building on the idea of Math as Programming, my next hurdle was figuring out which metrics to capture. My customer wanted all sorts of things. How many new credits were there on any given day? What was the average revenue per credit? What was our revenue per credit for the last 4 weeks? What was the total revenue for all credits for the last 4 weeks? Lots of numbers. In the end I decided there were three kinds of numerical measurements:

 * Measurements of observation
 * Measurements of change
 * Measurements of rate, conversion or average

Of the three I should only worry about capturing measurements of observation. With every observation I also needed to capture the time we observed the measurement as our independent variable. Once I figured this out then I just had to tear their more complex requests down into their underlying observations. E.g., average revenue per credit = observation of credit amount divided by the observation of credit count. Our independent variable, time, allows us to know which revenues and credit count observations we can relate to eachother.


#Drill Downs Increase Validation Time Not Coding Time#
Another problem with my coding perspective, when approaching this problem, was not understanding the cost of drill downs. Drill downs increased the amount of data we captured, even if it didn't require more code. The more data, the harder it is to find the errors if things don't roll up. Or in other words: how big do we want our hay stack to be?

To unpack this a little, imagine we are working with a data set that is rolled into three tiers. Tier one is the sum of all tier two numbrs. Each teir two is the sum of their respective tier three numbers. Just so we have numbers to work with let's assume our tiers have a branching factor of ten. That means for a single tier one there would be ten tier twos and one hundred tier threes.

For each possible drill down the amount of data we have to deal with increases exponentially. If we know our tier one is off by two where could the problem be? It could be just in the tier one or any of the tier twos and tier threes. We have to validate 111 data points to find an error of 2.

On a side note, interestingly and fortunately, drill downs don't increase our percent of error. Using our above tiers let's say each tier three value is ten, making each tier two value 100 (10 * 10) and our tier one 1,000. Now let's introduce an error rate of 20% into each tier three by changing their values to eight. That error would mean each tier two would be 80 (still off by 20% of the correct value of 100). And our tier one would now be 800 (20% off of 1,000).

#Consider The Double Entry System Of Accounting#
More to come...

#Calculate Results In Multiple Ways#
More to come...

#If Starting From Scratch Use Automated Corrections#
More to come...

#Avoid Double Counting By Defining Sets#
More to come...

#Sample Equations#

 * O(x)    = the observation at time x
 * C(x, y) = the change between times x and y
 * I(x, y) = the amount of increase between times x and y
 * D(x, y) = the amount of decrease between times x and y
 * C(x, x) = 0
 * C(x, y) = O(y) - O(x)
 * C(x, y) = I(x, y) - D(x, y)
 * C(x, y) = -C(y, x)
 * C(x, y) + C(y, z) = C(x, z)
