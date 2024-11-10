# SimpleOutline
___

## Category
Tools

## Author
Benjamin Bobkin

## Version
1.0

___

## Description
<strong>Simple Outline</strong>
<br>
As the name suggests it is a simple Outline Tool for the <strong>Fusion Page</strong>.
The outline keeps its size, no matter the resoulution.
<br>
<br>

Features:

<ul>
<li>creating a Border (either Round or Sharp)</li>
<li>Changing the color of the border, with all the same controls as the Background Node</li>
<li>"OutsideOnly" Controls, limit the Outline/Border to the outside of the input</li>
<li>options to render the border only</li>
</ul>

<br>
<br>
<strong>How to use the Border Only Controls?</strong>
<br>

you can check "Border Only" to only get the Border as an Output, without the source Image.
The "Grow Inside" Options allws the Border to be drawn on the inside aswell. It is simmilar to other apps, where you have "outside" (here: unchecked) and "both"/"centerd" (here: checked)
KEEP IN MIND: When checking the "Grow Inside" checkbox the Outside Only Controls won't work anymore (in this case you would want the inside anyways)
Which leads me to the next point:
<br>
<br>
<strong>How to use the Outside Only Controls?</strong>
<br>
the slider to change FIRST is the "Fill Ammount", this will slowly remove the Border/Outline from the inside of your Input.
However this might destroy the edges, by loosing details in the edges. This is where the "Fill Fix Edges" slider comes into place.
This should only be used if the edges are ruined, on its own it should NOT be used to get rid of the outlines on the inside. Adjust it slightly untlill the Edges are fixed.
If the edges can't be fixed with those two slider, there is always the option to use the Effect Mask input to manualy remove the Outline/Border from the image at specific parts.

KEEP IN MIND to use both sliders just untill they comoplete the job, not further:
Fill Ammount, should be used untill every inside edge is fully removed (even if the edges a ruined), not a bit further,
then, and only then you should use the Fill Fix Edges Slider if you are unhyppy with the edges. Adjusting the Slider to much will only ruin it more.
These contorlls might not always Work

___

## Download

Download a zipped atom package for offline installation:
> [com.BenjaminBobkin.SimpleOutline.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.BenjaminBobkin.SimpleOutline)  

## Dependencies

> [com.wesuckless.Switch](com.wesuckless.Switch.md)  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.BenjaminBobkin.SimpleOutline/Macros/BenjaminBobkin/SimpleOutline.setting?ref_type=heads">Macros/BenjaminBobkin/SimpleOutline.setting</a></li>
</ul>
