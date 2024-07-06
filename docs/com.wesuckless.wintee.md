# Wintee
___

## Category
Bin

## Author
We Suck Less

## Version
1.01

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

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Bin/wintee/source/LICENSE.txt?ref_type=heads">Bin/wintee/source/LICENSE.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Bin/wintee/source/queue.h?ref_type=heads">Bin/wintee/source/queue.h</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Bin/wintee/source/wintee.c?ref_type=heads">Bin/wintee/source/wintee.c</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Bin/wintee/source/wtee.ide?ref_type=heads">Bin/wintee/source/wtee.ide</a></li>
</ul>

### Linux

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Linux/Bin/wintee/docs/LICENSE.txt?ref_type=heads">Bin/wintee/docs/LICENSE.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Linux/Bin/wintee/docs/readme.txt?ref_type=heads">Bin/wintee/docs/readme.txt</a></li>

### macOS

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Mac/Bin/wintee/docs/LICENSE.txt?ref_type=heads">Bin/wintee/docs/LICENSE.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Mac/Bin/wintee/docs/readme.txt?ref_type=heads">Bin/wintee/docs/readme.txt</a></li>

### Windows

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Windows/Bin/wintee/bin/wtee.exe?ref_type=heads">Bin/wintee/bin/wtee.exe</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Windows/Bin/wintee/docs/LICENSE.txt?ref_type=heads">Bin/wintee/docs/LICENSE.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.wintee/Windows/Bin/wintee/docs/readme.txt?ref_type=heads">Bin/wintee/docs/readme.txt</a></li>
