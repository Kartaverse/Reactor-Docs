# Blurred Edges Restoration
___

## Author
Gregory Chalenko

## Version
4.5

## Category
Tools/Matte

___

## Description
<p>This macro expands the actual color of the objects so that it extends through the entire blurred areas, replacing the background color mixture.</p>

<p>There is always an issue with keying defocused and motion blurred objects: the color on the edges is mixed with the color of the background. Basically, the problem arises even with static objects which are in focus, because there is always some softness in the practical image. The most obvious solution to this is either to suppress (desaturate) the background color or to shrink the objects' edges.</p>

<p>In first case, you may have a problem if the background luminance is different, for instance, if you key dark objects against white (like trees against the sky). In second case, the blurring may be so strong, that the objects disappear completely with shrinking.</p>

<p>VFXPedia Thread:<br>
https://www.steakunderwater.com/VFXPedia/96.0.243.189/index8206.html?title=Settings_and_Macros/BlurredEdgesRestoration_Description</p>

<p>by Gregory Chalenko<br>
http://www.compositing.ru/Research/Tools/BlurredEdgesRestoration/</p>

___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.GregoryChalenko.BlurredEdgesRestoration/Macros/Matte/BlurredEdgesRestoration.setting?ref_type=heads">Macros/Matte/BlurredEdgesRestoration.setting</a></li>
</ul>
