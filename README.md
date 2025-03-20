# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Features
*CodeJester* is a Python package designed to make coding more fun with simple text transformations and feel-good messages. It includes four features: reversing text, converting words into leetspeak, generating random compliments for developers, and generating random fortunes for developers. 

The **Reverse Text** function flips any string backward, giving a fun twist to your input. The **Leetspeak** converter transforms text into a stylized hacker-style format (e.g., "hello" becomes "h3ll0"). The **Developer Compliments** feature provides developers with encouraging messages like "Your code is a masterpiece in the making" or "You're a debugging pro," based on the type of compliment you choose (debugging, coding, or motivational). Inspired by fortune cookies, the **Fortune** function provides developers with fortunes like "Your potential is limited only by your imagination" or "First, solve the problem. Then, write the code," based on a chosen theme (inspirational, funny, or programming).  

Now matter which feature you decide to use, *CodeJester* adds a bit of positivity and entertainment to a developer's workflow.

***
## A badge showing the result of the latest build/test workflow run

***
## A link to *CodeJester*'s page on the PyPI website

***
## How a developer who wants to import your project into their own code can do so - include documentation and code examples for all functions in your package and a link to an example Python program that uses each of them.

***
## How a developer who wants to contribute to CodeJester can set up the virtual environment, install dependencies, and build and test your package for themselves

1. Fork and Clone the Repository: Start by forking the repository on GitHub and cloning it locally:
```
git clone https://github.com/yourusername/codejester.git
cd codejester
```
2. Set Up the Virtual Environment: Use pipenv to manage dependencies and virtual environments. Install pipenv (if you haven’t already) and set up the environment
```
pip install pipenv
pipenv install --dev
pipenv shell
```
3. Install Dependencies: Ensure all required dependencies are installed with `pipenv install`
4. Build and Test the Package: Before making any changes, run tests to ensure the package is working correctly by running `pytest`
5. Create a New Feature Branch: Before making any changes, create a new branch with `git checkout -b feature-new-function`
6. Make Your Changes and Commit: Once you have implemented your changes, stage and commit them:
```
git add .
git commit -m "Added new feature"
```
7. Push Your Changes and Create a Pull Request: Push your changes to your forked repository with  `git push origin feature-new-function`

***
## *Stamped and Sealed* Teammates
- [Ethan Yu](https://github.com/ethanyuu910) 
- [Isha Gopal](https://github.com/ishy04)
- [Jennifer Huang](https://github.com/jenn.hng) 
- [Lana Davydov](https://github.com/lanadavydov)
- [Tarini Mathur](https://github.com/tmathur2005)

***
## Instructions for how to configure and run all parts of CodeJester for any developer on any platform

***
## Instructions for how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run

***
if there are any "secret" configuration files, such as .env or similar files, that are not included in the version control repository, examples of these files, such as env.example, with dummy data must be included in the repository and exact instructions for how to create the proper configuration files and what their contents should be must be supplied to the course admins by the due date.
