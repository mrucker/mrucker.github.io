---
layout   : page
title    : Writings
permalink: /writings/
nav_index: 3
---

  <ul class="posts">
    {% for post in site.posts %}
      <li>
        <a class="post-link" href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
