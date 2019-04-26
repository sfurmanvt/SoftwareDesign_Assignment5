# SoftwareDesign_Assignment5
<h1>Student Information</h1>

| Names           | PID            |
| --------------- |:--------------:|
| Samuel Furman   | sfurman@vt.edu |
| Lucas McCormick | mluke16@vt.edu |
| Hayden Cleek    | hmcleek@vt.edu |
| Daniel Medas    | dmedas@vt.edu  |    

<br>

<h1>Project Information</h1>

Software Design Assignment 5, Collaborative Music Composer

Use Cases Covered:

Add Comment
Remove Comment
Edit Comment
Add Profile
Edit Profile

<h1>Code Structure</h1>

Code matching our detailed class diagram is found within the BackEnd Directory.

The 25 unit tests are executed to test backend methods.

Differenes between class diagram and backend code can be found at the top of each backend file.

Front End directory is used for the demonstration of our product.

<h1>Running Tests</h1>

Code is written in python3.

You might need to run the following to resolve dependencies:

"pip install pygame"

"pip install scipy"

"pip install numpy"

run UnitTest.py from the command line using "python UnitTest.py" from within the
SoftwareDesign_Assignment5 folder.  

(use pip3 and python3 if on mac or linux or you already have python as python2)

<h1>Validation Tests</h1>

Our validation tests for the frontend portion of the code include:

<ul>
  <li>Requiring a valid email on signup</li>
  <li>Requiring all fields to be filled on the login page to sign in</li>
  <li>Requiring all fields to be filled when adding a comment on a composition</li>
  <li>Requiring all fields to be filled when editing a comment, as well as not allowing a commenter to change their name after a comment</li>
  <li>Verifying that a comment wants to be deleted upon clicking the delete button</li>
</ul>

<h1>Frontend Demonstration</h1>

In order to run the frontend
