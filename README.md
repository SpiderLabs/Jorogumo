# Jorōgumo [ 絡新婦 ]
A red team tool written in python for building SVG stored xss payloads, cloning webpages, or implementing custom javascript in pre-existing or cloned webpages.

## Features
![da12503cb7e54226a8e9f8164a6c0694](https://user-images.githubusercontent.com/39013067/228970400-306a5a8f-bcb8-45e1-9227-943e643136db.png)
### Clone a webpage: 

Creates a local copy of the target webpage, which can be used for further customization or attack purposes.
### Create a standalone SVG payload: 

Generates a payload in SVG format, embedding a specified image URL and redirecting users to a specified URL upon interaction.
### Stored Cross-Site Scripting SVG Credential Stealer: 

Clones a login page and injects a script that captures user credentials, and then generates an SVG to be chained with a stored cross-site scripting vulnerability. When the stored cross-site scripting svg payload is triggered, it renders a 404 picture by default, or the custom picture entered by the user, and when clicked, redirects the user to the attacker's malicious login page, where the credential stealer will post credentials to a web request catcher or listener.
### Build a webpage with existing JavaScript and HTML: 

Takes an existing HTML file and adds specified JavaScript code, either from a local file or a remote URL.
### Build a webpage with existing JavaScript but no HTML: 

Clones a webpage and adds specified JavaScript code, either from a local file or a remote URL, into the cloned webpage.
### Custom JavaScript Stored Cross-Site Scripting SVG Payload: 

Clones a webpage and adds specified JavaScript code, either from a local file or a remote URL, into the cloned webpage. Generates an SVG to be chained with a stored cross-site scripting vulnerability. When the stored cross-site scripting svg payload is triggered, it renders a 404 picture by default, or the custom picture entered by the user, and when clicked, redirects the user to the attacker's malicious page, where the custom javascript code will be executed.
