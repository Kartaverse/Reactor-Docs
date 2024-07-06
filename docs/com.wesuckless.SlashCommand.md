# Console Slash Commands
___

## Author
Fusion Reactor

## Version
1.0

## Category
Console

___

## Description
<p>Allows custom script-based console commands to be executed simply by prefixing them with a slash (/)</p>
	
<h2>Usage</h2>

<p>SlashCommand based scripts are installed in the Fusion user prefs "Scripts:/SlashCommand/" folder.</p>

<p>If your custom SlashCommand script was called "foo.lua" or "foo.py", then you would run it in the console using:</p>
<pre>/foo &lt;options&gt;</pre>

<p>SlashCommand .lua scripts work by reading the args[] value that is passed to the script from the Console view. This allows the script to decode each of the parameters that are passed to it.</p>

___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.SlashCommand/Fuses/Console/SlashCommand.fuse?ref_type=heads">Fuses/Console/SlashCommand.fuse</a></li>
</ul>
