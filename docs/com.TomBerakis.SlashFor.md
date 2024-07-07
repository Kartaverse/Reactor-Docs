# For Slash Command
___

## Category
Console

## Author
Tom Berakis

## Version
2.1

___

## Description
<p>The /for slash-command is used to quickly and easily apply changes across a number of tools.</p>
<p>Version 2 includes new additions for batch renaming nodes, with setting the clip name and node attributes, and selectively rendering branches of a comp by Movalex and Andrew Hazelden. Also a version up/down versioning feature was adapted from code by PingKing</p>

<h2>Usage</h2>
<pre>&gt; /for
Usage: /for (selected|visible|all) &#91;tooltype&#91;,tooltype...&#93;&#93; &#91;where &lt;condition&gt;&#93; &lt;command&gt; &#91; & &lt;command&gt;...&#93;
Supported commands:
animate &lt;input&gt; &#91;(with &lt;modifier&gt;|remove)&#93; &#91;force&#93;
color &#91;tile &lt;color&gt;&#93; &#91;text &lt;color&gt;&#93; &#91;fill &lt;color&gt;&#93;
get &lt;input&gt; (&#91;at &lt;time&gt;&#93;)
render &#91;step &lt;value&gt;&#93; &#91;proxy &lt;value&gt;&#93;
getattrs &lt;attribute&gt;
id
select &#91;(add|remove)&#93;
set &lt;input&gt; (&#91;at &lt;time&gt;&#93; to &lt;value&gt;|expression &lt;exp&gt;)
setattrs &lt;attribute&gt; (to &lt;value&gt;)
setclip (to &lt;value&gt;)
setname (to &lt;value&gt;)
version &#91;(up|down|to &lt;value&gt;)&#93;</pre>

<br><h3>Examples:</h3>

<p>Set the Size of all selected tools to 1.0:</p>
<pre>  /for selected set Size to 1.0</pre>

<p>Set the SeetheRate of all FastNoise tools in the comp to 1.0:</p>
<pre>  /for all FastNoise set SeetheRate to 1.0</pre>

<p>Double the current size of each Merge or Transform currently selected:</p>
<pre>  /for selected Merge,Transform set Size to value*2.0</pre>

<p>Animate Size of all selected tools with default modifier (BezierSpline):</p>
<pre>  /for selected animate Size</pre>

<p>Animate Size of all visible tools (ie not modifiers) with CubicSpline</p>
<pre>  /for visible animate Size with CubicSpline</pre>

<p>Animate Size of all selected tools, replacing any already animated ones:</p>
<pre>  /for selected animate Size force</pre>

<p>Animate Seethe of all FastNoise tools, creating a ramp from 1.0 to 5.0 over 100 frames:</p>
<pre>  /for all FastNoise animate Seethe & set Seethe at 0 to 1.0 & set Seethe at 100 to 5.0</pre>

<p>Remove animation from Size of all selected tools:</p>
<pre>  /for selected animate Size remove</pre>

<p>Set a Seethe expression on selected FastNoise tools:</p>
<pre>  /for selected FastNoise set Seethe expression time/10.0</pre>

<p>Select all FastNoise tools:</p>
<pre>  /for all FastNoise select</pre>

<p>Add all tools where Size &gt; 1 to the selection:</p>
<pre>  /for all where Size &gt; 1.0 select add</pre>

<p>Remove all Merge tools where Angle &lt; 0 from the selection:</p>
<pre>  /for all Merge where Angle &lt; 0 select remove</pre>

<p>Set the tile color to red for selected tools:</p>
<pre>  /for selected color tile 1,0,0</pre>

<p>Set the text color to green for selected FastNoise tools with a non-zero SeetheRate:</p>
<pre>  /for selected FastNoise where SeetheRate ~= 0 color text 0,1,0</pre>

<p>Set the value of the Center setting for selected tools:</p>
<pre>  /for selected set Center to {0.3,0.7}</pre>

<p>Get the selected tools' names for use with /for commands and scripting:</p>
<pre>  /for selected id</pre>

___

## Download

Download a zipped atom package for offline installation:
> [com.TomBerakis.SlashFor.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.TomBerakis.SlashFor)  

## Dependencies

> [com.wesuckless.SlashCommand](com.wesuckless.SlashCommand.md)  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.TomBerakis.SlashFor/Scripts/SlashCommand/for.lua?ref_type=heads">Scripts/SlashCommand/for.lua</a></li>
</ul>
