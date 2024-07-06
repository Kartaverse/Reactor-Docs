# Vonk | FusionScriptVal
___

## Author
 : Andrew Hazelden

## Version
 : v1.711

## Category
 : Kartaverse/Vonk Ultra/Modifiers
___

## Description
<p>FusionScriptVal is a node based data encapsulation library for Blackmagic Design Fusion.</p>

<p>The ScriptVal datatype in Fusion is used to pass Lua tables that hold arbitrary data between nodes. This makes it possible to create custom c-code struct like records that travel through the node graph in a seamless fashion.</p>

<p>Open-Source License<br>
The Vonk fuses are licensed under a GPL v3 license.</p>

<p>The original Spicy Acorn Vonk toolset was created by<br>
<a href="mailto:xmnr0x23@gmail.com">Kristof Indeherberge</a><br>
<a href="mailto:duriau.cedric@live.be">Cédric Duriau</a></p>

<p>The Vonk Ultra fork is maintained by:<br>
<a href="mailto:andrew@andrewhazelden.com">Andrew Hazelden</a></p>
___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Comps/Kartaverse/Vonk Ultra/Demo ScriptVal/Demo ScriptVal Vector Graphics 1.comp  
> Comps/Kartaverse/Vonk Ultra/Demo ScriptVal/Demo ScriptVal Vector Graphics 2.comp  
> Comps/Kartaverse/Vonk Ultra/Demo ScriptVal/Demo ScriptVal Vector Graphics 3.comp  
> Comps/Kartaverse/Vonk Ultra/Demo ScriptVal/Demo ScriptVal Vector Graphics 4.comp  
> Comps/Kartaverse/Vonk Ultra/Demo ScriptVal/Demo ScriptVal.comp  
> Comps/Kartaverse/Vonk Ultra/Demo ScriptVal/Media/vray.exr  
> Comps/Kartaverse/Vonk Ultra/Demo ScriptVal/Table/ScriptVal.table  
> Defaults/Fuse.vScriptValDoString_vScriptValDoString.setting.bak  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Array/vScriptValFromArray.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Array/vScriptValToArray.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Create/vScriptValCreate.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Create/vScriptValFromApp.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Create/vScriptValFromCSV.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Create/vScriptValFromDate.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Create/vScriptValFromListFiles.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Create/vScriptValFromPingHosts.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Create/vScriptValFromPrefs.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Create/vScriptValFromRegistry.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Custom Data/vScriptValFromCustomData.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Custom Data/vScriptValToCustomData.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Flow/vScriptValSwitch.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Flow/vScriptValWireless.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Font/vScriptValFontMetrics.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Font/vScriptValFromListFonts.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/IO/vScriptValFromBinaryFile.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/IO/vScriptValFromClipboard.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/IO/vScriptValFromFile.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/IO/vScriptValToBinaryFile.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/IO/vScriptValToClipboard.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/IO/vScriptValToFile.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Image/vScriptValFromEXRFile.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/JSON/vScriptValFromJSON.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/JSON/vScriptValToJSON.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValGetElementToNumber.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValGetElementToTable.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValGetElementToText.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValGetElementXYZToNumber.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValGetToNumber.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValGetToTable.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValGetToText.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValKeysToTable.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValKeysToText.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValRemoveElement.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValSetFromNumber.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValSetFromTable.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValSetFromText.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Key Value/vScriptValTrimElement.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Meta/vScriptValFromMetadata.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Meta/vScriptValToMetadata.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Number/vScriptValFromNumber.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Number/vScriptValToNumber.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Point/vScriptValFromPoint.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Point/vScriptValToPoint.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Script/vScriptValDoFile.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Script/vScriptValDoString.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Script/vScriptValDoStringMultiplex.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Shape/vScriptValCreatePolyline.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Temporal/vScriptValAccumulator.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Temporal/vScriptValTimeSpeed.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Temporal/vScriptValTimeStretch.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Text/vScriptValFromText.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Text/vScriptValToText.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Utility/vScriptValCount.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Utility/vScriptValDump.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Utility/vScriptValMerge.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/Utility/vScriptValViewer.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/XML/vScriptValFromXML.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/XML/vScriptValToXML.fuse  
> Fuses/Kartaverse/Vonk Ultra/ScriptVal/YAML/vScriptValFromYAML.fuse  
