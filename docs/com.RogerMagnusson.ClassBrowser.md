# Class Browser
___

## Category
Scripts/Comp

## Author
Roger Magnusson

## Version
1.3

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

## Donation
The author of the atom has suggested a donation of "".  
You can donate using the URL: <a href="https://www.paypal.me/rogermagnusson" class="button">https://www.paypal.me/rogermagnusson</a>
## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.RogerMagnusson.ClassBrowser/Scripts/Comp/Roger Magnusson/Class Browser.lua?ref_type=heads">Scripts/Comp/Roger Magnusson/Class Browser.lua</a></li>
</ul>
