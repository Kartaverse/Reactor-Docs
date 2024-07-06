# Class Browser
___

## Author
 : Roger Magnusson

## Version
 : v1.3

## Category
 : Scripts/Comp
___

## Description
<p>The Class Browser script allows you to browse all Fusion (and Resolve) classes it can find, including all properties and methods. It does this by looking at three things:</p>
<ul>
	<li>Fusion's built-in script documentation, GetHelp()</li>
	<li>The global _G table</li>
	<li>The binary files (yes, it's a simple and probably unreliable hack)</li>
	<li>As of v1.3 you can manually add documentation</li>
</ul>

<p>The binary files method came about when I started making a Fuse and soon became frustrated that there were some crucial pieces missing from VFXPedia. Without access to the official documentation it's really tricky. But I could see there was more stuff in the binaries just by looking at them.</p>

<p>Since classes found in the binaries don't come with a class hierarchy, not all classes will be placed correctly. In case I can't match a discovered class with a documented class I simply place it in the root.</p>

<p>To make a distinction between documented information and information discovered in the binary files I call the different sections "Properties", "Methods", "Discovered Properties" and "Discovered Methods".</p>
___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Scripts/Comp/Roger Magnusson/Class Browser.lua  
