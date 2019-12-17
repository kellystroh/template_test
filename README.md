# template_test
This repo exists to troubleshoot a dropdown/navbar menu bug on my website. 
I downloaded the template here: https://colorlib.com/wp/template/juli/ . 

Note: the original files contain several references to a file "skin.css" that doesn't exist 
and/or wasn't provided with the template. I don't know if this is connected to the problem. 

I have made the bare minimum of changes needed to replicate the problem. The changes I made are: 

	1) Move all CSS/JS/image/font files into folder "static"
	2) Move all HTML files into folder "templates"
	3) Edit links in each HTML file to account for the relocation of files into "static" folder
	4) Create app.py for flask app
	5) In 01-hompage.html, lines 69-87: change value of every href to "/post"

**It is difficult to detect the problem without step 5 because the default hrefs ("#") do not 
navigate to new pages. 

With the edited version, you should be able to download the repo, and run the website on
localhost:8080 with the command: python app.py (assuming you have python and flask installed)

