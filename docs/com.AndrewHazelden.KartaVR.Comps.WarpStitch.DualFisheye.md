# KartaVP Example | Dual Fisheye
___

## Author
 : Andrew Hazelden

## Version
 : v5.7301

## Category
 : Kartaverse/KartaVP/Comps
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

## Dependencies

> com.AndrewHazelden.KartaVP.Tools.kvrCropStereo  
> com.AndrewHazelden.KartaVP.Tools.kvrLens  
> com.AndrewHazelden.KartaVP.Tools.kvrViewer  
> com.AndrewHazelden.KartaVR.Tools.Images  
> com.AndrewHazelden.KartaVR.Tools.WarpStitch  

___

## Deploy

### Common (No Architecture)

> Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Effects Library.png  
> Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Inspector Controls.png  
> Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Images/Nodes.png  
> Comps/Kartaverse/WarpStitch/Dual Fisheye/Docs/Readme.txt  
> Comps/Kartaverse/WarpStitch/Dual Fisheye/Ricoh Theta v001.comp  
> Comps/Kartaverse/WarpStitch/Dual Fisheye/Samsung Gear360 v001.comp  
> Comps/Kartaverse/WarpStitch/Dual Fisheye/YI 360 VR Office Interior v001.comp  
> Comps/Kartaverse/WarpStitch/Dual Fisheye/YI 360 VR Parking Lot v001.comp  
> Macros/KartaVR/Warp/kvrDualFisheye.png  
> Macros/KartaVR/Warp/kvrDualFisheye.setting  
> Templates/Edit/Effects/KartaVP/Warp/kvrDualFisheye.png  
> Templates/Edit/Effects/KartaVP/Warp/kvrDualFisheye.setting  
