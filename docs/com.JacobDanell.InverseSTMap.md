# Inverse STMap
___

## Category
Tools/Warp

## Author
Jacob Danell

## Version
0.7

___

## Description
<center><h2>Inverse STMap</h2></center>
<p>A DCTL/GPU powered Fuse for all your inverse STmap needs.</p>

<p>Features:
<ul>
<li>DCTL, meaning it's very fast!</li>
<li>Works with Alpha</li>
<li>Supports different types of STmaps:</li>
<ul>
<li>Ignore (0 to Width) = First pixel is 0, last pixel is 1</li>
<li>Image (0 to Width-1) = This is what Custom Node-generated STmaps looks like and what the Texture node expects</li>
<li>Mesh (0.5 to Width-0.5) = This is what Nuke-generated STmaps looks like</li>
</ul>
<li>Different anti-aliasing and super sampling options</li>
</ul>
</p>

<p>For more info, please check:</p>

<br>WSL thread: <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?p=46265">https://www.steakunderwater.com/wesuckless/viewtopic.php?p=46265</a></br>

<p>
Changelog:<br />
v0.7, 2024-01-30:<br />
* Added multi-thread processing. It might sometimes be faster, other times slower.<br />
* Fixed alpha-problem when using Linear filtering<br />
<br />
v0.6, 2023-12-23:<br />
* Fill holes will now fill the whole image<br />
<br />
v0.5, 2023-05-05:<br />
* Now works with Alpha!<br />
* Fuse no longer crash if STmap doesn't fit the selected STMap Type (eg STmap type Image when STmap is of type Ignore).<br /><br />
<br />
v0.4, 2023-02-04:<br />
* Added a slider for the GPU process to scan only x pixels from the current pixel to try and speed the process up. The result was sadly not what i was after.<br />
<br />
v0.3, 2023-01-09:<br />
* Tried to make a DCTL version of the sampeling. Only works on very low res images. Slower than the CPU version sadly<br />
<br />
v0.2, 2023-01-03:<br />
* Added 3 different filters for better control<br />
* Added input for texture to automatically deform it to the wanted result. Gives better result in Linear filtering<br />
<br />
v0.1, 2022-12-29:<br />
* Init release<br />
</p>

___

## Donation
The author of the atom has suggested a donation of "5".  
You can donate using the URL: <a href="https://paypal.me/danell">https://paypal.me/danell</a>

## Download

Download a zipped atom package for offline installation:
> [com.JacobDanell.InverseSTMap.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.JacobDanell.InverseSTMap)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.InverseSTMap/Comps/Warp/Inverse STmap.comp?ref_type=heads">Comps/Warp/Inverse STmap.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.InverseSTMap/Fuses/Warp/InverseSTmap.Fuse?ref_type=heads">Fuses/Warp/InverseSTmap.Fuse</a></li>
</ul>
