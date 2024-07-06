# Euler Angle Filter
___

## Author
 : Bryan Ray

## Version
 : v1.0

## Category
 : Scripts/Tool
___

## Description
<p>Animated 3D geometry imported via FBX or Alembic may contain rotations greater than 360 degrees. 
	Fusion "wraps around" these rotations, resulting in the geometry spinning back around to 0 degrees.
	In the 3d viewport, such a discontinuity is undetectable, but if the renderer has motion blur
	enabled, the large sudden rotation will create an artifact.</p>

<p>To counteract the problem, this script detects large differences between rotation keyframes and 
	modifies the keys to remove the winding errors.</p>

<p>by Bryan Ray for Muse VFX</p>___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Scripts/Tool/MuseVFX/eulerFilter.lua  
