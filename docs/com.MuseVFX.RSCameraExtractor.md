# Redshift Camera Extractor
___

## Category
Tools/Metadata

## Author
Bryan Ray/MuseVFX

## Version
3.2

___

## Description
<p>Creating a Fusion camera from render image metadata is efficient and relatively error-proof. The RSCameraExtractor Fuse extracts the transformation matrix values from the metadata's comma-separated list, if necessary, applies the transformations using the correct ZXY rotation order, and provides the Rotations and Translations in a more easily-accessed table format.</p>
<p>A Canera3D Default setting file has been added, which has been configured with expressions to read the metadata loaded in the S6 settings. All you need to do is switch the camera to S6 and connect the RS Camera Extractor into the Image Input.

<hr>

<p>Version 3.2: Fixed Atom dependency error.
<p>Version 3.1: Added Matrix lua libraries.
<p>Version 3: Added 3DS Max support. Added a Camera3D Default setting file. Added a text-only second output for Vonk FusionMatrix support.
<p>Version 2: At some point prior to version 2.6.15, Redshift's metadata format changed. The Fuse has been updated to detect and account for the change.</p>


___

## Download

Download a zipped atom package for offline installation:
> [com.MuseVFX.RSCameraExtractor.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.MuseVFX.RSCameraExtractor)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.RSCameraExtractor/Defaults/Camera3D_Camera 3D.setting?ref_type=heads">Defaults/Camera3D_Camera 3D.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.RSCameraExtractor/Fuses/Metadata/RSCameraExtractor.fuse?ref_type=heads">Fuses/Metadata/RSCameraExtractor.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.RSCameraExtractor/Modules/Lua/matrix.lua?ref_type=heads">Modules/Lua/matrix.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.RSCameraExtractor/Modules/Lua/matrixutils.lua?ref_type=heads">Modules/Lua/matrixutils.lua</a></li>
</ul>
