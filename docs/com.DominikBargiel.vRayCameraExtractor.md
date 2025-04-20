# vRayCameraExtractor
___

## Category
Tools/3D

## Author
Dominik Bargiel

## Version
1.0

___

## Description
Creating a Fusion camera from render image metadata is efficient and relatively error-proof. The vRayCameraExtractor Fuse extracts the transformation matrix values from the metadata's comma-separated list, if necessary, applies the transformations using the correct ZXY rotation order, and provides the Rotations and Translations in a more easily-accessed table format.
A Canera3D Default setting file has been added, which has been configured with expressions to read the metadata loaded in the S6 settings. All you need to do is switch the camera to S6 and connect the RS Camera Extractor into the Image Input.

Macros/vRay/vRayCameraExtractor_Camera.setting was added that reads the values from the node.

___

## Donation
The author of the atom has suggested a donation of "0".  
You can donate using the URL: <a href=""></a>

## Download

Download a zipped atom package for offline installation:
> [com.DominikBargiel.vRayCameraExtractor.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.DominikBargiel.vRayCameraExtractor)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.vRayCameraExtractor/Fuses/Metadata/vRayCameraExtractor.fuse?ref_type=heads">Fuses/Metadata/vRayCameraExtractor.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.vRayCameraExtractor/Macros/vRay/vRayCameraExtractor_Camera.setting?ref_type=heads">Macros/vRay/vRayCameraExtractor_Camera.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.vRayCameraExtractor/Modules/Lua/matrix.lua?ref_type=heads">Modules/Lua/matrix.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.vRayCameraExtractor/Modules/Lua/matrixutils.lua?ref_type=heads">Modules/Lua/matrixutils.lua</a></li>
</ul>
