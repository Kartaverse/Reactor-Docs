# Loop
___

## Category
Tools/Flow

## Author
Pieter Van Houte

## Version
1.02

___

## Description
<h1 align="center"><span style="color:#ff5900">L</span><span style="color:#ffb300">o</span><span style="color:#f0ff00">o</span><span style="color:#96ff00">p</span><span style="color:#3cff00"> </span><span style="color:#00ff1e"><su<span style="color:#00ffd1">F</span><span style="color:#00d1ff">o</span><span style="color:#0077ff">r</span> <span style="color:#3c00ff">F</span><span style="color:#9600ff">u</span><span style="color:#f000ff">s</span><span style="color:#ff00b3">i</span><span style="color:#ff0059">o</span><span style="color:#ff0000">n</span></h1>
	
<h3><p>Loop is a new and free toolset for Blackmagic Design Fusion that allows you to create interesting, wonderful and delightfully unpredictable visuals.</p></h3>
<p>It enables you to create "iterative loops" by continuously rendering over itself. You do this by building an effect between a startpoint and an endpoint in your comp. Loop will render out this effect as an image and use that same image as the input for the next render. You can render image sequences and also have multiple iterations per single frame.</p>

<p>Loop consists of two tools:
<ul>
	<li>LoopStart</li>
	<li>LoopEnd</li>
</ul>
which will be installed in the Tools menu under Macros/Sprut. All the clever stuff is handled with a set of scripts controlled by the LoopEnd node.</p>
<p>Also included is a comp file demonstrating "Reaction Diffusion", which is the process used to create the mesmerizing Loop trailer on Youtube: <a href="https://youtu.be/ze8PEc7ZmAI">https://youtu.be/ze8PEc7ZmAI</a></p>
<p>After installation you can find the comp file here:<br>
<a href="file://Reactor:/Deploy/Comps/Loop/">Reactor:/Deploy/Comps/Loop/</a></p>

<p>For more information on Loop, come discuss it on We Suck Less!<br>
<a href="https://www.steakunderwater.com/wesuckless/">https://www.steakunderwater.com/wesuckless/</a></p>

___

## Donation
The author of the atom has suggested a donation of "".  
You can donate using the URL: <a href="https://www.patreon.com/wesuckless">https://www.patreon.com/wesuckless</a>
## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Loop/Comps/Loop/Reaction_Diffusion.comp?ref_type=heads">Comps/Loop/Reaction_Diffusion.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Loop/Comps/Loop/Trails.comp?ref_type=heads">Comps/Loop/Trails.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Loop/Macros/Loop/LoopEnd.setting?ref_type=heads">Macros/Loop/LoopEnd.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Loop/Macros/Loop/LoopStart.setting?ref_type=heads">Macros/Loop/LoopStart.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Loop/Modules/Lua/SuckLessDialogs.lua?ref_type=heads">Modules/Lua/SuckLessDialogs.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Loop/Scripts/Support/Loop/AbortLoop.lua?ref_type=heads">Scripts/Support/Loop/AbortLoop.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Loop/Scripts/Support/Loop/OpenCacheFolder.lua?ref_type=heads">Scripts/Support/Loop/OpenCacheFolder.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Loop/Scripts/Support/Loop/RunLoop.lua?ref_type=heads">Scripts/Support/Loop/RunLoop.lua</a></li>
</ul>
