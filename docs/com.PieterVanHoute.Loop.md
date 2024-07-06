# Loop
___

## Author
Pieter Van Houte

## Version
1.02

## Category
Tools/Flow

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

## Dependencies

## Deploy

### Common (No Architecture)

> Comps/Loop/Reaction_Diffusion.comp  
> Comps/Loop/Trails.comp  
> Macros/Loop/LoopEnd.setting  
> Macros/Loop/LoopStart.setting  
> Modules/Lua/SuckLessDialogs.lua  
> Scripts/Support/Loop/AbortLoop.lua  
> Scripts/Support/Loop/OpenCacheFolder.lua  
> Scripts/Support/Loop/RunLoop.lua  
