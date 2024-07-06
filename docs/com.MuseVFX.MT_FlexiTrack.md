# FlexiTrack
___

## Author
BryanRay

## Version
2.0

## Category
Tools/Tracking

___

## Description
<p>FlexTrack is a tracking helper that lets you apply a partial stabilization or matchmove, using already-existing tracking data. It only works with the basic Track node, not the Planar or Camera Trackers.</p>

<h3>Usage</h3>
<p>Perform your Track, as usual. Create the MT_FlexiTrack node. Drag your Tracker node to the Tracker input field in FlexiTrack's control panel. If you wish to stabilize, simply put FlexiTrack after your footage and set the sliders for the amount of stabilization you want: A value of 0 turns stabilization off entirely. A value of 1 applies 100% of the stabilization. There are separate sliders for X and Y, so you could, for instance, remove all vertical bounce but leave horizontal motion intact.</p>

<p>If you want to matchmove instead of stabilizing, click the Export Destabilizer button to create a copy of the node that applies the data in reverse. There is, unfortunately, no way to determine what order controls appear in when creating a node by script, so the controls in the Destabilizer will appear in a random order.</p>

<p>WSL thread: <a href=https://www.steakunderwater.com/wesuckless/viewtopic.php?f=6&t=1492&p=18725>FlexiTrack: A stabilize helper macro</a>. https://www.steakunderwater.com/wesuckless/viewtopic.php?f=6&t=1492&p=18725</p>

___

## Dependencies

## Deploy

### Common (No Architecture)

> Macros/Tracking/MT_FlexiTrack.setting  
