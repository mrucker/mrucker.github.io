---
layout   : posts
title    : Projects
permalink: /projects/
nav_index: 2
---
 {% assign projects = site.data.projects | sort: 'position' %} 
 {% for project in projects%}
	
   * [{{project.title}}]({{project.url}}) - {{project.description}}
 
 {% endfor %}
