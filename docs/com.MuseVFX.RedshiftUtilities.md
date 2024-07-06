# Redshift Utilities
___

## Category
Tools

## Author
Bryan Ray

## Version
3.0

___

## Description
<p>A collection of tools to make working with Redshift renders easier. This package contains:</p>


<ul>
	<li>Redshift Camera Extractor. Makes it easy to control a Camera3D using image metadata from a Redshift render.</li>
	<li>A Camera3D Default file for use with the Camera Extractor. </li>
	<li>Redshift Photographic Exposure. Match the appearance of the Redshift post-processing in comp.</li>
	<li>Redshift Vector Flipper. Conform normals and position AOVs to Fusion's preferred format.</li>
</ul>

<h3>Usage</h3>
<p><strong>Camera Extractor:</strong> Plug any Redshift AOV Loader into the input of the RS Camera Extractor node. Select the DCC that rendered the image with the Mode switch. Create a Camera3D node and switch to the S6 preset. Connect the main output of RS Camera Extractor to the ImageInput of the Camera3D node. The camera will automatically inherit the transforms from the render's metadata.</p>
<p><strong>Photographic Exposure:</strong> Place the node after your pre-composited CG. If the Photographic Exposure settings were adjusted prior to rendering, The Use Metadata switch will often automatically configure the node to match those settings. Otherwise, adjust the parameters to taste—documentation is available in the tool's comments.</p>
<p><strong>Vector Flipper:</strong> Connect any 3d vector AOV (normals, world position) to the Vector Flipper and choose the DCC that rendered the image with the Mode switch. If you need to flip the RGB channels, tick the 'Affect RGB' checkbox.

___

## Donation
The author of the atom has suggested a donation of "$5 USD".  
You can donate using the URL: <a href="https://www.paypal.me/BryanRayVFX" class="button">https://www.paypal.me/BryanRayVFX</a>
## Dependencies

> [com.MuseVFX.RSCameraExtractor](com.MuseVFX.RSCameraExtractor.md ':class=button')  
> [com.MuseVFX.RsPhotographicExposure](com.MuseVFX.RsPhotographicExposure.md ':class=button')  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.RedshiftUtilities/Macros/Redshift/RsVectorFlipper.setting?ref_type=heads">Macros/Redshift/RsVectorFlipper.setting</a></li>
</ul>
