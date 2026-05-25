# displace plus plus
___

## Category
Tools/Warp

## Author
stib

## Version
0.3

___

## Description
<H1>Displace Plus Plus</H1>
<H2>A better displacement map tool</h2>
<p>This tool uses the foreground image to drive displacement of the backgound input. It is GPU accelerated, so it is very fast<p>
<p>There are five modes:</p>
<ul>
<li>The usual X and Y displacement, where the value of the selected channels of an image (r, g, b, like the default one, but also luminance and alpha) drive the X and Y displacement, with individual controls for strength</li>
<li>Linked XY displacement, which is the same as the first mode, but for convenience the X and Y strength is linked</li>
<li>Angle and radius displacement, where one channel drives the angle each pixel gets displaced, and another drives how far the pixel is displaced. Can create intersting swirling</li>
<li>Rotation mode, where the value of the channel determines how much to rotate the pixel around the pivot point. Good for motion graphics effects, I guess<li>
<li>Image gradient, where only a single channel is used, but instead of the value of the channel, the difference between neighbouring pixels drives the displacemnt. Imagine a graph of the pixel values along a row of pixels; the slope of the graph determines how far to move the pixel. It works like a lens where the brightness of the image determines the thickness of the lens, consequently it's great for making glass-like effects.</li>
</ul>
<p> The <strong>midpoint</strong> control determines the value of the input channel that causes no change. The input channel is normally between 0 and 1, so with the midpoint set to 0.5 pixels on the channel with 0 value will move the pixel in the negative direction, and pixels of value 1 will move it in the positive direction, depending on the mode.<p>
<p>The <strong>overflow</strong> control determines what to do with pixels that are moved outside the canvas. They can be wrapped around, the edges of the canvas can be clamped, or the pixels that come from beyond the canvas can be set to transparent.<p>
<p>The image gradient mode has to take multiple samples to create smooth looking images. The <strong>samples</strong> slider determines the quality of the image. The default 4 is acceptible for previewing, but I suggest for final rendering to yeet it up, to say 64 or more.</p>
<p>More fuses and info at <a href='https://codeberg.org/stib/stibs_fuses'>my codeberg repo</a>, and scripts for that other software that rhymes with smadobee smafter smeffects at <a href='https://pureandapplied.com.au'>my blog</a></p>

___

## Download

Download a zipped atom package for offline installation:
> [com.pureandapplied.stibs_fuses.displaceplusplus.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.pureandapplied.stibs_fuses.displaceplusplus)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.pureandapplied.stibs_fuses.displaceplusplus/Fuses/stibs_fuses/DisplacePlusPlus.fuse?ref_type=heads">Fuses/stibs_fuses/DisplacePlusPlus.fuse</a></li>
</ul>
