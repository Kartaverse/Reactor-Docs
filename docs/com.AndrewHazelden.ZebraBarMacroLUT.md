# ZebraBar MacroLUT
___

## Author
 : Andrew Hazelden

## Version
 : v1.0

## Category
 : Viewshaders
___

## Description
<p>This atom has a MacroLUT modified version of the classic VFXPedia "Zebra" macro. This viewshader can be used in the Fusion Viewer window to visualize super-white values. This macro shows how non-programmer, artistic minded Fusion users could build their own tools in Fusion for doing technical review checks on footage.</p>

<p>Once installed, a "ZebraBar MacroLUT" item is accessible in the Viewer window's LUT menu.</p>

<p>The "Zebra Bars Example.comp" file provides a simple example that has a FastNoise node that has the highlights extending into the super-white territory. The color values on the FastNoise are animated so you can see the zebra bar zone move in the frame where the values exceed an RGB intensity of +1.0.</p>

<h2>Future Modifications</h2>
<p>Since this MacroLUT item is packaged as a GroupOperator node, you can drop the setting file into your Fusion comp from your desktop and access it as a regular macro, too.  This would allow you to expand the ZebraBarLUT group and add any extra nodes you might need to embed like a OpenColorIO node or any other item you feel the need for.</p>___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Comps/Viewshaders/Zebra Bars.comp  
> LUTs/ZebraBarLUT.setting  
