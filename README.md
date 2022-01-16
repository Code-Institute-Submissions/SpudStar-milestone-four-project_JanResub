
# ByteSized Trades
## A Full Stack Development Project by Edward Stanley
Bytesized Trades is a website with one goal in mind, to give players of the game 'Pokemon' a forum in which they can request pokemon they want added to their team. 

The current setup of the site is that the owner holds a database worth of pokemon they are looking to trade off, so instead of asking around aimlessly, those trainers now come to him. The website has the ability for the owner to add pokemon, edit them, and delete them if they no longer exist.

The users are able to access the website anomynously, or create an account which gets verified by email, and add pokemon they want to request to the bag. Due to the nature of this, the same id pokemon cannot be added by the user twice as that would be redundant. 
The user can then checkout those pokemon by providing their own trainer code and email (Else the user would have no way to communicate with them to trade).
#
## User Stories
### The Owner -
    - Wants to advertise all the pokemon they have
    - Wants people to be able to add them to the bag
    - Wants to be able to contact the user after the request is made
    - Might want to get a bit of money from each request

### The Unauthorized user -
    - Wants to advertise all the pokemon they have
    - Wants people to be able to add them to the bag
    - Wants to be able to contact the user after the request is made
    - Might want to get a bit of money from each request

#

### The Authorized user -
    - Wants to advertise all the pokemon they have
    - Wants people to be able to add them to the bag
    - Wants to be able to contact the user after the request is made
    - Might want to get a bit of money from each request

#
## Wireframes
The following wirefrane was made in Balsamiq  
[Please Click Here.](read_me_resources_/wireframe_ms3.pdf)

The wireframe can also be found in the readmeassets folder included in this project
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
- Whilst it cannot render them currently, I unfortunatley ran out of time, it returns the order number to the profile so users can see their past order numbers. Ideally it would show them a breakdown but I decided to keep it in as it proves there is a point to logging in
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
- The ability to filter respective to a specific stat i.e hp. I unfortunatley ran out of time to do any more filtering

## Testing
Over the project there were multiple small flaws such as missing an s off a variable stopping the ListInlineItem from going inline, however I would like to identify some of the key problems I had whilst working on this website:

### Two Foreign Keys for Info
The Info model contains the variables type1 and type2, which can range from  
1-18 usually due to 18 types being in the game. The problem however was that type2 didnt always have a value hence couldnt link up with a foreign key. 
To solve this I created a 19th category with a value of 19 as essentially a null category. Any items which initially didnt have a second type were assigned to it to avoid any null errors with the key.

### Loaded migrations stopping progress
A huge frustration through this was when a migration and data was already loaded for a model, it very much did not like changes to it. Hence in order to run the migration I would often have to start a new workspace, reinstall everything using pip3, and then migrate. I tried searching on the web for a quicker way to do this to no avail.

### Images not showing on mobile
After finally getting the Google Cloud working (which was an ordeal in itself) the images for all the links were no more. Turns out IOS doesn't seem to like my website, and unfortunatley I couldnt find a work around for this

### Images not showing on mobile
Other known unfixed bugs:
- On smaller screens the padding from the top doesnt update correctly causing overlap, this isnt as much of an issue on larger screens but it is still annoying
- The footer keeps popping up which isnt ideal
- A few forms get shifted to the left/right

While those lead to a bad user experience, the views it happens on makes very little difference to what the user usually encounters. All the main views are working as intended, and visual tricks like the collapsable with links help a lot for the user experience overall

## Testing User Stories

#
## Deployment
The steps on how to deploy the project for yourself are outlined below:


#
## Credits
### General Code Layout
For the purpose of this project I referred to and used authentication from the Code Institute Chris's Boutique ADO. However I believe I have differentiated the project enough through my own bootstrap analysis, and database scheme in order to support my own user stories.
### Code Specifics
A major part of the borrowed code is for google cloud to access my static files.
The steps I took and tried to better fit me is from [here.](https://stackoverflow.com/questions/40127675/serve-static-files-from-google-cloud-storage-bucket-for-django-app-hosted-on-gc)
### Data for Databases
The Json for Info fixtures was largely manipulated by myself however the origonal source of the data was from [here.](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_I))
I copied and pasted the tables into Excel, and then used Windows Powershell to convert it to Json, plus minor text formatting to make it a viable fixture.
### Media
The sprites for each pokemon are gotten from [here.](https://veekun.com/dex/downloads), There was not much editing to speak of.

The images for each pokemon type are gotten from [here.](https://brickbronze.fandom.com/wiki/Appendix:Pok%C3%A9mon_Types), This took a lot more editing as they were all in the same image. I also resized them so the default maximum size would be suitable for me.

The image for the repeating background was made by myself in Gimp, an image editing software, which I also used to edit the above mentions. 

I should mention however that despite the source links all of the images are using assets from Nintendo's Pokemon.
#
## Acknowledgement

A huge thank you to the Student Care team, especially Kieron, whom without which this definitely wouldn't have been possible. It has been a nightmare of a month with illness and bereavement, and thankfully now I have a valid project to submit.

Also a thank you to Igor, who helped me figure out why the ListItemInline wasnt inline in the admin

A lot of work has gone into this project, and I do wish that I had more time to flesh it out, but I am happy with the result and I believe it meets all of the criteria.
#