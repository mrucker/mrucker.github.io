---
layout   : posts
title    : Writings
permalink: /writings/
nav_index: 3
---

 {% for post in site.posts %}
   
   {% if post.external_url %}
   * [{{post.title}}]({{ post.external_url }})
   {% else %}
   * [{{post.title}}]({{ post.url }})
   {% endif %}

 {% endfor %}

