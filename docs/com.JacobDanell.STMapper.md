# STMapper
___

## Author
Jacob Danell

## Version
1.2

## Category
Tools/Warp

___

## Description
<center><h2>STMapper</h2></center>
<p>A DCTL/GPU powered Fuse for all your STmap needs.</p>

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
	<li>Set the amount of distortion you want</li>
	<li>Works with DoD in the texture and STMap</li>
	<li>Get the size from the Texture or the STmap</li>
	<li>Different tiling options</li>
</ul>
</p>

<p>Todo:
<ul>
	<li>Not working with RoI.</li>
</ul>
</p>


<p>For more info, please check:</p>

<br>WSL thread: <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=4429">https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=4429</a></br>


<p>
Changelog:<br/>
v1.2: 2023-11-01:<br/>
- Select the image size, window size and clipping to get the exact image you need<br/>
- STMapper can now read the DoD from the stmap and write out data in the outputs DoD correctly<br/>
- STMapper now a- dds center-offset metadata to automatically be able to apply the correct center-offset when re-distorting the image<br/>
- Grouped the parameters for a cleaner UI<br/>
- Changed default tiling mode to Transparent<br/>
- Distortion amount now respects the UV channel selection<br/>
- Removed cap for Distortion slider. It's not magical and can't reverse your stmap if set to -1 but you can get some fun results.<br/>
- Added author text<br/>
- Code Cleanup<br/>
<br/>

v1.1: 2022-12-10:<br />
- Now even faster and better quality when viewing with HQ off!<br />
- Rewrote the whole stmap engine to now support native tiling sampler<br />
- Fixed PreCalculation so correct image size information goes to output nodes<br />
- You can now select where to get your metadata from<br />
- The depth is now picked from the texture instead of the STmap<br />
- Now works with DoD bigger than the image/stmap<br />
- Remove premulti for STmap and postmulti for RGB<br />
- Removed Image Frame with DoD crop from Crop selection (I don't remember the use-case really...)<br />
- You can now select the amount of undistortion you want<br />
<br />

v1.0.3, 2022-03-17:<br />
- Now works with OpenCL.<br />
<br />

v1.0.2, 2022-02-25:<br />
- Added Repeat Pivot that lets you select where the pivot point of the repeat is located<br />
- Cleaned up the UX by replacing "Calculate STmap from pixel center" with "Match Render" where you can select between the 3 different types of STMaps.
<ul>
	<li>Ignore = First pixel is 0, last pixel is 1.</li>
	<li>Image = This is what Custom Node-generated STmaps looks like and what the Texture node expects.</li>
	<li>Mesh = This is what Nuke-generated STmaps looks like.</li>
</ul>
- Removed Crop to DoD that you could set when using Tile or Mirror (honestly I don't remember what it was there for...)<br />
- Rewrote the Tile and Mirror tiling so it no longer gives weird artifacts when the input images DoD is smaller than the image size.<br />

<br />
v1.0.1, 2022-02-03:<br />
- STMapper now expects the first pixel to be 0 and the pixel next to the last pixel to be 1. This is how Fusions Texture node works.<br />
- Added "Calculate STmap from pixel center" to read STmaps like Nuke does.<br />
<br />
v1.0, 2020-10-12:<br />
- First release!<br />
</p>

___

## Dependencies

## Deploy

### Common (No Architecture)

> Fuses/Warp/STMapper.fuse  
