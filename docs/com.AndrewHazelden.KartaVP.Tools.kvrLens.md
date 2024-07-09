# KartaVP Tools | kvrLens
___

## Category
Kartaverse/KartaVP/Tools

## Author
Andrew Hazelden

## Version
5.7301

___

## Description
<p>The Kartaverse "kvrLens" and "kvrLensStereo" DCTL fuses allows you to distort your imagery using either the "Brown-Conrady", "Panotools", or "SynthEyes" lens distortion models. The "kvrSTMapGenerator" DCTL fuse allows you to generate an initial STMap template gradient.</p>

<p>Brown-Conrady is a popular lens model to use with computer vision tools like OpenCV, and photogrammetry/NeRF tools. Panotools is a lens model used with 360VR panoramic imagery. The SynthEyes lens model is used for camera tracking/match moving.</p>

<p>Bonus DCTLs: Resolve Edit and Color page compatible DCTL files are included in the folder:<br>
Reactor:/Deploy/Bin/Kartaverse/LUT/</p>

<h2>DCTL Fuse Support Requirements</h2>

<ul>
<li>An OpenCL, CUDA, or Metal based GPU</li>
<li>Fusion Studio 16-19+ or Resolve 16-19+</li>
</ul>

<h2>Open Source Software License</h2>
<p>GPL v3 License</p>


___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaVP.Tools.kvrLens.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaVP.Tools.kvrLens)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrLens/Bin/Kartaverse/LUT/kvrBrownConrady.dctl?ref_type=heads">Bin/Kartaverse/LUT/kvrBrownConrady.dctl</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrLens/Bin/Kartaverse/LUT/kvrPanotools.dctl?ref_type=heads">Bin/Kartaverse/LUT/kvrPanotools.dctl</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrLens/Bin/Kartaverse/LUT/kvrSTMapGenerator.dctl?ref_type=heads">Bin/Kartaverse/LUT/kvrSTMapGenerator.dctl</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrLens/Comps/Kartaverse/KartaVP/kvrLens/kvrLens Distortion Comparison.comp?ref_type=heads">Comps/Kartaverse/KartaVP/kvrLens/kvrLens Distortion Comparison.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrLens/Fuses/Kartaverse/KartaVP/Warp/kvrLens.fuse?ref_type=heads">Fuses/Kartaverse/KartaVP/Warp/kvrLens.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrLens/Fuses/Kartaverse/KartaVP/Warp/kvrLensStereo.fuse?ref_type=heads">Fuses/Kartaverse/KartaVP/Warp/kvrLensStereo.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVP.Tools.kvrLens/Fuses/Kartaverse/KartaVP/Warp/kvrSTMapGenerator.fuse?ref_type=heads">Fuses/Kartaverse/KartaVP/Warp/kvrSTMapGenerator.fuse</a></li>
</ul>
