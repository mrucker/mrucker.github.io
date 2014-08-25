---
layout   : page
title    : Writings
permalink: /writings/
nav_index: 3
---
 {% for post in site.posts %}
   * [{{post.title}}]({{ post.url }})
 {% endfor %}
