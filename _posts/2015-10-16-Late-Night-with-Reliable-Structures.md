---
layout: post
---
Recently, I read an Atlantic article about Late Night with Seth Meyers. The piece itself was workaday, but it contained an interesting quote from Meyers about the forms of his genre (e.g. desk interviews, stand up monologues and funny-man band leaders). "I don't think these are traditions as much as they're structures that have proved they can bear comedy weight. That's the reason people keep using them."

In the last six months three software projects I support have transitioned from growth to maturity. During the transition, I've been reflecting on the software, looking for what has gone well and what hasn't. Meyers' comments resonated strongly with these refelections.

Even in a medium as foreign to software as late night comedy, one of the keys to mastery is still learning what structures to rely on. Euclid is calling out from his grave. 

Here are the software structures that have borne weight on my recent projects.

 1. **ETL**: Perhaps the best decision we ever did was to use the ETL pattern for a few early modules. In our .NET projects that meant we made three interfaces: IRead, IMap and IWrite. We have been able to reuse these interfaces again and again in all kinds of application contexts. These interfaces have become so common that I even find myself writing simple HTTP Request handlers as IMaps, a habbit that hasn't hurt at all and has, on a number of occasions, helped to migrate front end reports to back end scheduled jobs.
 
 2. **URL**: A change we made midstream was to begin using URLs for non web related resources. The first time we did this was for a project that needed to reference a specific table. We started out having three separate columns: server, database, table. Maintaining these columns was a pain. So, we decided to define our own custom url scheme table://<server>/<database>/[<schema>]/<table>. We now have tons of these (e.g. user://, email:// and grid://).
 
 3. **Unit Tests**: I know everyone says it, but I am still amazed by how many projects I've worked on without them. We knew that we'd be supporting our applications for years so we took the time to build an entire library just to make tests eaesier to write and maintain. It has paid itself off a hundred times over. At least five times a day (the approximate number of times I run the tests) I think to myself, "thank God we wrote these."
 
 4. **Universal Data Transfer Objects**: As with Unit Tests, this one took a moderate amount of upfront work and only paid itself off over years. While moving information around the system (from the database, to the web server, into cache or wherever) we started to create several small one off Data Transfer Objects that had no function other than carrying data. To remedy this we decided to create an IRow interface that was basically a simplified dictionary. We then created type converters that allow us to easily convert any object to an IRow representation and back again. No more one off DTO's needed. A secondary benefit was optimizing and unit testing our IRow implementations, making our code highly performant and dependable.
 
 5. **Composition over Inheritance**: This one I got from the good old Gang of Four. Not much to say here other than we often find ourselves regretting decisions to use inheritance. There have been times when inheritance has been nice but those times are rare and usually involve incredbily simple classes (like the URL's mentioned above). To avoid inheritance we have relied heavily on the Utility libraries mentioned below.
 
 6. **Utilities (aka Shared or Tools)**: A wise developer once told me, "not everything has to be an object. It's alright to have some one-off, static utility methods." When we are running full speed towards a deadline throwing quick helpful functions into a shared pool can be a life saver. After some time has passed we will come back to our utility methods and, with enough of them in one spot, are able to find ways to organize them into propper classes. 

Well there you have it. Those are some of the structures my team and company rely on every day to keep our software moving forward. They have become like good friends, saving us many times from dreaded, unforseen design-problems.

To rely on another weight bearing structure I will close with where I started. Meyers had a final quote on the importance of also having opportunities that let you break form as well, "It's nice right now that there are so many places that are letting you do comedy and just getting out of the way." Perhaps that is another key to success, a place to do what you know what works and a place to experiment.
