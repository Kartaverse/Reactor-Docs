# Chemical
___

## Author
SirEdric

## Version
1.1

## Category
Scripts/Comp

___

## Description
<h1 align="center"><sup>&#91;se&#93;</sup>Chemical</h1>

<h3 align="center"> Comp Script</h3>

<p>Script to Import JSON 3D Files of chemical structures as published on<br>
https://www.ncbi.nlm.nih.gov/pccompound</p>

<p>A good example is<br>
https://pubchem.ncbi.nlm.nih.gov/compound/6914120</p>

<p>Follow the thread on WSL here:<br>
https://www.steakunderwater.com/wesuckless/viewtopic.php?f=16&t=1727</p>

<p>For Fusion earlier than 9.0.1 this Script requires the lua JSON library from:</b><br>
https://gist.github.com/tylerneylon/59f4bcf316be525b30ab</p>

<p>to be present in (e.g.) %AppData%\Blackmagic Design\Fusion\Modules\Lua</b></p>

<p>As of Fusion 9.0.1 the dkjson library is already included.</p>

<p>Download the desired .json file from the 3D-Section of any compound on that site.<br>
Run the Script to import that structure into Fusion.</p>
	
<p>Beware! This might create humongous amounts of tools on your flow!
Especially with interesting looking structures like:<br>
https://pubchem.ncbi.nlm.nih.gov/compound/186342#section=2D-Structure</p>

<p>If you want to Render with SuperSampling turned on,<br>
a LineThickness of 10 and MaterialBoost of at least 2 is recommended.</p>

<p>Use the modify script to change the attributes of Atoms and Bonds.</p>

<p>Version 1.1 changes:</p>
<ul>
	<li>Massive improvements for the materials and modification options.</li>
	<li>Option to create text-labels on the atoms.</li>
	<li>General improvements.</li>
</ul>

___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.SirEdric.Chemical/Scripts/Comp/SE_ChemJson_import.lua?ref_type=heads">Scripts/Comp/SE_ChemJson_import.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.SirEdric.Chemical/Scripts/Comp/SE_ChemJson_modify.lua?ref_type=heads">Scripts/Comp/SE_ChemJson_modify.lua</a></li>
</ul>
