---
layout: post
---
Microsoft, over the life of the .NET framework, has used many different Asynchronous patterns. This post will look at three of them and hopefully, in the process, shed some light on options available to .NET developers trying to write their own asynchronous code.

#Begin/End Pattern#

In .NET 1.x Microsoft used the Begin/End pattern. This pattern had three major pieces:

1. The Begin method. This method begins an operation asynchronously and creates an IAsyncResult token for the operation.
2. The IAsyncResult. This token indicates if an asynchronous operation is finished. It is consumed by the End method.
3. The End method. This method returns the result of an asynchronous operation. If necessary, it will block execution until the result is ready.

A good example of this pattern is BeginInvoke and EndInvoke on delegates.

#Async/Completed Pattern#

In .NET 2.0 Microsoft used the Async/Completed pattern. This pattern also has three major pieces:

1. A Method with an 'Async' suffix. This method starts the asynchronous operation
2. An event with a 'Completed' suffix. This event is fired when the asynchronous operation completes.
3. An EventArgs. This is passed to the Completed event and contains the result of the operation and any exceptions that may have occurred.

A good example of a class using this pattern is WebClient

#Async/Await Pattern#

In .NET 4.0 Microsoft began using the Async/Await pattern. This pattern also also has three major pieces:

1. 'async' keyword in the signature of the method that will be making the asynchronous call.
2. 'await' keyword in front of an awaitable operation (typically a Task but doesn't have to be).
3. Task or Task<T> return type from the async method. Token used by the caller to know when the async method has completed.

A good example of a class using this pattern is HttpClient.

#Sample Code#

* [Three Asynchronous Patterns][1]

#Sources#

* [C# In Depth Third Edition by Jon Skeet][2] Page 463

[1]: https://github.com/mrucker/ThreeAsynchronousPatterns
[2]: http://www.amazon.com/Depth-3rd-Edition-Jon-Skeet/dp/161729134X/