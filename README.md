# Mouse Track

This is an application written in python to monitor the interaction with the mouse.
The purpose of this application is to improve your productivity by minimize the number of times you are reaching for the mouse.


### How does it work
It listens to mouse events:
- onClick
- onScroll
- onMove

It records these events and store them into a json file.
It then displays these data into a UI.
It also displays a value called Mouse usage that is the union of these three with some business rules.

#### Event rules
- onClick -> Every click is saved into the json
- onScroll -> There are many events happening when you "scroll". We are going to limit this for one event every 3 seconds
- onMove -> Same as above

#### Mouse usage rules
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

#### Run the tests
```pip install ".[test]"```

```pytest tests```

#### Run the app
```python mouse-track.py```

#### Build the app
```pyinstaller mouse-track.spec```