# KartaVP Example | Dual Fisheye
___

## Category
Kartaverse/KartaVP/Comps

## Author
Andrew Hazelden

## Version
5.8

___

## Description
<h1>Dual Fisheye Stitching Comps</h1>

<p>The example comps process dual fisheye media from Samsung Gear360, Ricoh Theta, and YI 360 VR cameras into a monoscopic 2D LatLong image projection output.</p>

<p>The included kvrDualFisheye effects template works with footage from a dual circular fisheye lens camera. It expects footage that has a pair of front and back circular fisheye lens images merged into the same frame layout. The default settings for the macro have been tuned for a Samsung Gear360 camera.</p>

<p>When this atom package is installed you can explore the example Fusion composites in this folder:</p>
<pre><a href="file://Reactor:/Deploy/Comps/Kartaverse/WarpStitch/Dual Fisheye/">Reactor:/Deploy/Comps/Kartaverse/WarpStitch/Dual Fisheye/</a></pre>

<h2>Effects Template Usage</h2>
<p>In the Resolve Edit page, the "kvrDualFisheye" macro can then be dragged from the Effects Library "Effects &gt; KartaVP &gt; Warp" category onto a clip in the timeline. Select the clip and then open the Inspector view to adjust the parameters using the "Effects &gt; Fusion &gt; kvrDualFisheye" item.</p>

<p>In the inspector view, if you click the little magic wand icon next to the right of the heading "kvrDualFisheye" you can hop into the Fusion page to customize the macro node. Double clicking on the "kvrDualFisheye" node in the Fusion page allows you to expand the group to access the nodes that are stored inside the group object.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye)  

## Dependencies

> [com.AndrewHazelden.KartaVP.Tools.kvrCropStereo](com.AndrewHazelden.KartaVP.Tools.kvrCropStereo.md)  
> [com.AndrewHazelden.KartaVP.Tools.kvrLens](com.AndrewHazelden.KartaVP.Tools.kvrLens.md)  
> [com.AndrewHazelden.KartaVP.Tools.kvrViewer](com.AndrewHazelden.KartaVP.Tools.kvrViewer.md)  
> [com.AndrewHazelden.KartaVR.Tools.Images](com.AndrewHazelden.KartaVR.Tools.Images.md)  
> [com.AndrewHazelden.KartaVR.Tools.WarpStitch](com.AndrewHazelden.KartaVR.Tools.WarpStitch.md)  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Effects Library.png?ref_type=heads">Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Effects Library.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Inspector Controls.png?ref_type=heads">Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Inspector Controls.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Nodes.png?ref_type=heads">Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Nodes.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Readme.txt?ref_type=heads">Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Readme.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Comps/Kartaverse/WarpStitch/Dual Fisheye/Ricoh Theta v001.comp?ref_type=heads">Comps/Kartaverse/WarpStitch/Dual Fisheye/Ricoh Theta v001.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Comps/Kartaverse/WarpStitch/Dual Fisheye/Samsung Gear360 v001.comp?ref_type=heads">Comps/Kartaverse/WarpStitch/Dual Fisheye/Samsung Gear360 v001.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Comps/Kartaverse/WarpStitch/Dual Fisheye/YI 360 VR Office Interior v001.comp?ref_type=heads">Comps/Kartaverse/WarpStitch/Dual Fisheye/YI 360 VR Office Interior v001.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Comps/Kartaverse/WarpStitch/Dual Fisheye/YI 360 VR Parking Lot v001.comp?ref_type=heads">Comps/Kartaverse/WarpStitch/Dual Fisheye/YI 360 VR Parking Lot v001.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Macros/KartaVR/Warp/kvrDualFisheye.png?ref_type=heads">Macros/KartaVR/Warp/kvrDualFisheye.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Macros/KartaVR/Warp/kvrDualFisheye.setting?ref_type=heads">Macros/KartaVR/Warp/kvrDualFisheye.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Templates/Edit/Effects/KartaVP/Warp/kvrDualFisheye.png?ref_type=heads">Templates/Edit/Effects/KartaVP/Warp/kvrDualFisheye.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Templates/Edit/Effects/KartaVP/Warp/kvrDualFisheye.setting?ref_type=heads">Templates/Edit/Effects/KartaVP/Warp/kvrDualFisheye.setting</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Templates/Fusion/KartaVP/Warp/kvrDualFisheye.png?ref_type=heads">Templates/Fusion/KartaVP/Warp/kvrDualFisheye.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Comps.WarpStitch.DualFisheye/Templates/Fusion/KartaVP/Warp/kvrDualFisheye.setting?ref_type=heads">Templates/Fusion/KartaVP/Warp/kvrDualFisheye.setting</a></li>
</ul>
