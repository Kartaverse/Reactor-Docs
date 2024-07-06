# Hypertext Compositor
___

## Author
 : Andrew Hazelden

## Version
 : v1.2

## Category
 : Docs
___

## Description
<h2>Overview</h2>

<p>The Hypertext Compositor script looks for an HTML formatted sidecar .htm webpage file in the same folder as a .comp file. This allows you to pass along an illustrated guide about the composite to other users. Hypertext Compositor supports the use of custom Fusion comp based HTML "a href" anchor codes to create guided tutorials that can control the Fusion timeline, adjust comp settings, add nodes/macros/media/3D models, run scripts, and display content in the viewer window when you click on the hyperlinks in Fusion 16-17+/Resolve 16-17+. If you "Shift+Click" on a hyperlink a preview of the URL will be displayed.</p>

<p>In Fusion Standalone/Resolve v16-17+ you can also drag an .htm file from your desktop and drop it in the Nodes view and the webpage will be displayed in a new window.<p>

<p>If you would like to learn how to use the custom "a href" anchor codes, look in the header of the "<a href="Reactor:/Deploy/Config/HypertextCompositor/">Reactor:/Deploy/Config/HypertextCompositor/</a>" folder based scripts for more information.</p>

<h2>What is an SxS or SBS?</h2>

<p>Hypertext Compositor was inpired by an old-school Fusion term called "SxS" / "SBS" / "Side-by-Side" that is used to represent an approach where a .lua script could be run by Fusion as soon as a .comp file of the same name was opened in the Fusion GUI, or when the composite was being rendered by the "Fusion Render Node" program. The Hypertext Compositor extends this Side-by-Side system to support comp specific documentation.</p>

<h2>Hypertext Compositor Usage</h2>

<p>If you had a composite called "wesuckless.comp", the SBS html sidecar file would be named "wesuckless.htm". When the composite is opened using the "File &gt; Open..." or "File &gt; Open Recent &gt; " menu items, the matching HTML guide would be displayed automatically.</p>

<h2>Sticky Note SBS Macro</h2>

<p>If you regulary move between Resolve and Fusion Studio Standalone, you might find it handy to add a "Sticky Note SBS" macro to your composite, in place of a regular "Note" node. The "Sticky Note SBS" macro has a button added to the UI in the Inspector view labelled "Display SBS Help" which can be edited in a programmer's text editor like Notepad++ (Windows), BBedit (MacOS), or GEDIT (Linux) to pre-enter a PathMap based filepath for the SBS sidecar .htm file on disk. This allows Resolve users to open the Hypertext Compositor guide that matches the current Fusion page composite.</p>

<h2>Email Andrew Hazelden</h2>
<p><a href="mailto:andrew@andrewhazelden.com">andrew@andrewhazelden.com</a></p>

___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Config/HypertextCompositor/HypertextCompositor.fu  
> Config/HypertextCompositor/HypertextCompositor.lua  
> Config/HypertextCompositor/HypertextCompositorEditor.lua  
> Config/HypertextCompositor/icons/asterisk_32px.png  
> Config/HypertextCompositor/icons/bold_32px.png  
> Config/HypertextCompositor/icons/calendar_32px.png  
> Config/HypertextCompositor/icons/close_32px.png  
> Config/HypertextCompositor/icons/code_32px.png  
> Config/HypertextCompositor/icons/create_32px.png  
> Config/HypertextCompositor/icons/folder_32px.png  
> Config/HypertextCompositor/icons/heading_32px.png  
> Config/HypertextCompositor/icons/image_32px.png  
> Config/HypertextCompositor/icons/italic_32px.png  
> Config/HypertextCompositor/icons/link_32px.png  
> Config/HypertextCompositor/icons/list_32px.png  
> Config/HypertextCompositor/icons/list_ordered_32px.png  
> Config/HypertextCompositor/icons/open_32px.png  
> Config/HypertextCompositor/icons/paragraph_32px.png  
> Config/HypertextCompositor/icons/quit_32px.png  
> Config/HypertextCompositor/icons/quote_32px.png  
> Config/HypertextCompositor/icons/refresh_32px.png  
> Config/HypertextCompositor/icons/save_32px.png  
> Config/HypertextCompositor/icons/sbs-cursor.png  
> Config/HypertextCompositor/icons/sbs-dark-magic-wand.png  
> Config/HypertextCompositor/icons/sbs-magic-wand.png  
> Config/HypertextCompositor/icons/strike_32px.png  
> Config/HypertextCompositor/icons/table_32px.png  
> Config/HypertextCompositor/icons/tint_32px.png  
> Config/HypertextCompositor/icons/underline_32px.png  
> Macros/Hypertext Compositor/Sticky Note SBS.setting  
> Scripts/Comp/Hypertext Compositor/Hypertext Compositor Editor.lua  
