# ExponentialGlow
___

## Author
 : Stefan Ihringer

## Version
 : v1.0

## Category
 : Tools/Blur
___

## Description
<p>This macro creates a photorealistic glow with an exponential falloff.</p>

<p>A glow is just a blur that is added on top of the input image. Fusion's Glow and SoftGlow tools basically work like that and the result usually doesn't look convincing for strong glows (or in linear color space) so you need to create several blurs and glows with different radii to create a nicer-looking falloff. One technique is to add up blurs with radii that increase exponentially: 1, 2, 4, 8, 16 and so on. This macro does all the hard work for you.</p>

<p>ExponentialGlow is designed for linear gamma, floating point images that are viewed using a LUT. If you crank it up you might even see banding in float16, so float32 is recommended.</p>

<p>This macro is based on a tool I found that was attributed to one Stuart Lashley. It's also similar to the great Multistep Blur (you would need to set it to a tiny minimum blur and a huge maximum blur with a high bias value to create a similar look). Also, this macro supports DoD and has been optimized to prevent unnecessary re-rendering when gain or tint are adjusted.</p>

<p>VFXPedia &gt; Settings and Macros &gt; ExponentialGlow<br>
https://www.steakunderwater.com/VFXPedia/96.0.243.189/index2f2f.html?title=Settings_and_Macros/ExponentialGlow_Description</p>

<p>Pigsfly Forum &gt; Lightswoosh Thread<br>
http://pigsfly.com/index.php?/topic/8208-lightswoosh/?hl=exponentialglow</p>
___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Macros/Blur/ExponentialGlow.setting  
