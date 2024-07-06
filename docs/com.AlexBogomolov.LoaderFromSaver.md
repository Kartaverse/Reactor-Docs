# Loader from Saver
___

## Category
Scripts/Comp

## Author
Alexey Bogomolov

## Version
1.66

___

## Description
<p>Literally create Loader from Saver. Works with multiple savers. Loader is created next to the Saver's position.</p>
<p><i>Features:</i></p>
<ul>
	<li>If the Saver has image sequence with no number padding &#91; <code>0000</code> &#93;, default padding is created.
</li>
	<li>If the file is a container (mov, avi, mp4, mxf) — original name is used. </li>
	<li>Launch this scripts with Saver Manager UI tool (available in Reactor)</li>
    <li>connect the created Loader to Saver's downstream nodes</li>
    <li>convert regular saver to Saver Plus</li>
    <li>add versioning buttons to Saver Plus</li>
    <li>scan existing files and suggest correct sequence numbering if the file is not found or no snum in filepath</li>
</ul>



___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.LoaderFromSaver/Scripts/Comp/Saver Tools/CreateSaverPlus.lua?ref_type=heads">Scripts/Comp/Saver Tools/CreateSaverPlus.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.LoaderFromSaver/Scripts/Comp/Saver Tools/LoaderFromSaver.lua?ref_type=heads">Scripts/Comp/Saver Tools/LoaderFromSaver.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.LoaderFromSaver/Scripts/Support/SaverPlus/ButtonVersionDown.py?ref_type=heads">Scripts/Support/SaverPlus/ButtonVersionDown.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.LoaderFromSaver/Scripts/Support/SaverPlus/ButtonVersionUp.py?ref_type=heads">Scripts/Support/SaverPlus/ButtonVersionUp.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.LoaderFromSaver/Scripts/Tool/ConvertToSaverPlus.lua?ref_type=heads">Scripts/Tool/ConvertToSaverPlus.lua</a></li>
</ul>
