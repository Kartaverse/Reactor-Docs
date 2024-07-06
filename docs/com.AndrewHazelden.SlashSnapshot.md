# Snapshot Slash Command
___

## Author
Andrew Hazelden

## Version
2.0

## Category
Console

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

> com.wesuckless.SlashCommand  
## Deploy

### Common (No Architecture)

> Scripts/SlashCommand/snapshot.lua  
