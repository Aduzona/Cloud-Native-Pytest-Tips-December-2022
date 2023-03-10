[![Build](https://github.com/Aduzona/Cloud-Native-Pytest-Tips-December-2022/actions/workflows/build.yml/badge.svg)](https://github.com/Aduzona/Cloud-Native-Pytest-Tips-December-2022/actions/workflows/build.yml)

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

## Project Stucture

* Makefile `touch Makefile`
* requirements `touch requirements.txt`
* test file `test_hello.py`
* script to test `hello.py`
* Check python version `which python`
* Check Number of libraries installed `pip freeze | wc -l` this is usually much.
* Take a look at the library `pip freeze | wc -l`
* To avoid conflict for real world production environment. create virtual environment.

## Note on Virtualenv

1. Codespaces is a debian based system, so we will use `virtualenv ~/.venv`. we added it in the home directory.
2. Edit bashrc file `vim ~/.bashrc` , do `shift+g` to get to the bottom of the file, type `o` to open a new line. and put in `source ~/.venv/bin/activate` press `Esc` key and save by typing `:wq`. 
3. Open a new shell to automatically source the virtual environment.
4. Verify the right python `which python` and try `pip freeze | wc -l`. check now no package.
5. Now we can start building 100 reproducable system.

## Makefile

Upgade pip and install libraries in requirements.txt
```Makefile
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
```
run test file here it is `test_hello.py`
```Makefile
test:
	python -m pytest -vv test_hello.py
```

format python codes with black
```Makefile
format:
	black *.py
```
Lint which [pylint](https://ipwithease.com/what-is-pylint-python-programming-tool/), disable recommendations and configurations which are too noisy
only keep warning which is useful.
```Makefile
lint:
	pylint --disable=R,C hello.py
```

put them together according to execution steps
```Makefile
all: install lint test format
```

* See all the things in your Makefile `make ` press tab. thus make space tab.
* run `make install`
* check the history of the command you have run by runing `history`.
  * then find the line you want to run e.g line 12. `!12`
  * or If not there then run `pip freeze | wc -l`
* check libraries installed `pip freeze`
* copy the library versions to `requirements.txt`
* test it again by typing in `make install`
Then Add Libraries to requirements file

Then checkin the code.
```
git status
git add *
git commit -m "message"
git push
```

* Setup the Build system to actually get the installation step running.

## Build

**Build system e.g Github Actions:**

* **Cloud Native Approach**
* Test installations process (used codespaces)
  * run the Makefile commands
* Test in many different environments:
  * AWS Cloud9
  * GCP
  * Azure

We will take the installation steps and expand them to other environments.
Make new build system. We start with github actions.
You can take a look at some example of deploy process

* click Actions button.
* click Pylint under continuous Integration.
* click configure, start commit and commit.



There are 2 steps in this `build.yml` install step and lint step.
In codespaces or your favourite environment.
* Enter the github workflow `cd .github/workflows`
* We renamed the file to build. `mv pylint.yml build.yml` or `git mv pylint.yml build.yml`
* In `build.yml` change name: to `Build`
* We already have a Makefile,therefore in name:`install dependencies`,
  * Swap the run: to `make install` e.g. 
  before
  ```yml
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
  ```
  
  after
  ```yml
    - name: Install dependencies
      run: |
        make install
  ```
  
* copy pylint from `build.yml` to Makefile lint:
  copy `pylint $(git ls-files '*.py')`
  ```yml
    - name: Analysing the code with pylint
      run: |
        pylint $(git ls-files '*.py')
  ```
  to this and add extra `$` sign
  ```Makefile
  lint:
	    pylint --disable=R,C $$(git ls-files '*.py')
  ```
  * Change `build.yml` under pylint section to `make lint`
    ```yml
    - name: Analysing the code with pylint
      run: |
        make lint
    ```
* Change to `make install` in the `build.yml`
  ```yml
    - name: Install dependencies
      run: |
        make install
  ```
We have now kept all the complexity abstracted to the Makefile

## Test the lint

using `hello.py`, write a function using `make lint`


## Testing for Multi-Cloud

* AWS CloudShell
	Cloudshell is free so this is a cost effective  way of configuring your app for deployment
	* First activate ssh key see [SSH](https://github.com/Aduzona/python-for-devops-december-2022) 
	* Or Use https but use Personal access tokens (classic)(PAT) as password.(you can create PAT in github settings)
```sh

git clone git@github.com:Aduzona/Cloud-Native-Pytest-Tips-December-2022.git
python3 -m venv ~/.Cloud-Native-Pytest-Tips-December-2022
source ~/.Cloud-Native-Pytest-Tips-December-2022/bin/activate
which python
cd Cloud-Native-Pytest-Tips-December-2022
git pull
make install
make lint
```

setup testing for the python version we are on, e.g. python 3.7
```sh
vim .git
vim .github/workflows/build.yml
```
now add another python version to `build.yml`
```yml
matrix:
  python-version:["3.7","3.8","3.9","3.10"]
```
```sh
git status
git add .github/workflows/build.yml
git commit -m "adding 3.7 python"
```
if asked for congiguration
```sh
git config --global user.email "****@gmail.com"
git config --global user.name "aduzona"
git commit -m "adding 3.7 python"
git push
```

if you use https

```
username: aduzona
password: get your personal access token
```
* Cloud9


### AWS Cloud9

using https

```sh
git clone https://github.com/Aduzona/Cloud-Native-Pytest-Tips-December-2022.git
cd Cloud-Native-Pytest-Tips-December-2022
python3 -m venv ~/.venv
vim ~/.bashrc
```

inside the vim, press i to insert, :q to quit, :wq to save and quite
```
#source virtualenv
source ~/.venv/bin/activate
```

* open new terminal
* Type `which python` here it is python3
* Type `python3` to see the python version you are working with, i worked with `Python 3.7.15` then type `exit()`
* change directory to `Cloud-Native-Pytest-Tips-December-2022` and type `make install`
* run `make lint`.
* Lets create a library `mkdir mylib`
* create an init file `touch mylib/__init__`, so that python interpreter will be able to import that.
move the `hello.py` into library structure. so create a fruit routine. 

**library structure**

mylib
- __init__.py
- fruits.py
hello.py

in `hello.py`:

turn the script into command line tool or at least the begining of a command line tool`#!/usr/bin/env python` makes it executable by d
```py

#!/usr/bin/env python
```
```py
from mylib.fruity import random_fruit


if __name__=="__main__":
    print(random_fruit())# only run this if it is run as a script.

```

* make hello.py executable by doing `chmod +x hello.py`
* Just run `./hello.py` to execute.
* 

**Testing**

We now have a simple script and a library, so we can begin the test. do we want to test directory or build things out as a script.
in Pytest, you can run a test:
* in a module `pytest test_mod.py`
* in a directory `pytest testing/`
* by keyword expressions `pytest -k "MyClass and not method`
 

* Using `git mv test_hello.py test_fruity.py` Rename `test_hello.py` to `test_fruity.py` this is to match `mylib` library file `fruity.py`
* Add a test to `test_fruity.py` to test `fruity.py`

```py
from mylib.fruity import random_fruit

def test_random_fruit():
    assert "apple" or"banana" or "cherry" in random_fruit()

```
* Add a pytest-cov to requirements.py  first check version `pip freeze | grep pytest-cov`, then add to requirements.py.
* change the Makefile

From
  ```
  test:
	python -m pytest -vv test_fruity.py
  ```
  
To
```
test:
	python -m pytest -vv --cov=mylib test_fruity.py
```
* add another step to `github/workflows - build.yml` so that the test coverage will be better.

```yml

    - name: Testing Python
      run: |
        make test

```

* Create a testing directory `mkdir testing`
* move `test_fruity.py` to testing directory `git mv test_fruity.py testing/`
* change the way I run my code, to reflect this changes in Makefile

```Makefile
test:
	python -m pytest -vv --cov=mylib testing/

```
Now anything I put in the directory testing, it will be able to run by simply running `make test`

**Testing with Wikipedia library**

* Add wikipedia to `requirements.txt` and run `make install`
* Also add `ipython` to `requirements.txt` and run `make install` work well with libraries that  has interactive style.
  * `ipython` allows me to prototype things quickly.
  * `pip freeze | grep ipython` to get the version of ipython installed and add it to `requirements.py`
  * 
* Create a new library file in `mylib` with `touch mylib/wiki.py` and test file in `testing` with `touch testing/test_wiki.py`

**Using Python fire**

This can help us build test quicker, add `fire` to the requirements.py, make install, then run `pip freeze | grep fire` to extract the library version,
update the `requirements.txt`.
* rewrite `hello.py`:

```py
#!/usr/bin/env python

from mylib.wiki import search_wiki

import fire
if __name__ == '__main__':
  fire.Fire(search_wiki)
```


* run `./hello.py` this is because, we added this part `#!/usr/bin/env python` in `hello.py`
  * `./hello.py`equivalent to `python hello.py`
* you can change arguments `./hello.py --term=Warrior`


## Using Pytest

* Use libbrary style: `python -m pytest -vv --cov=mylib testing/`
* Run tests by keyword expressions: `python -m pytest -vv -k "search"`, 
  * This allows to test on only the library we are working on if we have a hugh code base
  * Testing for only fruit in `fruity.py` is done like this `python -m pytest -vv -k "fruit"`
* To run a specific test within a module: `python -m pytest -vv testing/test_fruity.py::test_random_fruit`
  * Inside `test_fruity.py` there is `test_random_fruit`
* Run tests by marker expressions: https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark

Add to Makefile:
* Profile tests: `pytest --durations=10 --durations-min=1.0`
In the Makefile
```Makefile
profile-test-code:
	python -m pytest -vv --durations=10 --durations-min=1.0
```
This means get a list of 10 test durations over 1 seconds long
Thus, pytest will not show test durations that are <1 seconds.

* Skipping `@pytest.mark.skip(reason="no way of currently testing this")`
* [Checkout Fixtures here](https://paiml.com/docs/home/books/testing-in-python/chapter07-pytest-fixtures/)

## References

* [Initialize Makefile](https://github.com/noahgift/github-actions-pytest/blob/master/Makefile)
* [Python fire](https://github.com/google/python-fire)
