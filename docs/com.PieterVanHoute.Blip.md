# Blip
___

## Category
Modifiers

## Author
Pieter Van Houte

## Version
2.52

___

## Description
<font color=#ffd100><h2>Blip</h2></font>

<p>Remember the last time you had to animate single frame events in your comp? Muzzle flashes, anyone? Flickering light bulbs? Lightning strikes? Glitchy motion graphics perhaps?</p>

<p>Simply do those little events by typing in the frames where you want them. Super fast, super easy. </p>

<h3>A quick rundown of the available parameters:</h3>


<ul>
<li><b>Rest Value</b>: the base value of your parameter. This is the value the Modifier will output on non-Blip Frames. </li>
<li><b>Blip Value</b>: the value the Modifier outputs on the frames defined as Blip Frames. </li>
<li><b>Blip Length</b>: doesn't have to be single frame Blips of course... </li>
<li><b>Attack/Decay</b>: for Blips longer than single frames, you can fade them in or out.</li>
<li><b>Blip Frames</b>: the frames where a Blip starts. You can type one frame per line, comma separate them, space, tab, up to you. You can be as sloppy as you damn well like! v1.4+ also supports ranges such as 1-10.</li>
<li><b>Frame Scale</b>: Scale yor Blip frames, for example Blip frame 10 will become Blip frame 20 with Frame Scale set to 2.</li>
<li><b>Frame Offset</b>: As above, and following the following order of operations: Frame Scale first, then Frame Offset (and you get a preview of all that so you don't have to count inside your precious head!).</li>
<li><b>Supports decimal values!</li>
</ul>

<font color=#ffd100><h2>Blip 2.5 -- massive overhaul!</h2></font>

<h3>Thanks to <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?p=57799#p57799">input of the mighty JustCropIt</a>, version 2.5 introduces Repeats!</h3>

<p>Rather than trying to explain exactly what it does, it's really worth reading the topic.</p>

<h3>A quick rundown of the added parameters:</h3>


<ul>
<li><b>Repeat Blip</b>: how many times the blips defined in Blip Frames will be repeated - works with ranges too! </li>
<li><b>Repeat Offset</b>: inserts an Offset between the repeats (in whole frames). </li>
<li><b>Value Multiplier</b>: at 1 it does nothing, at 0.5 it halves the Blip Value of every repeated Blip (at 2 it doubles it). So with a Repeat Blip set to 2 instead of the Blip values being 1, 1, 1 they'd be 1, 0.5, 0.25. </li>
<li><b>Multiplier Curve</b>: controls the Value Multiplier, Linear is as the example above, Expo is exponential allowing for easing in/out, and Spline is just wild - play with it! </li>
<li><b>Value Overlap</b>: what happens when repeated blips are starting to overlap - keep the original Blip Value, Replace the Blip Value with the value of the repetition (post multiplier curve) or add both values together. </li>
</ul>

<h4>If you like Blip and the time it saves you, please consider <a href="https://www.patreon.com/wesuckless">becoming a We Suck Less Patron</a></h4>

<h3>We Suck Less companion topic:</h3>

<p><a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3485">https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3485</a></p>

___

## Donation
The author of the atom has suggested a donation of "".  
You can donate using the URL: <a href="https://www.patreon.com/wesuckless">https://www.patreon.com/wesuckless</a>

## Download

Download a zipped atom package for offline installation:
> [com.PieterVanHoute.Blip.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.PieterVanHoute.Blip)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.PieterVanHoute.Blip/Fuses/Modifiers/Blip.fuse?ref_type=heads">Fuses/Modifiers/Blip.fuse</a></li>
</ul>
