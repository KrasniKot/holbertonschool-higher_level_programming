# JavaScript DOM manipulation

## Requirements:
* Allowed editors: All of them.
* All your files will be interpreted on Chrome browser (version 57.0 or later)
* All your files should end with a new line
* A mandatory README.md file with meaningful information about the content, should be placed at the root folder of the project.
* Your code should be semistandard compliant
* You are not allowed to use var
* HTML should not reload for each action: DOM manipulation, update values, fetch data…

### Task 0: Color Me
Write a JavaScript script that updates the text color of the `header` element to red (`#FF0000`):
* You must use `document.querySelector` to select the HTML tag

### Task 1: Click and turn red
Write a JavaScript script that updates the text color of the `header` element to red (`#FF0000`) when the user clicks on the tag with id `red_header`:

### Task 2: Add \`.red\` class
Write a JavaScript script that adds the class `red` to the `header` element when the user clicks on the tag with id `red_header`

### Task 3: Toggle classes
Write a JavaScript script that toggles the class of the `header` element when the user clicks on the tag id `toggle_header`:

The `header` element must always have one class: `red` or `green`, never both in the same time and never empty. If the current class is `red`, when the user click on id `toggle_header` element, the class must be updated to `green` ; and the reverse.

### Task 4: List of elements
Write a JavaScript script that adds a li element to a list when the user clicks on the element with id add_item:

The new element must be: <li>Item</li> The new element must be added to the ul element with class my_list

### Task 5: Change the text
Write a JavaScript script that updates the text of the header element to New Header!!! when the user clicks on the element with id update_header

### Task 6: Star wars character
Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

The name must be displayed in the HTML tag with id character.
You must use the Fetch API.
You probably should read something about usign Promises later.

### Task 7: Star Wars movies
Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

All movie titles must be list in the HTML ul element with id list_movies
You must use the Fetch API.

### Task 8: Say Hello!
Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML element with id hello.

The translation of “hello” must be displayed in the HTML element with id hello
Your script must work when it is imported from the <head> tag

### Task 9: List, add, remove
Write a JavaScript script that adds, removes and clears li elements from a list when the user clicks:

The new element must be: <li>Item</li>
The new element must be added to the element with id my_list
When the user clicks on the element with id add_item: a new element is added to the list
When the user clicks on the element with id remove_item: the last element is removed from the list
When the user clicks on the element with id clear_list: all elements of the list are removed You script must work when it imported from the head tag Please test with this HTML file in your browser:

## Author
Emanuel Trias
