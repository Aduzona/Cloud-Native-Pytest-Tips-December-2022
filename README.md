# Cloud-Native-Pytest-Tips-December-2022

Pytest repo, covering best practices
Make Projects more reproducable, set it up on different environment.

Avoid stating with Laptop first:  Starting with a cloud based environment like.
* Github codespaces.
* AWS Cloud9
  
![Buil System](Images/Build_System.png)

**Scaffold**
Skaffold handles the workflow for building, pushing and deploying your application, allowing you to focus on what matters most: writing code [scaffold.dev](https://skaffold.dev/)

**Key Terms in Testing**

* requirements: contains list of packages and versions, this is 100% reproducable.
* Makefile: it is a linux based file,has commands that automates tasks.
* Docker Containers: 
  * Dockerfile is a plain text file that defines what will be in run time when you do buil the docker format container.
  * Container: Includes Runtime and code/software.
These are done in Virtual env or/and docker, this is to reproduce same structure.

**Kaizen== Devops**

Means continuous Improvement, You can be in 3 states: 

* Degrading: No automation
* Same: remains in same state
* Improving: When automated, updates could be performed.

