# Retimer
___

## Author
Jacob Danell

## Version
1.2

## Category
Tools/Miscellaneous

___

## Description
<center><h2>Retimer + Retimer3D</h2></center>
<p>Retimer lets you retime your footage or 3D scene but it calculates the retiming on a frame basis.</p>

<br>This means that if you're on frame 100 and changes the speed from 1 to 2, the next frame will be 102 while if you would simply change the clips speed you would end up at frame 200.</br>

<p>The fuse contains three settings:</p>
<ol>
	<li>Nearest - The fuse gets the nearest whole frame</li>
	<li>Blend (for 2D images only) - If you end up at frame 10.5 you will get 50% of frame 10 and 50% of frame 11</li>
	<li>Subframe - If your footage contains subframes, this option will show these subframes. It does NOT generate subframes itself.</li>
</ol>

<p>For 2D images you can enable <strong><i>Show frame in metadata</i></strong> to add the current retimed frame in the metadata. You can later see this in your SubViewer.</p>

<p>For more info, please check:</p>

<br>WSL thread: <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=3703">https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=3703</a></br>


<p>
Changelog:<br/>
1.2, 2020-10-12:<br/>
* Fixed problem for Retimer inside of Resolve Fusion<br/>
<br/>
v1.1, 2020-03-05:<br/>
* Added Retimer3D, retime your 3D scenes!<br/>
* Added an offset slider so you can start your shot somewhere else<br/>
* Cleaned up complicated code so the script now self-reference itself <br/>
<br/>
v1.0.2, 2020-01-19:<br/>
* Change the Interpolation Mode's dropdown/button from ComboControl to MultiButtonControl to make it work better in Fusion 9<br/>
<br/>
v1.0.1, 2020-01-12:<br/>
* Change Interpolation Mode from dropdown list to multi button to work better in Fusion 9<br/>
<br/>
v1.0, 2020-01-09:<br />
* First release!
</p>

___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.Retimer/Fuses/Miscellaneous/Retimer.fuse?ref_type=heads">Fuses/Miscellaneous/Retimer.fuse</a></li>
</ul>
