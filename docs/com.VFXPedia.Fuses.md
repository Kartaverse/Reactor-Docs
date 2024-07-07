# VFXPedia Example Fuses
___

## Category
Tools

## Author
Eyeon

## Version
1.0

___

## Description
<p>The Fuses below come from the VFXpedia website and were written or released by employees of Eyeon Software. As examples, they were written to demonstrate, and not necessarily to provide useful functionality (though some do).


<p>VFXPedia Page - Eyeon:Script/Reference/Applications/Fuse/Example Fuses:<br>
https://www.steakunderwater.com/VFXPedia/96.0.243.189/index8be6.html?title=Eyeon:Script/Reference/Applications/Fuse/Example_Fuses</p>

<h2>Useful Fuses</h2>

<h3>Duplicate.Fuse</h3>
<p>This Fuse appears in the Fuses/eyeon category. Use this for making copies of layers, with offsets, blend, gain and even jitter. If you find yourself going 3D just to take advantage of the Duplicate 3D tool, this one's for you. If you like Trails but want to netrender, or want more control, you'll probably find this handy too. For bonus points, enable the hidden Time Offset control - but read the note first!</p>


<h3>CropRectangle.Fuse</h3>
<p>This Fuse appears in the Tools/Transform category. It is a variation on the crop tool. It initially presents an uncropped version of the image, with an onscreen rectangle control that represents the cropping region. Selecting the "Show Crop" option will output the crop instead, and hides the rectangle control.</p>

<h3>Set_Metadata.Fuse</h3>
<p>This Fuse appears in the Fuses/eyeon category. Use this fuse to add/insert metadata to an image. The first field is used to define the metadata tag, and the second field the value. Example: Set the tag to Timecode and add a timecode modifier to the second field.</p>

<h2>Coding Examples</h2>

<p>The following examples are not necessarily intended to perform a useful function. Artists who wish to create their own Fuses may find them useful as starting points. Tools in this category will appear under the Fuses category in the Tools menu.</p>

<h3>Null.Fuse</h3>
<p>About as simple as it gets. This tool doesn't actually do anything - it just passes the input to the output. An example of the bare minimum required to create a tool.</p>

<h3>BoolTest.Fuse</h3>
<p>An example Fuse which re-implements the min, max, add and subtract functions of the Channel Booleans tool using a multibutton array.</p>

<h3>ClipRange.Fuse</h3>
<p>An example Fuse which will clamps the high and low ranges values of the Red, Green, Blue, and Alpha values of an image using range controls.</p>

<h3>Gain.Fuse</h3>
<p>An example Fuse which implements a simple Gain. Demonstrates the Slider and Combo control types. Also a good example of the various methods of processing pixels in an image.</p>

<h3>SourceTest.Fuse</h3>
<p>A Creator or Source type tool. This creates an image full of random noise. A good example of how to create new images</p>

<h3>ShapeTest.Fuse</h3>
<p>A more detailed example that draws multiple shapes over an image. A good example of drawing, merging and transformation functions.</p>

<h3>ParticleEmitterTest.Fuse</h3>
<p>A nearly complete reimplementation of the pEmitter tool as a Fuse.</p>

<h3>TextCountdown.Fuse</h3>
<p>Example of a Text modifier Fuse, with a simple countdown output. To use, modify any text field with Countdown.</p>

<h3>TilePic.Fuse</h3>
<p>This Fuse demonstrates how to add a tile picture icon to a Fuse tool. Otherwise it is identical to the Null.Fuse above. Full instructions can be found in the REG_Fuse_TilePic Attribute documentation.</p>



<h2>Clones of Native Tools</h2>

<p>These Fuses are clones of tools already found in Fusion. They are handy starting points for extending and modifying the default functionality, or just to see how the tools work.</p>

<h3>FuseScale.Fuse</h3>
<p>A reimplementation of the Scale tool as a Fuse. Good example of the Image:Resize() method.</p>

<h3>FuseBlur.Fuse</h3>
<p>A reimplementation of the Blur tool as a Fuse. Good example of the Image:Blur() method.</p>

<h3>FuseGlow.Fuse</h3>
<p>A reimplementation of the Glow tool as a Fuse. Good example of the Image:Blur() method.</p>

<h3>FuseMerge.Fuse</h3>
<p>A reimplementation of the Merge tool as a Fuse. Good example of the Image:Merge() method.</p>

<h3>FuseTransform.Fuse</h3>
<p>A reimplementation of the Transform tool as a Fuse. Good example of the Image:Transform() method.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.VFXPedia.Fuses.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.VFXPedia.Fuses)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Blur/FuseBlur.Fuse?ref_type=heads">Fuses/VFXPedia/Blur/FuseBlur.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Blur/FuseGlow.Fuse?ref_type=heads">Fuses/VFXPedia/Blur/FuseGlow.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Color/BoolTest.Fuse?ref_type=heads">Fuses/VFXPedia/Color/BoolTest.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Color/ClipRange.Fuse?ref_type=heads">Fuses/VFXPedia/Color/ClipRange.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Color/Gain.Fuse?ref_type=heads">Fuses/VFXPedia/Color/Gain.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Composite/FuseMerge.Fuse?ref_type=heads">Fuses/VFXPedia/Composite/FuseMerge.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Creator/SourceTest.Fuse?ref_type=heads">Fuses/VFXPedia/Creator/SourceTest.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Mask/ShapeTest.Fuse?ref_type=heads">Fuses/VFXPedia/Mask/ShapeTest.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Metadata/Set_Metadata.Fuse?ref_type=heads">Fuses/VFXPedia/Metadata/Set_Metadata.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Miscellaneous/Duplicate.Fuse?ref_type=heads">Fuses/VFXPedia/Miscellaneous/Duplicate.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Miscellaneous/TilePic.Fuse?ref_type=heads">Fuses/VFXPedia/Miscellaneous/TilePic.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Modifiers/TextCountdown.Fuse?ref_type=heads">Fuses/VFXPedia/Modifiers/TextCountdown.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Particles/ParticleEmitterTest.Fuse?ref_type=heads">Fuses/VFXPedia/Particles/ParticleEmitterTest.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Transform/CropRectangle.Fuse?ref_type=heads">Fuses/VFXPedia/Transform/CropRectangle.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Transform/FuseScale.Fuse?ref_type=heads">Fuses/VFXPedia/Transform/FuseScale.Fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Transform/FuseTransform.fuse?ref_type=heads">Fuses/VFXPedia/Transform/FuseTransform.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.Fuses/Fuses/VFXPedia/Transform/Null.Fuse?ref_type=heads">Fuses/VFXPedia/Transform/Null.Fuse</a></li>
</ul>
