# Snapshot Slash Command
___

## Category
Console

## Author
Andrew Hazelden

## Version
2.0

___

## Description
<p>Snapshot is a console slash command that saves out snapshot images from Fusion's left image viewer window.</p>

<h2>Usage</h2>

<p>Step 1. Select a node and view its output in Fusion's left viewer window.<br>
Step 2. Switch to the Fusion Console tab.<br>
Step 3. To quickly save a viewer snapshot image to disk (using the default image format) type in:</p>

<pre>/snapshot</pre>

<p>Alternatively, to save an image to disk of a specific image format add the file type extension to the command:</p>

<pre>/snapshot jpg
/snapshot bmp
/snapshot exr
/snapshot png
/snapshot tga
/snapshot tif</pre>

<h2>Notes</h2>

<p>You can change the default image format written to disk by the "/snapshot" command by uncommenting a specific "snapshotImageFormat" image format line at the top of the script.</p>

___

## Dependencies

> [com.wesuckless.SlashCommand](com.wesuckless.SlashCommand.md ':class=button')  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.SlashSnapshot/Scripts/SlashCommand/snapshot.lua?ref_type=heads">Scripts/SlashCommand/snapshot.lua</a></li>
</ul>
