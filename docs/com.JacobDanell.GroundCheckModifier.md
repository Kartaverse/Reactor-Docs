# Ground Check
___

## Category
Modifiers

## Author
Jacob Danell

## Version
1.0

___

## Description
<div style="text-align: center"><strong>Ground Check Modifier</strong></div><br/>
<br/>
This modifier lets you easily place an object on an uneven ground.<br/>
Add the modifier to a position controller eg the Center controller in the transform node.<br/>
Connect the ground-image to the modifier and if the locator ends up under ground it will get pushed up to the surface.<br/>
<br/>
The angle is the direction the point will be pushed towards until it reaches the surface.<br/>
Search distance is the percentage of the resolution for the modifier to search for the ground plane.<br/>
If you have two surfaces above each other you might need to lower the search distance so the locator doesn't jump to the surface above.<br/>
<br/>
Changelog:<br/>
v1.0, 2024-01-09:<br/>
- First release!<br/>
<br/>
com.JacobDanell.GroundCheckModifier.zip

___

## Donation
The author of the atom has suggested a donation of "$5".  
You can donate using the URL: <a href="https://www.paypal.me/danell" class="button">https://www.paypal.me/danell</a>
## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.GroundCheckModifier/Fuses/Modifiers/GroundCheckModifier.fuse?ref_type=heads">Fuses/Modifiers/GroundCheckModifier.fuse</a></li>
</ul>
