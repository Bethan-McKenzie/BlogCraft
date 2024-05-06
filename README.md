# Blogcraft (Capstone Project for Code Insitute - Coleg Gwent Bootcamp)
![Image of the Blogcraft homepage](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/Homepage%20of%20Blogcraft.png)

Blogcraft is a site which aims to bring together the Minecraft community! They can share their builds, any bugs found, Minecraft content creators they like and so much more. The idea stemmed from my love of the game and the fact that there's not really a place dedicated to just Minecraft like this.

## Purpose

This website has been built using the Django framework for functionality with both frontend and backend.

Blogcraft allows the user to register, create posts as well as have a profile which can have the information (such as username and email address) changed and saved.
Currently there are three bugs in the site that I am unable to fix, due to time restraints caused by uncontrollable circumstances, and thus do not allow the user to delete their own posts, show the images that a user uploads when creating a post or allow users engage with the community through comments on posts (more information [here]() in the bugs section).

The link to the live site can be found [here](https://bethanmckenzie-blogcraft-b4a04edf4612.herokuapp.com)

<hr>

## Features

## Homepage

A fully responsive homepage featuring posts that users have made inside cards that adapt their size based on multiple factors such as, the amount of text needing to be displayed, the size of the image for the post and the size of the screen the user is viewing on.

![Image of Blogcraft Desktop Homepage](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/Homepage%20of%20Blogcraft.png)

![Image of Blogcraft Tablet Homepage](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/Blogcraft%20Homepage%20Tablet.png)

![Image of Blogcraft Mobile Homepage](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/Blogcraft%20Homepage%20Mobile.png)

## Navbar

![Image of navbar with user not logged in](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/Navbar%20of%20user%20not%20logged%20in.png)

Featuring a navbar that changes options depending on if the user is logged in or not throughout the site and what areas they can access depending on that status.

![Image of navbar with user logged in](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/Navbar.png)

The navbar is also responsive throughout ensuring users easy navigation throughout the site no matter what device they're accessing from changing to a dropdown menu for both tablet and mobile devices.

![Image of responsive navbar](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/dropdown-navbar.png)

## Footer

Throughout the site the footer remains constant and allows users to follow official Minecraft accounts on different platforms with ease.

![Image of the site footer](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/footer.png)

## Login

Users can eaily navigate to the login page where they are met with a prompt for them to sign in or if they have yet to register a link to sign up

![Image of sigh in page](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/sign-in.png)

The interface allows for users to click the 'remember me' checkbox to have the site remember their login details and quickly get into their account with no hassle!

![Image of sign up page](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20sign%20up.png)

Although unstyled the sign up page works perfectly for functionality.


## My Profile

When loggedin users can access their profile that for now only contains their username, email and when they signed up however future features are planned!

![Image of my profile page](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/my-profile.png)

The page also contains a button to redirect the user to the edit profile page where they can edit their username and or email address and save those changes.

![Image of edit profile page](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20edit%20profile.png)

## Creating a post

Creating a post is extremely simple for the users, all they have to do is be logged in, navigate to the correctly marked page via navbar, fill in the relevant information and hit post!

![Image of create a post page](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20create%20a%20post.png)

## Post Detail

When the user clicks on the post they wish to see they're able to read what the user has posted from the title down to the last period. The user is able to see how many comments the post has at the top under the description text and were they to scroll down they can join the conversation with other members in the comments section of that particular post.

![Image with the details of the post](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20post%20detail.png)

## Comments

Each post detail page has a comments section at the bottom where users will be able to engage with the community. There is a current bug where it's not fully functional right now, more about this [here]().

![Image of comments section](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/write-comment.png)

<hr>

## UX & Design

The colours of the site were chosen to fit the goal of users knowing what the site is and what it's about. Eerie Black, Kelly Green and Gray are used throughout Minecraft's official website and would be very familiar to those who have viewed that site before. The White Smoke was chosen as a white that isn't harsh on the eyes but still provides high contrast for ultimate accessability.

![Image of colour palette](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/BlogCraft%20colour%20palette.png)

All images used throughout the site are completely copyright free as they came from my own gameplay of Minecraft and were screenshots I had done myself.

## Wireframes
## Homepage
![Image of Homepage Wireframe](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20wireframe%20homepage.png)
## Sign In
![Image fo sign in wireframe](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20wireframe%20sign%20in.png)
## Sign Up
![Image fo sign up wireframe](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20wireframe%20sign%20up.png)
## My Profile
![Image of my profile wireframe](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20wireframe%20user%20profile.png)
## Create Post
![Image of create a post wireframe](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20wireframe%20create%20post.png)
## Post Detail
![Image of post detail wireframe](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20wireframe%20view%20post.png)
## Comments
![Image of comments wireframe](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20wireframe%20comments.png)

<hr>

## Database

![Image of Blogcraft ERD](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20ERD.png)
![Image of model being implimented](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blog%20model.png)

<hr>

## Development

Using a kanban board that can be found [here](https://github.com/users/Bethan-McKenzie/projects/2/views/1) I was able to keep track of what progress was being made towards the completeion of the site.

<hr>

## Testing

Blogcraft has been tested on multiple devices such as PC, Tablet and Mobiles to ensure the desired outcome across all devices.

## HTML
[The Markup Validation Service](https://validator.w3.org) was used to check the validation and compliancy of all my pages. There was an issue brought up on the My Profile page with the efit my profile button however, due to time constraints it couldn't be changed and will be changed in the next iteration to meet HTML standards.

## CSS
Blogcraft has passed CSS validation using [The CSS Validation Service](https://jigsaw.w3.org/css-validator/)

![Image of CSS Validation](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/W3C%20CSS%20validation.png)

## Lighthouse

Blogcraft was checked using Lighthouse to ensure accessability and standards are met.

![Image of Lighthouse Testing](https://github.com/Bethan-McKenzie/BlogCraft/blob/main/media/blogcraft%20lighthouse.png)

## Browser Compatibility

Blogcraft has been checked on multiple browsers such as Safari, Google Chrome and Opera GX to ensure that the site meets expectations across a range of different browsers for best user experience.

<hr>

## Future Features

<hr>

### Known Issues & Bugs

## Bugs

There are currently three bugs in the site that due to time restaints couldn't be solved.

- When a user creates a post and uploads and image with it, the image doesn't get uploaded to Cloudinary so a placeholder image is shown on the site instead.

- The delete post functionality isn't quite there as, when the user who made the post clicks the delete button, it doesn't delete the post.

- When a user comments on a post a 404 page is displayed however, if you were to go back on the post the comment is there.

I believe that in the next iteration of the project all these bugs could be solved with some time that I unfortunately didn't have.

## Issues

- Currently users can upload image files of any size, this could slow the website down in future and compression or cropping of user-uploaded images should be implemented to solve this.

- Currently users are unable to add alt-text to images that they upload. This presents an accessibility problem and should be remedied to ensure the website reflecting an inclusive community is truly inclusive in it's own design.

<hr>

## Technologies

## Languages

Python, JavaScript, HTML, CSS

## Programs, Frameworks and Libraries

[Git](https://git-scm.com)
[GitHub](https://github.com)
[GitPod](https://dashboard.heroku.com/apps)
[Heroku](https://dashboard.heroku.com/apps)
[Bootstrap 4.1.3](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
[FontAwesome](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
[Django](https://www.djangoproject.com)
Django AllAuth
[PostgreSQL](https://www.postgresql.org)
[ElephantSQL](https://www.elephantsql.com)
[Cloudinary](https://cloudinary.com)
[Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template)
[Balsamiq](https://balsamiq.com)

<hr>

## Deployment

## Github

After making a new respository for my capstone project from the [CI template](https://github.com/Code-Institute-Org/gitpod-full-template), I created a workspace in gitpod where all of my development took place.

## Development Environment Set Up

For ease of set up and to ensure nothing was forgotten I followed along with Kevin-CI's video that was made for our third hackathon to ensure that no future problems would come from the environment being incorrectly set up.

## Heroku

Heroku is used to host Blogcraft. Heroku is a container-based cloud Platform for building, deploying and managing apps. This project was first deployed to Heroku in the very early stages following app structure setup.

Towards the end of the project I regenerated the SECRET_KEY and did the following;

Add Django secret key to config vars SECRET_KEY

I redeployed to Heroku roughly once a day.

Prior to submitting the finished project I ensured I had DEBUG=False in settings.py

<hr>

## Credits

[StackOverflow](https://stackoverflow.com) for helping debug.
[Net Ninja](https://www.youtube.com/@NetNinja), [Code With Stein](https://www.youtube.com/@CodeWithStein) & [Max Goodridge](https://www.youtube.com/@MaxGoodridgeTech) for their youtube tutorials helping me to better understand Django.

<hr>

## Personal Acnowlegements

- The amazing people that I shared my bootcamp with, who made me smile and laugh when I was stressed out, gave me a helping hand when needed, who reached out when they needed something allowing me to better my understanding by helping others and letting me know that I wasn't alone in this. Your comradery got me through some tough times, I hope I helped you as well. I'm going to miss you all and I hope we stay in touch :)

- I would like to thank our facilitator Iris Smok, and our two coding coaches amd SMEs Martin McInerney and Kevin Loughrey for their patience, encouragement, humour, clear instruction and putting up with my tired brain.

- Lastly but certainly not least, I would like to thank my Code Institute mentor, Ronan McClelland for his insight and encouragement during the final project.

  I couldn't have done it without you all so thank you, from the bottom of my heart

<hr>
