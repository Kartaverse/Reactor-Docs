# Batch Change Parameters
___

## Category
Scripts/Comp

## Author
Bryan Ray/MuseVFX

## Version
4.3

___

## Description
<p>This script allows you to change parameters for multiple selected tools simultaneously. The selected tools need not be of the same node type. With Batch Change Parameters's GUI, only the Inputs that the tools have in common will be changed.</p>
<p>This script has been updated and works in Fusion v9-17.2.1+ and Resolve v15+.</p>
<hr />
<h2>We Suck Less Thread:</h2>
<p>Batch Parameter Changer — A Rewrite for Fusion 9
<a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?f=6&amp;p=13401#p13147">https://www.steakunderwater.com/wesuckless/viewtopic.php?f=6&amp;p=13401#p13147</a></p>
<hr />
<h2>Change Log:</h2>
<ul>
<li>
<p><strong>v1.0 - 2007-02-22</strong> (by SlayerK)</p>
<ul>
<li>Initial release</li>
</ul>
</li>
<li>
<p><strong>v2.0 - 2018-01-22</strong> (by Bryan Ray for MuseVFX)</p>
<ul>
<li>Updated for Fusion 9 and UI Manager. Cleaned code and added documentation. Removed orphan and redundant functions. Removed un-implemented math operations code.</li>
</ul>
</li>
<li>
<p><strong>v3 - 2019-11-17</strong> (By Andrew Hazelden for Reactor)</p>
<ul>
<li>Updated to add a copy of "bmd.isin()" function that was renamed to "bcIsIn()" so the script can run in Resolve where the "bmd.scriptlib" file does not exist. Added a TargetID value to the UI Manager window so pressing "Ctrl + W" closes the window instead of the composite.</li>
<li>Added error handling for several nil return values from "fuIDlist" and "uIDAttrs.INPID_InputControl" that caused "gusb()" error messages in the Console.</li>
<li>Adjusted UI Manager GUI weight values to fix Fusion/Resolve v16 GUI rendering issues.</li>
</ul>
</li>
<li>
<p><strong>v4 - 2020-02-05</strong> (by Bryan Ray for MuseVFX)</p>
<ul>
<li>Improved UI formatting</li>
<li>Implemented Operation mode</li>
<li>Appended page to control names.</li>
</ul>
</li>
<li>
<p><strong>v4.1 - 2020-04-03</strong> (by Bryan Ray for MuseVFX)</p>
<ul>
<li>Added handling for expressions</li>
</ul>
</li>
<li>
<p><strong>v4.2 - 2020-05-21</strong> (by Bryan Ray for MuseVFX with input from Movalex)</p>
<ul>
<li>Added handling for Loader and Saver Filename inputs</li>
<li>Added wildcard text handling for filename inputs</li>
<li>use gsub for pattern search.</li>
</ul>
</li>
<li>
<p><strong>v4.3 - 2023-12-20</strong> (changes by stib)</p>
<ul>
<li>Added random operators</li>
<li>Added increment operators</li>
<li>Modernized Lua for counting tables using #table</li>
</ul>
</li>
</ul>

___

## Donation
The author of the atom has suggested a donation of "$3 USD".  
You can donate using the URL: <a href="https://www.paypal.com/paypalme/BryanRayVFX" class="button">https://www.paypal.com/paypalme/BryanRayVFX</a>
## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.BatchChangeParameters/Scripts/Comp/Batch_Change_Parameters.lua?ref_type=heads">Scripts/Comp/Batch_Change_Parameters.lua</a></li>
</ul>
