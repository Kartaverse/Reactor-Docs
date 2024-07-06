# KartaVR Tools | WarpStitch Ultra
___

## Author
Andrew Hazelden

## Version
5.73

## Category
Kartaverse/KartaVR/Tools

___

## Description
<p>Kartaverse "kvrWarpStitch" is a hardware accelerated DCTL fuse for Resolve/Fusion that allows you warp and stitch fisheye imagery into an equirectangular/spherical/LatLong image projection panoramic video. Floating-point 16-bit per channel, and 32-bit per channel image processing is supported so you can work with bracket merged high dynamic range data and stitch the media into a spherical HDRI.</p>

<p>The DCTL support in WarpStitch allows the same fuse code to run equally well in a cross-platform fashion on Windows/Linux/macOS systems running across CUDA, OpenCL, and Metal GPU hardware.</p>

<p>The code was ported by David Kohen (<a href="https://www.youtube.com/LearnNowFX">Learn Now FX</a>), and Andrew Hazelden. WarpStitch is based upon proof of concept code provided by Chad Capeland's CustomShader3D "3CuS Sample: Warping Fisheye to Equirectangular" CG fragment shader.</p>

<h2>DCTL Fuse Support Requirements</h2>

<ul>
	<li>An OpenCL, CUDA, or Metal based GPU</li>
	<li>Fusion Studio 17-19+ or Resolve 17-19+</li>
</ul>

<h2>Open Source Software License</h2>
<p>LGPL 3.0 license</p>

<h2>Under the Bridge Example</h2>
<p>The "Under the Bridge" example stitching comp is now available as a separate atom package in Reactor. This streamlines the installation of the WarpStitch Ultra fuse.</p>


___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.WarpStitch/Fuses/Kartaverse/KartaVR/Warp/kvrWarpStitchUltra.fuse?ref_type=heads">Fuses/Kartaverse/KartaVR/Warp/kvrWarpStitchUltra.fuse</a></li>
</ul>
