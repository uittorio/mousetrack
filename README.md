# Track Mouse

This is an application written in python to monitor how often the mouse is used.
The purpose of this application is to minimize the number of times the mouse is use to improve a developer experience through shortcuts


### How does it work
The application listens to the mouse event
- onClick
- onScroll
- onMove

It records these events and store them into a json file.
It then displays these data into a UI.
It also displays a value called Mouse usage that is the union of these three with some business rules. 

#### What are these rules
A mouse usage is considered valid when
- Any of the three events, onClick, onScroll, onMove happened 
- As long as you keep using the mouse without using the keyboard it counts as 1
- It will count as 1 if you stop using the mouse or the keyboard for 4 seconds

#### Examples
1. I have a webpage open and I 
   - Move the mouse 
   - Click to open a link.
> Count as 1.
> You've just interacted with the mouse and then stop doing anything else

2. I have a webpage open and I
 - Move the mouse
 - Click to open a link
 - Scroll the page
 - Click on a search bar
 - Type "find restaurants"
 - Move the mouse to click the new link

> Count as 2.
> You've interactive with the mouse, then with the keyboard and finally with the mouse again.

3. I have my favourite IDE open and I
 - use thousands of shortcuts to do magic stuff 
 - move the mouse cursor to navigate through the files
 - use another shortcut
> Count as 1.
> You've interactive with the mouse once keyboard click

### Run the application locally

#### Install dependencies
```pip install .```

#### Run the tests (Work in progress)
⚠️ 👷👷 ⚠️    

#### Run the app
```python main.py ```