
# ByteSized Trades
## A Full Stack Development Project by Edward Stanley
Bytesized Trades is a website with one goal in mind, to give players of the game 'Pokemon' a forum in which they can request pokemon they want added to their team. 

The current setup of the site is that the owner holds a database worth of pokemon they are looking to trade off, so instead of asking around aimlessly, those trainers now come to him. The website has the ability for the owner to add pokemon, edit them, and delete them if they no longer exist.

The users are able to access the website anomynously, or create an account which gets verified by email, and add pokemon they want to request to the bag. Due to the nature of this, the same id pokemon cannot be added by the user twice as that would be redundant. 
The user can then checkout those pokemon by providing their own trainer code and email (Else the user would have no way to communicate with them to trade).
#
## User Stories
### The Owner -

#
## Existing Features
I will be covering the features on an app by app basis
### The Base Directory / Home App
- Contains a structured layout thatnks to Bootstrap which was the majority of the stylings for this project too
- Contains the formatting necessary to deploy the website to Heroku
- Contains a settings app which takes Heroku's Config Vars for the more sensitive links which helps secure the site
- Contains a static folder which is accessed and saved in Google Cloud in order to give additional stylings at points in the project
- Contains a structured nav with collapsable links which keeps screen coverage minimal
### The Goods App
- The Ability to add a pokemon if you are a superuser
- The Ability to edit a pokemon if you are a superuser
- The Ability to delete a pokemon if you are a superuser
- On a regular load iterates through all the pokemon in a database, displaying them all in a card like format with the name, picture, types, level, and the pokemon's owner
- On a load specified by the type buttons, filters the list to streamline the users experience to find what they want. In terms of pokemon types is a very important factor.
- On a load specified by the search bar, filter the list to any pokemon containing the submitted string, again this streamlines the experience for the user allowing them to get what they want quicker.
- When a pokemon's image is clicked, it takes the user to a more detailed view of its stats, as well as presenting the user with the option to add the pokemon to their bag.
### The Bag App
- The ability to view what pokemon the user has selected thus far, and a breakdown of each one, to let the user keep track easier.
- The ability to remove a pokemon from the bag if the user deems they dont want it anymore
- The ability to send the user to checkout the pokemon they have so far, or return to the rest whilst keeping the session open so that the user doesnt lose their additions
### The Profile App
- Uses Allauth to allow for secure sign in, sign out and secure general activities
- Uses Allauth's authentication system by sending the User a confirmation email
- Allows for protection against non admin users from accessing features they shouldnt such as adding products
### The Checkout App
- Takes a form consisting of the user's inputs, whether anomynous or not, and generates a success page provided that the form is valid.
- Uses Stripe as an optional donation if the user wishes to contribute towards the project, payments successfully come up through stripes system
- Gives a clear breakdown of the order on success reminding the user what they have requested from the owner

### Features yet to be added
- Greying out the add to cart button if the user already has that product in their bag
- As set up by the foreign key in model Info, the ability for the user to make their own pokemon and add them to the system. 
They would only be able to delete and edit their own. This wasnt implemented due to unsurity if it would contradict L03.3
- An alternate to the checkout system where the user has an option of adding one of their pokemon to the order form, which would then have the details sent to the owner forming a better trade. This wasnt added due to the point above.
- The Info model and early commits have a price assigned which I initially wanted to implement however opted for the donation due to time. It still being there allows me to adapt it in future. The same occurs with the abilities which again would be nice to include however editing 801+ fixtures would've taken a while 

## Testing
Over the project there were multiple small flaws such as missing an s off a variable stopping the ListInlineItem from going inline, however I would like to identify some of the key problems I had whilst working on this website:

### Two Foreign Keys for Info
The Info model contains the variables type1 and type2, which can range from  
1-18 usually due to 18 types being in the game. The problem however was that type2 didnt always have a value hence couldnt link up with a foreign key. 
To solve this I created a 19th category with a value of 19 as essentially a null category. Any items which initially didnt have a second type were assigned to it to avoid any null errors with the key.

### Images not showing on mobile


#
## Deployment
I was unable to deploy the project via Heroku, the app refused to connect. Upon attempts to log in via Heroku it would state there was an IP error. I was unable to fix this in time for submission unfortunatley.

#
## Acknowledgement

A huge thank you to the Student Care team, especially Kieron, whom without which this definitely wouldn't have been possible. It has been a nightmare of a month with illness and bereavement, and thankfully now I have a valid project to submit.

Also a thank you to Igor, who helped me figure out why the ListItemInline wasnt inline in the admin
#