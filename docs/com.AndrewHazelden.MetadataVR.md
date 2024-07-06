# KartaVR Tools | MetadataVR
___

## Author
 : Andrew Hazelden

## Version
 : v5.1

## Category
 : Kartaverse/KartaVR/Tools/Metadata
___

## Description
<p>The MetadataVR fuse provides a quick set of controls to adjust the metadata tags on your 360VR and Stereo 3D imagery. This metadata information lets Fusion's viewer windows switch to the correct Stereo 3D, and 360VR image projection display modes automatically which can save you time if you are working in a large composite and are constantly remapping your imagery between several different image projections in your flow.</p>

<p>The MetadataVR fuse works by assigning the Fusion centric "<strong><i>Stereo.Method</i></strong>" and the "<strong><i>Pano.Format</i></strong>" metadata tags.</p>

<p>Fusion 9.0.2 or Resolve 15 B4+ is required.</p>

<p>Note: This fuse does not add YouTube 360/Facebook 360 spatial media metadata tags to the video output. A separate Python based Comp script tool would be need to be created in the future to carry out that task since a Fusion Saver/MediaOut node does not support passing that specific kind of information directly into the rendered MP4/MOV file at this time.</p>


<h1>Node Inputs</h1>

<p>Image</p>


<h1>GUI Controls</h1>


<h2>Stereo Format (ComboControl)</h2>

<ul>
	<li>Mono 2D</li>
	<li>Stereo 3D Over Under</li>
	<li>Stereo 3D Side By Side</li>
</ul>


<h2>Image Projection (ComboControl)</h2>

<ul>
	<li>None</li>
	<li>LatLong</li>
	<li>Vertical Cross</li>
	<li>Horizontal Cross</li>
	<li>Vertical Strip</li>
	<li>Horizontal Strip</li>
</ul>


<h2>Verbose (Checkbox)</h2>

<p>Prints the raw metadata info to the Fusion Console.</p>___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Fuses/Metadata/MetadataVR.fuse  
