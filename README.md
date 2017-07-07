# scripts

## [autofill](https://github.com/BMariscal/scripts/blob/master/auto_fill.py) :
Script uses Selenium and chromedriver. The script automatically logs you into Reddit. [Good resource to assist in script customization.](http://selenium-python.readthedocs.io/locating-elements.html)


## [catching bart](https://github.com/BMariscal/scripts/tree/master/catchingbart) :

Scripts use the <b>bart api</b>. The bart api uses a standard XML output. <em>I used urllib to access the api data and used the ElementTree library to manipulate XML</em>.

 ##### [First script](https://github.com/BMariscal/scripts/blob/master/catchingbart/catching_bart.py)
    gives you the route schedule times for the route 1 bart (PITT station to MLBR).

 ##### [Second script](https://github.com/BMariscal/scripts/blob/master/catchingbart/cmd_catching_bart.py)
     does the same as the script above but you are able to change the api url from the command line,
     making the script customizable and more flexible.
 
 
 
 ## [profanity filter](https://github.com/BMariscal/scripts/tree/master/profanityFilter) :
 Script filters profanities from text file. 


## [file upload progress tracker](https://github.com/BMariscal/scripts/blob/master/progress-tracker.js) :
Node.js(Readable/writable streams & stream pipe): Copies files. Keeps track of upload progress while uploading source file content to a set destination.

