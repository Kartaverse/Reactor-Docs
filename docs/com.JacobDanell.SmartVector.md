# Smart Vector
___

## Category
Tools/Warp

## Author
Jacob Danell

## Version
0.31

___

## Description
<center><h1>Smart Vector</h1></center>

<p>A smart vector fuse for Fusion! It's basically the same as <A HREF="https://www.steakunderwater.com/wesuckless/viewtopic.php?p=39982#p39982">Millolab 's Vector Warp macro</a> but with additional features.</p>

<h2>For More info</h2>
Check out the development thread on WSL for more details about the fuse:<br>
<a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?p=46092#p46092">https://www.steakunderwater.com/wesuckless/viewtopic.php?p=46092#p46092</a>

<h2>YouTube Video Tutorial</h2>
Check out the "Fusion Vector Warp beta tutorial" video:<br>
<a href="https://www.youtube.com/watch?v=lh7APGa7Mvk">https://www.youtube.com/watch?v=lh7APGa7Mvk</a>

<h2>Usage Notes</h2>
<p>The fuse itself doesn't create any vectors. If you don't have any, use the Optical Flow node before this fuse. This fuse accumulates the vectors frame by frame. If you jump between non-consecutive frames the result will be scrambled. Use the buttons to process the image correctly.</p>

<p>The "CopyAux" channel will look up your node-tree for a CopyAux node and will automatically change its aux channel to Vector/Back Vector as needed. If the wrong CopyAux node gets selected for some reason, drag the correct one into the Aux Node box in the UI.</p>

<p>If using the RGB channel as vectors, make sure it uses Forward Vector for frames earlier than the source frame and Back Vector for frame after the source frame.</p>

<p>The preview uses your ram to cache the result. If you don't have enough ram preview won't work correctly. In that case, render out the result directly insted. The fuse will render out exr files in 32bit with zip compression.</p>


___

## Donation
The author of the atom has suggested a donation of "".  
You can donate using the URL: <a href="https://paypal.me/danell">https://paypal.me/danell</a>

## Download

Download a zipped atom package for offline installation:
> [com.JacobDanell.SmartVector.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.JacobDanell.SmartVector)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.SmartVector/Fuses/Warp/Smart Vector.Fuse?ref_type=heads">Fuses/Warp/Smart Vector.Fuse</a></li>
</ul>
