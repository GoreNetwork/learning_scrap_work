<H1> Pimarty parts of a website </H1> 

*  HTML has the page elements
*  CSS will be the style elements
*  Bootstrap will provide the auto styling and components through CSS and JS
* useful links:
    * https://codepen.io/pen/

<H3> Things we'll need to be able to do in the webpage using Flask</H3>

*  Accept info from a user
*  Get info from a DB
*  Create/Update/Remove info from said DB
*  Give info back to user

<H1> HTML </H1> 

comments look like this ```<!-- comment here -->```

<H2> Tags </H2>

things inside a set of brackets that start/stop an effect (like the H1 tags in MD)

*  Head
  * Contains meta data
    * Link to CSS files
    * Link to JS files
    * title tag (what appears on the tab in the browser)

* Body
  * H1-6 work the same way as they do in markdown
  * you need a p tag ```<p> </p>``` tag for paragraphs (line returns and such)
  * ```<br>``` gives a line return between items
  * Bold things with the strong tag
  * Italic with em tag
  * make lists with ul and ol tags, these can be nested
  * sooo many of these!!
  * div tag used with CSS to format things inside that tag a certian way, these are generally large sections
  * spans are used for smaller sections you want to apply formatting to



<H2> HTML Forms </H2>
How the website accepts info use "form" tags to setup a form, and "input" tags to accept user info.  All major form element already has a input tag attribute.  "submit" input types adds a buttion for form submission

```<input type="text" name="" value="" placeholder="Your username here">```

* input type = text, password, other input types
  * diffrent types do different things
    * email makes sure it at least looks like an email
    * password doesn't show what you put in
* name = the identifier of this field for when you hit submit
* value = what is sent back to the server when you submit the info (generally not defined in code)
* place holder: text to say what the box is, but not a default vaule

<H3>Sumit types</H3> 

```<input type="submit" name="" value="Enter">```.  
2 main types: 
* GET: requets info from the website 
  * Send back info to the Action URL
* POST: Sending data to site to process

<H1>CSS</H1>

Changes style attributes
* Color
* Background
* Borders, etc

In generall you have a .css file that is refrenced in the html header like this:  ```<link rel="stylesheet" href="test.css">```.  Inside that file you're refrencing things like the header and saying what you want to do with said header: font size, background etc.  More often you'll be refrencing the div id 


```    
<div class="test_div" id="test_div">
        <p>Here's a div with a class</p>
        <p>Here's <span class="test_span"> a span section</span> inside the div</p>
    </div>
```
like this
```
.test_div{
    background-color: rgb(213, 11, 183);
    color: rgb(0, 0, 0);
}
```
Then just apply that test_div tag to any section you want formated that way.  Most anything type can take an id, however some types are refrenced diffrently in CSS: a div id is refrenced starting with a ".", however a p tag's ID is refrenced with a #

<h1>Bootstrap</h1>
Big CSS / Java file: prebuilt/easy to use things we can put in our website documentation at www.getbootstrap.com.  Just as you can link to a local CSS file you can link to a webpage with CSS on it via a CDN (content delevery network)

```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
```
or 
```
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
```

check boxes:  https://getbootstrap.com/docs/5.3/forms/checks-radios/

<h1>Python stuff</h1>

create venv with `conda create --name [name of venv]`

create with a particular python version `conda create --name [name of venv] python=3.9`

See a list of your envs with `conda env list`

<h1>Flask stuff</h1>

<h2>Routing</h2>

The app.route: determines the url path to the function (view) of the website
@app.route('/')  # This is the root of the website (http://127.0.0.1:5000/)
@app.route('/page_2') # this would be http://127.0.0.1:5000/page_2

```
@app.route('/')
def index():
    return '<h1>Kick the puppy!!</h1>'
# the functions "index" and "page_2" define how these pages are built
@app.route('/page_2')
def page_2():
    return '<h1>Kick the puppy even more!!</h1>'
```