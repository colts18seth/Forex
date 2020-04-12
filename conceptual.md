### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
 * Python is strongly typed, has a big library of modules to use and it is mostly used in backend programming


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you 
  can try to get a missing key (like "c") *without* your programming 
  crashing.  
 1. you can use the get() method//dict.get("c", 3)
 1. you can set up a default value//dict.setdefault("c", 3)


- What is a unit test?
 * a unit test is testing an individual unit in a program


- What is an integration test?
 * an integration test is testing multiple units of a program together


- What is the role of web application framework, like Flask?
 * frameworks save a tremendous amount of time and effort building apps  
 developers can use code thats already made, instead of re-inventing the wheel


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
 * You wouldn't want the route to get too long.  Something very broad would be ideal for a route, but when it gets down to smaller details query params seem like a better fit.


- How do you collect data from a URL placeholder parameter using Flask?
 * variable route names are created by placing <> around the placeholder and when the route is hit, the name is passed into the routes function

- How do you collect data from the query string using Flask?
 * it is taken from request.args["placeholder"] or request.args.get("placeholder")

- How do you collect data from the body of the request using Flask?
 * you can collect the body data using request.get_json()

- What is a cookie and what kinds of things are they commonly used for?
 * cookies are a way for the browser to "remember" small things. A simple example would be a banner that shows at the top of a page.  If that banner is closed, there could be a cookie saved that tells the browser not to show that banner again for the current user.

- What is the session object in Flask?
 * session is used for "remembering" certain things for the user.  Such as, if playing a game you might want to save the score to the session.  The session is emptied when the server is stopped or the browser is closed. 

- What does Flask's `jsonify()` do?
 * jsonify() helps developers convert data to json.  Its used to prevent easy errors

- What was the hardest part of this past week for you?
 * The hardest part was figuring out how to get axios post request and flask working together.

 
- What was the most interesting?
 * The amount of modules Python is equipped with