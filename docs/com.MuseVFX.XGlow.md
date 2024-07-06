# XGlow
___

## Category
Tools

## Author
Bryan Ray

## Version
1.02

___

## Description
<p>XGlow performs an iterative glow, with kernels based on either exponential growth or the Fibonacci Sequence. It's faster than the existing Exponential Glow macros and has some additional color options.</p>

<p><strong>Mode:</strong> The Exponential mode spreads faster and generally has a less intense core.</p>

<p><strong>Threshold:</strong> Values below the low end of the Threshold will not glow. Values above the high end will glow with maximum strength. There is a gradual falloff of glow strength from high to low.</p>

<p><strong>Gain:</strong> Pre-process on the source image. This occurs _after_ the threshold.</p>

<p><strong>Source Saturation:</strong> Pre-process on the source image. It doesn't affect the actual source image, but it does modify the color that is used to perform the blurs.</p>

<p><strong>Glow Saturation:</strong> Strength of a progressive desaturation of the glow—colors will become more or less intense with each iteration.</p>

<p><strong>Glow Size:</strong> The initial blur kernel size. X and Y glow kernels can be unlocked and adjusted separately if desired.</p>

<p><strong>Iterations:</strong> The number of glows to perform.</p>

<p><strong>Falloff:</strong> The rate at which the brightness of the glow decreases.</p>

<p><strong>Gradient:</strong> The glow can be recolored with this control. The first iteration will be the color of the left edge, and the final iteration will _add_ the color of the right edge. The gradient is additive, so you may not wind up with exactly the colors you're expecting.</p>

<p><strong>Glow Only:</strong> Turns off the Merge onto the original source image, leaving only the glows.</p>

WSL Development thread: 
<a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?f=17&t=3275">https://www.steakunderwater.com/wesuckless/viewtopic.php?f=17&t=3275</a>

___

## Donation
The author of the atom has suggested a donation of "$2 USD".  
You can donate using the URL: <a href="paypal.me/BryanRayVFX" class="button">paypal.me/BryanRayVFX</a>
## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.XGlow/Fuses/Blur/MT_XGlow.fuse?ref_type=heads">Fuses/Blur/MT_XGlow.fuse</a></li>
</ul>
