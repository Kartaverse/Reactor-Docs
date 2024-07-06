# Shell Slash Command
___

## Author
Fusion Reactor

## Version
1.0

## Category
Console

___

## Description
<p>A console slash command to execute shell/terminal commands.</p>

<h2>Usage</h2>

<p>Step 1. Switch to the Fusion Console tab.<br>

Step 2. To run a terminal command type in:</p>
<pre>/shell &lt;command&gt; &lt;options&gt;</pre>

<p>Print the current directory (Mac/Linux):</p>
<pre>/shell pwd</pre>

<p>List the directory contents (Mac/Linux):</p>
<pre>/shell ls ~/Documents/</pre>

<p>List the directory contents (Windows):</p>
<pre>/shell dir %USERPROFILE%\Documents\</pre>

<p>Print the current environment variables (Windows):</p>
<pre>/shell set</pre>

<p>Print the current environment variables (Mac/Linux):</p>
<pre>/shell env</pre>

<p>Open the current folder in a new Explorer folder browsing window (Windows):</p>
<pre>/shell explorer .\</pre>

<p>Open the current folder in a new Finder folder browsing window (Mac):</p>
<pre>/shell open ./</pre>

<p>Open the current folder in a new Nautilus folder browsing window (Linux):</p>
<pre>/shell nautilus ./</pre>

<p>Run wget to download a file (Mac/Linux):</p>
<pre>/shell wget 'https://www.steakunderwater.com/wesuckless/images/smilies/icon_e_smile.gif'</pre>

___

## Dependencies

> [com.wesuckless.SlashCommand](com.wesuckless.SlashCommand.md)  
## Deploy

### Common (No Architecture)

> Scripts/SlashCommand/shell.lua  
