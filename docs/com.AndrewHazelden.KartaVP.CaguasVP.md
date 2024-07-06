# KartaVP Example | Caguas VP
___

## Author
 : Andrew Hazelden and Robert Moreno

## Version
 : v5.73

## Category
 : Kartaverse/KartaVP/Comps
___

## Description
<h2>Overview</h2>

<p>This Kartaverse stitching example shows an interesting workflow that batch stitches a PTGui Pro v12 .pts file inside of Fusion's node graph. The Kartaverse PT data nodes parse the .pts file to extract the location of the PTGui Pro batch rendered panoramic image.</p>

<p>Finally, rest of the example composite shows how to create a simulated virtual production LED video stage wall using Fusion's 3D workspace. The panoramic imagery is automatically placed onto this LED video wall surface. A Camera3D node can then be flown around inside the virtual production stage filming volume to create previz versions of shots with the wrap-around live-action background plate visible.</p>

<h2>About the Footage</h2>

<p>The "Nighttime View of Caguas, Puerto Rico (Dec 2021)" media was filmed by <a href="https://www.instagram.com/cave_manpr/">Robert Moreno</a>. Robert's photographic process helped produced a cylindrical image projection output, with plenty of overlap to allow for precise artist-controlled blending and masking of each view.</p>

<p>This sample footage was captured using a Nikon D750 Camera with an AF DX Fisheye-Nikkor 10.5mm F/2.8 ED lens. A Nodal Ninja panoramic head was adjusted to an indexed rotation value of 15 degrees per view rotation increment, and 12 view angles were captured in the Nikon RAW NEF image format starting at 1:30 AM, local time on 2021-12-08. The pictures had an average of a 30 second exposure time, ISO 1600, aperture F/8, and the content was captured using a manual exposure mode.</p>

<h2>Requirements</h2>
<p>Kartaverse "PT" data nodes, "Vonk Ultra", and "kvrViewer" from the Reactor Package Manager.</p>

___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Comps/Kartaverse/KartaVP/Caguas VP/Caguas VP v001.comp  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/Caguas VP Cylinder.pts  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/Caguas VP Cylinder_hdr.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0001.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0002.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0003.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0004.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0005.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0006.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0007.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0008.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0009.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0010.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0011.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.0012.exr  
> Comps/Kartaverse/KartaVP/Caguas VP/Media/EXR/Fisheye-Nikkor.ifl  
> Comps/Kartaverse/KartaVP/Caguas VP/docs/Readme.md  
> Comps/Kartaverse/KartaVP/Caguas VP/docs/images/comp_vp_previz.png  
> Comps/Kartaverse/KartaVP/Caguas VP/docs/images/npp_for_fusion_json_pts_viewing.png  
> Comps/Kartaverse/KartaVP/Caguas VP/docs/images/pt_nodes_1.png  
> Comps/Kartaverse/KartaVP/Caguas VP/docs/images/pt_nodes_2.png  
> Comps/Kartaverse/KartaVP/Caguas VP/docs/images/stitched_cylinder.jpg  
