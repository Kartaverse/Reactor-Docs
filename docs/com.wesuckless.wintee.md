# Wintee
___

## Author
We Suck Less

## Version
1.01

## Category
Bin

___

## Description
<p>Wintee provides a Windows native version of the GNU Linux "tee" terminal utility that is used for shell output redirection.</p>

<p>Wintee will take any input from standard input and copy the data to standard out and any files specified on the command line. The most common way for people to use wintee is to pipe the output of a command into wintee using the "|" operator on the command line.</p>

<h2>Usage Example:</h2>

<pre>echo Hello world | wintee output1.txt output2.txt</pre>

<h2>Parameters:</h2>

<p>wintee allows you to use the following command parameters:</p>

<pre>Parameter  Purpose
a  append to the given file(s), do not overwrite
i  ignore interrupt signals
?  display the help screen and exit
--version  output version information and exit
--help  display the help screen and exit</pre>

<h2>Open Source License:</h2>
<p>Mozilla Public License<br>
Wintee was created by Ryan Buhl.<br>
The Wintee atom was packaged by Andrew Hazelden.</p>

<h2>For More Information:</h2>
<p>https://code.google.com/archive/p/wintee/</p>


___

## Dependencies

## Deploy

### Common (No Architecture)

> Bin/wintee/source/LICENSE.txt  
> Bin/wintee/source/queue.h  
> Bin/wintee/source/wintee.c  
> Bin/wintee/source/wtee.ide  

### Linux

> Bin/wintee/docs/LICENSE.txt  
> Bin/wintee/docs/readme.txt  

### macOS

> Bin/wintee/docs/LICENSE.txt  
> Bin/wintee/docs/readme.txt  

### Windows

> Bin/wintee/bin/wtee.exe  
> Bin/wintee/docs/LICENSE.txt  
> Bin/wintee/docs/readme.txt  
