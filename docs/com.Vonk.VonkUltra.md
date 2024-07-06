# Vonk Ultra
___

## Category
Kartaverse/Vonk Ultra

## Author
Andrew Hazelden

## Version
1.8

___

## Description
<p>Vonk Ultra is a collection of data nodes for Blackmagic Design Resolve/Fusion. Vonk can be thought of as node-based modifiers that live in the flow. These node-based operations provide a no-code alternative to using expressions or custom scripts. Data nodes are tools that allow you to interconnect nodes together by supporting more data types for the input and output connections such as numbers, text, spreadsheets, CSV, JSON, XML, YAML, metadata, arrays, matrices, and more.</p>

<p>These data node-based techniques encourage a more seamless interchange of information between DCC tools by reducing the loss of important metadata, removing manual data entry steps that can be error-prone, and keep data flowing through a pipeline in a more organized and consistent way.</p>

<p>The long-term hope of Vonk's developers is to help encourage artists and TDs to adopt "data node" concepts across a full production pipeline. These approaches are beneficial for teams working on cutting-edge projects in the motion graphics, VFX, XR, computer vision, machine learning, video/photogrammetry, and digital production/VP space.</p>

<p>Vonk's wide range of nodes include the newly added "vFileSystem" fuses which make it possible for a comp/pipeline TD to port the conceptual ideas found in a typical pipeline shell-script (.bat/.sh) into a fully node-based "Visual Shell Scripting'' paradigm that can run cross-platform inside of Resolve/Fusion/Fusion Render Node. This is effective if it's late at night, your brain focus is fading fast, and you need to quickly whip up in 15 minutes or less a general purpose data processing tool to solve an immediate production challenge.</p>

<p>Open-Source License<br>
The Vonk fuses are licensed under a GPL v3 license.</p>

<p>Acknowledgements<br>
The original Spicy Acorn Vonk toolset was created by<br>
<a href="mailto:xmnr0x23@gmail.com">Kristof Indeherberge</a><br>
<a href="mailto:duriau.cedric@live.be">Cédric Duriau</a></p>

<p>The Vonk Ultra fork is maintained by:<br>
<a href="mailto:andrew@andrewhazelden.com">Andrew Hazelden</a></p>

<p>Documentation<br>
The <a href="https://docs.google.com/document/d/1U9WfdHlE1AZHdU6_ZQCB1I2nSa5I7TyHG2vKMi2I7v8/edit?usp=sharing">Vonk Ultra documentation</a> is accessible on Google Docs.</p>

<p>Local PDF formatted Vonk documentation can be read on disk at:<br>
<a href="file://Reactor:/Deploy/Docs/Kartaverse/Vonk Ultra/Vonk Ultra Data Nodes.pdf">Reactor:/Deploy/Docs/Kartaverse/Vonk Ultra/Vonk Ultra Data Nodes.pdf</p>

<p>If you would like to provide feedback on the evolution of the Vonk data nodes, please check out the <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?p=41165#p41165">development thread on the Steakunderwater forum</a>.</p>



___

## Dependencies

> [com.AndrewHazelden.JSONFromFile.DragDrop](com.AndrewHazelden.JSONFromFile.DragDrop.md ':class=button')  
> [com.AndrewHazelden.vTextFromFile.DragDrop](com.AndrewHazelden.vTextFromFile.DragDrop.md ':class=button')  
> [com.Exosite.LuaYAML](com.Exosite.LuaYAML.md ':class=button')  
> [com.KyleSmith.utf8](com.KyleSmith.utf8.md ':class=button')  
> [com.ManoelCampos.xml2lua](com.ManoelCampos.xml2lua.md ':class=button')  
> [com.MichaelLutz.LuaMatrix](com.MichaelLutz.LuaMatrix.md ':class=button')  
> [com.Vonk.Fusion3D](com.Vonk.Fusion3D.md ':class=button')  
> [com.Vonk.FusionArray](com.Vonk.FusionArray.md ':class=button')  
> [com.Vonk.FusionBase64](com.Vonk.FusionBase64.md ':class=button')  
> [com.Vonk.FusionCBOR](com.Vonk.FusionCBOR.md ':class=button')  
> [com.Vonk.FusionColor](com.Vonk.FusionColor.md ':class=button')  
> [com.Vonk.FusionFileSystem](com.Vonk.FusionFileSystem.md ':class=button')  
> [com.Vonk.FusionGradient](com.Vonk.FusionGradient.md ':class=button')  
> [com.Vonk.FusionGuide](com.Vonk.FusionGuide.md ':class=button')  
> [com.Vonk.FusionImage](com.Vonk.FusionImage.md ':class=button')  
> [com.Vonk.FusionJSON](com.Vonk.FusionJSON.md ':class=button')  
> [com.Vonk.FusionMatrix](com.Vonk.FusionMatrix.md ':class=button')  
> [com.Vonk.FusionMeta](com.Vonk.FusionMeta.md ':class=button')  
> [com.Vonk.FusionNumber](com.Vonk.FusionNumber.md ':class=button')  
> [com.Vonk.FusionPoint](com.Vonk.FusionPoint.md ':class=button')  
> [com.Vonk.FusionScriptVal](com.Vonk.FusionScriptVal.md ':class=button')  
> [com.Vonk.FusionShape](com.Vonk.FusionShape.md ':class=button')  
> [com.Vonk.FusionText](com.Vonk.FusionText.md ':class=button')  
> [com.Vonk.FusionUSD](com.Vonk.FusionUSD.md ':class=button')  
> [com.Vonk.FusionVector](com.Vonk.FusionVector.md ':class=button')  
> [com.Vonk.FusionYAML](com.Vonk.FusionYAML.md ':class=button')  
> [com.Vonk.Scripts](com.Vonk.Scripts.md ':class=button')  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Vonk.VonkUltra/Comps/Kartaverse/Vonk Ultra/Vonk Ultra.drp?ref_type=heads">Comps/Kartaverse/Vonk Ultra/Vonk Ultra.drp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Vonk.VonkUltra/Docs/Kartaverse/Vonk Ultra/Vonk Ultra Data Nodes.pdf?ref_type=heads">Docs/Kartaverse/Vonk Ultra/Vonk Ultra Data Nodes.pdf</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Vonk.VonkUltra/Docs/Kartaverse/Vonk Ultra/com.Vonk.VonkUltra.md?ref_type=heads">Docs/Kartaverse/Vonk Ultra/com.Vonk.VonkUltra.md</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Vonk.VonkUltra/Docs/Kartaverse/Vonk Ultra/gpl-3.0.txt?ref_type=heads">Docs/Kartaverse/Vonk Ultra/gpl-3.0.txt</a></li>
</ul>
