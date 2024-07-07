# KartaVP Tools | kvrCropStereo
___

## Category
Kartaverse/KartaVP/Tools

## Author
Andrew Hazelden

## Version
5.73

___

## Description
<p>The Kartaverse "kvrCropStereo" DCTL fuse allows you to crop stereo 3D imagery with individual control over the left and right eye views. You can also do per-eye rotation corrections to adjust for camera body positioning on a tripod with presets for 0&deg;, 90&deg;, 180&deg;, and 270&deg; image orientations.</p>
	
<p>This node makes quick work of 180VR to 360VR frame size conversions by padding out the empty area. You can also go from 360VR (360&deg;x180&deg;) to cropped down 180VR (180&deg;x180&deg;) output as well.</p>

<h2>DCTL Fuse Support Requirements</h2>

<ul>
	<li>An OpenCL, CUDA, or Metal based GPU</li>
	<li>Fusion Studio 16-19+ or Resolve 16-19+</li>
</ul>

<h2>Open Source Software License</h2>
<p>LGPL 3.0 License</p>



___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaVP.Tools.kvrCropStereo.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaVP.Tools.kvrCropStereo)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrCropStereo/Comps/Kartaverse/KartaVP/kvrCropStereo/Dual Fisheye STMap Creation v001.comp?ref_type=heads">Comps/Kartaverse/KartaVP/kvrCropStereo/Dual Fisheye STMap Creation v001.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrCropStereo/Comps/Kartaverse/KartaVP/kvrCropStereo/kvrCropStereo v001.comp?ref_type=heads">Comps/Kartaverse/KartaVP/kvrCropStereo/kvrCropStereo v001.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrCropStereo/Fuses/Kartaverse/KartaVP/Warp/kvrCropStereo.fuse?ref_type=heads">Fuses/Kartaverse/KartaVP/Warp/kvrCropStereo.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrCropStereo/Macros/KartaVR/Images/Canon R5C Body With Canon RF5.2mm Dual Fisheye Lens.jpg?ref_type=heads">Macros/KartaVR/Images/Canon R5C Body With Canon RF5.2mm Dual Fisheye Lens.jpg</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrCropStereo/Macros/KartaVR/Images/RED Digital V-Raptor 8K With Canon RF5.2mm Dual Fisheye Lens.jpg?ref_type=heads">Macros/KartaVR/Images/RED Digital V-Raptor 8K With Canon RF5.2mm Dual Fisheye Lens.jpg</a></li>
</ul>
