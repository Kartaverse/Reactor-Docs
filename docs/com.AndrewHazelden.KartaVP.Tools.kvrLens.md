# KartaVP Tools | kvrLens
___

## Author
Andrew Hazelden

## Version
5.73

## Category
Kartaverse/KartaVP/Tools

___

## Description
<p>The Kartaverse "kvrLens" and "kvrLensStereo" DCTL fuses allows you to distort your imagery using either the "Brown-Conrady", "Panotools", or "SynthEyes" lens distortion models. The "kvrSTMapGenerator" DCTL fuse allows you to generate an initial STMap template.</p>

<p>Brown-Conrady is popular with computer vision tools like OpenCV, and photogrammetry/NeRF tools. Panotools is used with 360VR panoramic imagery. SynthEyes is used for camera tracking/match moving.</p>

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

## Dependencies

## Deploy

### Common (No Architecture)

> Bin/Kartaverse/LUT/kvrBrownConrady.dctl  
> Bin/Kartaverse/LUT/kvrPanotools.dctl  
> Bin/Kartaverse/LUT/kvrSTMapGenerator.dctl  
> Comps/Kartaverse/KartaVP/kvrLens/kvrLens Distortion Comparison.comp  
> Fuses/Kartaverse/KartaVP/Warp/kvrLens.fuse  
> Fuses/Kartaverse/KartaVP/Warp/kvrLensStereo.fuse  
> Fuses/Kartaverse/KartaVP/Warp/kvrSTMapGenerator.fuse  
