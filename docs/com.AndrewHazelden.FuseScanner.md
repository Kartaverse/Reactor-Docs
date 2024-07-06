# Fuse Scanner
___

## Author
Andrew Hazelden

## Version
3.141

## Category
Scripts/Reactor

___

## Description
<p>The Fuse Scanner script creates a UI Manager tree view filled with details about all of the .fuse files installed in your Fusion "Fuses:" and "LUTs:" PathMap folders.</p>

<p>The [x] Expand PathMaps checkbox at the top of the window allows you to see the filepath as a full absolute path, or as a relative PathMap location shortened down to a compact form. This is useful if you want to see in a quick glance if the fuse is coming from a "LUTs:" or "Fuses:" location.</p>

<p>The [x] Show Duplicate Fuse IDs checkbox at the top of the window filters the tree view contents so you only see Fuses that have matching (duplicate) Fuse ID values. This makes it easy to see when you have multiple fuses installed that have the same internal name to Fusion regardless of what the filename on disk is.</p>

<p>Single click on a row to copy the filepath to your clipboard. Double click on a row to open the containing folder. Scroll the Tree view horizontally to the right to see the extra columns.</p>

<p>This Tree view has information sourced from the fuse FuRegisterClass function settings like:</p>

<pre>
  FuRegisterClass (fuseID), (regClass)
  REGS_Name
  REG_Version
  REGS_Category
  REGS_OpIconString
  REGS_OpDescription
  REGS_Company
  REGS_URL
  REGS_HelpTopic
  REG_TimeVariant
  REG_SupportsDoD
  REG_NoMotionBlurCtrls
  REG_NoObjMatCtrls
  REG_NoBlendCtrls
  REG_OpNoMask
</pre>

___

## Dependencies

## Deploy

### Common (No Architecture)

> Scripts/Comp/Andrew Hazelden/Fuse Scanner.lua  
