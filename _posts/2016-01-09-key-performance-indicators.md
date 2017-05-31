---
layout: post
---
About two months ago I was asked by my CIO to design a KPI system. I'd never worked on a project quite like it but felt confident we could do it. Little did I know how complicated the task was actually going to be. What follows are the lessons I've learned on my journey to a final solution. It is worth noting I started from scratch -- so, many of my ideas may not be relevant to a project that is adding new indicators to an existing KPI system.

# Math As Programming #
I'm a programmer. When I set out to solve a problem the first thing I do is write code. I consider a problem solvable if I can envision the needed code. In the case of KPI's this seemed super easy. We want to track metric X, Y, and Z. Therefore, I need to create a new table and put in logging code to track changes to X, Y and Z. Unfortunately, capturing the data was the easy part.

To explain what I mean let's take a quick trip into mathematical history. Imagine a triangle for which we've captured two of the three interior angles and none of the side lengths. Next, assume our customer only asked us for these two angles. It might seem like we've done sufficient work, but with the information we've captured we severely limited ourselves. Instead, had we captured all three angles we could validate our results by making sure they add up to 180 degrees. As it is, we simply have to hope we're right. Or, what if someday in the future our customer needs to know the side length of our triangle. With only two internal angles there is no way we can know any side length. If we had captured even one side with our two angles we could solve for all three sides. This problem is known as the Solution of Triangles.

In a very real way, the equations that convert triangle characteristics into other characteristics are their own kind of program. For my KPI's, because I didn't define the mathematical relationships between my metrics from the beginning, I spent a lot of time logging data that couldn't be validated or transformed into other metrics. To see sample equations look below.

# Understand The Types Of Measurement #
Building on the idea of Math as Programming, my next hurdle was figuring out which metrics to capture. My customer wanted all sorts of things. How many new credits were there on any given day? What was the average revenue per credit? What was our revenue per credit for the last 4 weeks? What was the total revenue for all credits for the last 4 weeks? Lots of numbers. In the end I decided there were three kinds of numerical measurements:

 * Measurements of observation
 * Measurements of change
 * Measurements of rate, conversion or average

Of the three I should only worry about capturing measurements of observation. With every observation I also needed to capture the time we observed the measurement as our independent variable. Once I figured this out then I just had to tear their more complex requests down into their underlying observations. E.g., average revenue per credit = observation of credit amount divided by the observation of credit count. Our independent variable, time, allows us to know which revenues and credit count observations we can relate to each other.


# Drill Downs Increase Validation Time Not Coding Time #
Another problem with my coding perspective, when approaching this problem, was not understanding the cost of drill downs. Drill downs increased the amount of data we captured, even if it didn't require more code. The more data, the harder it is to find the errors if things don't roll up. Or in other words: how big do we want our hay stack to be?

To unpack this a little, imagine we are working with a data set that is rolled into three tiers. Tier one is the sum of all tier two numbers. Each tier two is the sum of their respective tier three numbers. Just so we have numbers to work with let's assume our tiers have a branching factor of ten. That means for a single tier one there would be ten tier twos and one hundred tier threes.

For each possible drill down the amount of data we have to deal with increases exponentially. If we know our tier one is off by two where could the problem be? It could be just in the tier one or any of the tier twos and tier threes. We have to validate 111 data points to find an error of 2.

On a side note, interestingly and fortunately, drill downs don't increase our percent of error. Using our above tiers let's say each tier three value is ten, making each tier two value 100 (i.e., 10 * 10) and our tier one 1,000. Now let's introduce an error rate of 20% into each tier three by changing their values to eight. That error would mean each tier two would be 80 (20% of the correct value of 100). And our tier one would now be 800 (20% off of 1,000).

# Consider The Double Entry System Of Accounting #
Another challenge I was stuck on was creating metrics that could be balanced. I wanted to sum all the amounts up in a given category and get the total result. Intuitively, I needed to know all amounts that were placed into a category in order to perform this calculation. After more reflection though, I began to realize that the amount of money in a category was the result of two separate tallies: the amount of money placed into a category minus the amount of money taken out of a category. By tracking inputs and outputs the total of all transactions in a day should always equal zero plus the amount of money that was truly inserted on that day. This insight is the crux of the Double Entry Accounting System. By tracking inputs and outputs we easily roll our account to any point in time.

# Calculate Results In Multiple Ways #
We calculate our totals in three different ways. I can't even begin to express how many errors this has revealed. It doesn't guarantee that our numbers actually match reality, but it does at least make it much less likely that there are unintended arithmetic errors in our system of accounting. This added accuracy isn't free. When there are discrepancies between our distinct totals it isn't always immediately clear which total has the error. Plus, depending on how many drill downs you've built into the KPI finding the error could entail rummaging through hundreds of thousands of small entries to find the one with a mistake. However, in our experience the errors we always found were critical and needed to be fixed now matter how much time it took.

# If Starting From Scratch Use Automated Corrections #
We started from scratch. That meant we had no solid ground to build on. After several weeks of trying to ferret out all the mistakes in our system we added a correction process.

The correction process looked something like this:
 
 1. Validate the results for one of the Total Methods (let's call it V1).
 2. When other Total Methods differ add the necessary entries to match V1. 
 3. Mark the added data as coming from the corrections process.

This process did a few things for us. One, we were able to begin immediately feeding accurate reports to our executives even though large amounts of the data came from the corrections process. We then focused on finding all the holes in our system. As we discovered them the amount of data from corrections slowly decreased. Our executives felt more confident about the numbers as they saw us slowly fill in all the missing pieces. This also helped the developers keep making progress. Before the introduction of the "corrections" it had felt like we were always in crisis mode. After adding corrections it was obvious we still had work to do but we at least had a way to show our progress and build on it. All said and done it took us about one to two months to plug all our data holes. Much longer than any of us predicted.

# Avoid Double Counting By Defining Sets #
A final major hurdle we had to overcome was avoiding double counting. The aforementioned Double Entry System of Accounting went a long ways towards solving this problem. Unfortunately, it was still an easy trap to fall into and not always obvious when we did. The multiple methods of counting helped because if one method double counted then it would be greater than the other methods. Still, even then it wasn't a freebie because differences in values could be the result of missing data and not double counted data.

The solution that finally removed this ghost from our machine was creating solid definitions of data sets. All data sets were equal to every other data set, and within one data set no entry could be counted twice. Any distinct collection of data points could be divided into as many or as few of sets as needed. What was important was not how the sets were defined, but that they were strictly honored. As an example here are three sets we used:
 
 1. [Created] + [Deleted]
 2. [Status1] + [Status2] + [Status3]
 3. [Bucket1] + [Bucket2]

And here are the various relationships between the sets:
 
 * [Created] - [Deleted] = [Status1] + [Status2] + [Status3]
 * [Created] - [Deleted] = [Bucket1] + [Bucket2]
 * [Bucket1] = [Status1]
 * [Bucket2] = [Status2] + [Status3]
 * [Bucket1] + [Bucket2] = [Status1] + [Status2] + [Status3]

An important thing to note is there is nothing fundamentally preventing overlapping sets. Using the inclusion-exclusion principle double counting can be avoided. However, because we were free to define our sets however we chose, defining our sets such that there were no overlaps simply greatly simplified our calculations.

# Sample Equations #
Hearkening back to Math as Programming here are a few basic formulas to begin to how to build a complex statistical language from basic observations.

 * x       = an earlier point in time
 * y       = a later point in time
 * O(x)    = the observation at time x
 * C(x, y) = the change between times x and y
 * I(x, y) = the amount of increase between times x and y
 * D(x, y) = the amount of decrease between times x and y
 * S(x, y) = the speed at which O(x) is changing 
 * C(x, x) = 0
 * C(x, y) = O(y) - O(x)
 * C(x, y) = I(x, y) - D(x, y)
 * C(x, y) = -C(y, x)
 * C(x, y) + C(y, z) = C(x, z)
 * S(x, y) = C(x, y) / (y - x)
