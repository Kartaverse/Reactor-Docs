# Euler Angle Filter
___

## Category
Scripts/Tool

## Author
Bryan Ray

## Version
1.0

___

## Description
<p>Animated 3D geometry imported via FBX or Alembic may contain rotations greater than 360 degrees. 
	Fusion "wraps around" these rotations, resulting in the geometry spinning back around to 0 degrees.
	In the 3d viewport, such a discontinuity is undetectable, but if the renderer has motion blur
	enabled, the large sudden rotation will create an artifact.</p>

<p>To counteract the problem, this script detects large differences between rotation keyframes and 
	modifies the keys to remove the winding errors.</p>

<p>by Bryan Ray for Muse VFX</p>

___

## Donation
The author of the atom has suggested a donation of "".  
You can donate using the URL: <a href="https://www.paypal.com/paypalme/BryanRayVFX" class="button">https://www.paypal.com/paypalme/BryanRayVFX</a>
## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.eulerFilter/Scripts/Tool/MuseVFX/eulerFilter.lua?ref_type=heads">Scripts/Tool/MuseVFX/eulerFilter.lua</a></li>
</ul>
