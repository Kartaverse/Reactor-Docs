# KartaVR Tools | Z360
___

## Category
Legacy/Tools/VR

## Author
Andrew Hazelden

## Version
5.7301

___

## Description
<p>The KartaVR legacy Z360 tools allow for depthmap based 360VR 6DoF omni-stereo 3D workflows to be done in Fusion. The overall Z360 approach is also known as "RGBD" if you are using other VR tools.</p>

<p>The source footage for Z360 workflows is an over/under formatted LatLong image that has a color panorama on the top of the frame, and a greyscale depthmap panorama on the bottom of the frame. It is possible for you to use external depthmap generators to prepare the z-depth data required by Z360.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaVR.Tools.Z360.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaVR.Tools.Z360)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360DepthBlur.bmp?ref_type=heads">Macros/KartaVR/Z360/Z360DepthBlur.bmp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360DepthBlur.setting?ref_type=heads">Macros/KartaVR/Z360/Z360DepthBlur.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Extract.bmp?ref_type=heads">Macros/KartaVR/Z360/Z360Extract.bmp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Extract.setting?ref_type=heads">Macros/KartaVR/Z360/Z360Extract.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Merge.bmp?ref_type=heads">Macros/KartaVR/Z360/Z360Merge.bmp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Merge.setting?ref_type=heads">Macros/KartaVR/Z360/Z360Merge.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Mesh3D.bmp?ref_type=heads">Macros/KartaVR/Z360/Z360Mesh3D.bmp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Mesh3D.setting?ref_type=heads">Macros/KartaVR/Z360/Z360Mesh3D.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Renderer3D.bmp?ref_type=heads">Macros/KartaVR/Z360/Z360Renderer3D.bmp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Renderer3D.setting?ref_type=heads">Macros/KartaVR/Z360/Z360Renderer3D.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Stereo.bmp?ref_type=heads">Macros/KartaVR/Z360/Z360Stereo.bmp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360Stereo.setting?ref_type=heads">Macros/KartaVR/Z360/Z360Stereo.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360VRDolly.bmp?ref_type=heads">Macros/KartaVR/Z360/Z360VRDolly.bmp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Macros/KartaVR/Z360/Z360VRDolly.setting?ref_type=heads">Macros/KartaVR/Z360/Z360VRDolly.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Edit/Effects/KartaVR/Z360/Z360DepthBlur.png?ref_type=heads">Templates/Edit/Effects/KartaVR/Z360/Z360DepthBlur.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Edit/Effects/KartaVR/Z360/Z360DepthBlur.setting?ref_type=heads">Templates/Edit/Effects/KartaVR/Z360/Z360DepthBlur.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Edit/Effects/KartaVR/Z360/Z360Stereo.png?ref_type=heads">Templates/Edit/Effects/KartaVR/Z360/Z360Stereo.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Edit/Effects/KartaVR/Z360/Z360Stereo.setting?ref_type=heads">Templates/Edit/Effects/KartaVR/Z360/Z360Stereo.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Edit/Effects/KartaVR/Z360/Z360VRDolly.png?ref_type=heads">Templates/Edit/Effects/KartaVR/Z360/Z360VRDolly.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Edit/Effects/KartaVR/Z360/Z360VRDolly.setting?ref_type=heads">Templates/Edit/Effects/KartaVR/Z360/Z360VRDolly.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360DepthBlur.png?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360DepthBlur.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360DepthBlur.setting?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360DepthBlur.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Extract.png?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Extract.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Extract.setting?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Extract.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Merge.png?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Merge.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Merge.setting?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Merge.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Mesh3D.png?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Mesh3D.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Mesh3D.setting?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Mesh3D.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Renderer3D.png?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Renderer3D.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Renderer3D.setting?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Renderer3D.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Stereo.png?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Stereo.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360Stereo.setting?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360Stereo.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360VRDolly.png?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360VRDolly.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Tools.Z360/Templates/Fusion/KartaVR/Z360/Z360VRDolly.setting?ref_type=heads">Templates/Fusion/KartaVR/Z360/Z360VRDolly.setting</a></li>
</ul>
