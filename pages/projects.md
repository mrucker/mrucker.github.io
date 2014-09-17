---
layout   : posts
title    : Projects
permalink: /projects/
nav_index: 2
---

 {% for project in site.data.projects | sort 'position' %}
	
   * [{{project.title}}]({{project.url}}) - {{project.description}}
 
 {% endfor %}
