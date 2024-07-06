# Convert Movies to Image Sequences
___

## Author
Andrew Hazelden

## Version
3.1

## Category
Scripts/Comp

___

## Description
<p>The Convert Movies to Image Sequences script lets you extract image sequences from a folder's worth of movie files.</p>

<h2>Required Tools</h2>

<p>This script uses FFmpeg to automatically extract footage from movie files. Windows and Mac users who install this atom will have a shared linking version of FFmpeg 64-bit installed by Reactor's dependency system to the "Reactor:/Deploy/Bin/ffmpeg/" PathMap folder.</p>

<h3>MacOS Tip</h3>

<p>If you are on MacOS you need to adjust the MacOS permissions for FFmpeg using the following Lua command in the Fusion Console tab:</p>

<pre>
	-- Set the FFmpeg program on MacOS to have executable permissions so the ffmpeg command line tool can be used:
	command = 'chmod -R 755 "' .. comp:MapPath('Reactor:/Deploy/Bin/ffmpeg/bin/') .. '"'
	print("[Permissions Update] " .. command)
	os.execute(command)
</pre>

<h3>Linux Tip</h3>

<p>If you are using Fusion on Linux you need to install FFmpeg manually to use this script. Installation details are in the script header on how to do this. You can check the current installation location of ffmpeg using the terminal command "which ffmpeg".</p>

<h2>Copyright Notice</h2>
<p>This script was originally created as a custom pipeline tool that was included with the KartaVR for Fusion toolset. It is not authorized for public re-distribution outside of WSL Reactor.</p>


___

## Dependencies

> [com.wesuckless.ffmpeg](com.wesuckless.ffmpeg.md)  
> [com.wesuckless.wintee](com.wesuckless.wintee.md)  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.ConvertMoviesToImageSequences/Scripts/Comp/Andrew Hazelden/Convert Movies to Image Sequences.lua?ref_type=heads">Scripts/Comp/Andrew Hazelden/Convert Movies to Image Sequences.lua</a></li>
</ul>
