# Atom Probe
___

## Author
 : Andrew Hazelden

## Version
 : v2.0

## Category
 : Scripts/Reactor
___

## Description
<p>The Atom Probe script scans your "Reactor:/Deploy/Atoms/" folder or local GitLab Atoms folder to look for .atom package files. The resulting atom folder output is written to the Fusion Console Tab.</p>

<h2>FuScript Terminal Command</h2>

You can also run this tool from a terminal window using the following type of syntax:

<pre>
fuscript -x 'fusion = bmd.scriptapp("Fusion", "localhost");if fusion ~= nil then app = fusion;composition = fu.CurrentComp;comp = composition;SetActiveComp(comp) else print("&#91;Error&#93; Please open up the Fusion GUI before running this tool.") end' -l lua "/Library/Application Support/Blackmagic Design/Fusion/Reactor/Deploy/Scripts/Comp/Andrew Hazelden/Atom Probe Console.lua"
</pre>___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Scripts/Comp/Andrew Hazelden/Atom Probe Console.lua  
