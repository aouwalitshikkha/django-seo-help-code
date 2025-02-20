# Solving Cannonical Problem

The Code will solve the problem of Cannonical Pagination issues in Search console

![](duplicate_issue_gsc.jpg)

place the below code in your template 

```python
<link rel="canonical" href="{{ request.scheme }}://{{ request.get_host }}{{ request.path }}" />
```