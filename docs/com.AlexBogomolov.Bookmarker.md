# Bookmarker
___

## Category
Scripts/Comp

## Author
Alexey Bogomolov

## Version
3.12

___

## Description
<p>Bookmarking script for your flow.</p>
<p>Add bookmarks for selected or active tool. Set custom bookmark name or use default tool's name. Then invoke jump script and switch instantly to the desired node on your huge comp.</p>
<p>Use <code>SHIFT+A</code> to add bookmark and <code>SHIFT+J</code> to jump between bookmarks. Windows users can additionally jump with <code>DOWN/UP</code> or open bookmarks dropdown with <code>ALT+DOWN</code>.</p>   
<p>Bookmarks are stored in comp metadata, so they will remain after Fusion restart. The script requires 64-bit Python (v2.7.+ or v3.6.+).
Suggestions and PR's are appreciated: https://github.com/movalex/fusion</p>
<p>Features:</p>
<p>Requests and issues: <a href="https://gitlab.com/WeSuckLess/Reactor/tree/movalex/Atoms/com.AlexBogomolov.Bookmarker">https://gitlab.com/WeSuckLess/Reactor/tree/movalex/Atoms/com.AlexBogomolov.Bookmarker</a></p>
<p>STU topic and discussion, feature requests and updates: <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=2858">.../wesuckless/viewtopic.php?f=33&t=2858</a></p>
<ul>
	<li>bookmarks can be sorted by name or tool type</li>
	<li>delete single bookmark, multiple bookmarks selected with shift/cmd or reset all with ALT+reset button</li>
	<li>submit bookmark addition on <code>Enter</code></li>
	<li>close window on <code>ESC</code></li>
	<li>tool position is preserved for each bookmark (on Fusion 17)</li>
	<li>rename bookmark (add the same tool with different name)</li>
	<li>refresh bookmarks list if some was added while Jump UI is still running</li>
    <li>move selected tools to a bookmark position</li>
    <li>try to find a bookmarked tool if it was renamed</li>
    <li>refresh bookmarks if you switch comps</li>
<p>update 2.5:</p>
<ul>
<li> add checkbox 'move selected to bookmark'. Move multiple selected nodes available</li>
<li> Jump back and forth between previous and current bookmarks</li>
</ul>
<p>v 2.6:</p>
<ul>
<li> add tool ID next to Bookmark name</li>
<li> add all Underlays as Bookmarks button in Add script</li>
<li> catch error on JumpBack function</li>
</ul>
<p>v 2.71:</p>
<ul>
<li>add 16.2 exception for data parsing since the bug was onlly limited to 16.2</li>
</ul>
<p>v 2.8:</p>
<ul>
<li>Sorting bookmarks by name and tool type</li>
<li>Button to remove orphaned bookmarks</li>
<li>prevent multiple windows to launch </li>
<li>attempt to find tool by ID, if bookmark was not found because tool was renamed</li>
</ul>
<p>v 3.0:</p>
<ul>
<li>use TreeView to store Bookmarks, updated UI</li>
<li>remove Jump Back button and cleanup buttons</li>
<li>use Fusion 17 bookmarking API to store tool position</li>
</ul>
<p>v 3.1:</p>
<ul>
<li>fix Resolve 17+ compatibility (omit __flags data)</li>
</ul>



___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.Bookmarker/Config/Bookmarker/bookmark_cfg.fu?ref_type=heads">Config/Bookmarker/bookmark_cfg.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.Bookmarker/Scripts/Comp/Bookmarker/bookmark_add.py?ref_type=heads">Scripts/Comp/Bookmarker/bookmark_add.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.Bookmarker/Scripts/Comp/Bookmarker/bookmark_jump.py?ref_type=heads">Scripts/Comp/Bookmarker/bookmark_jump.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.Bookmarker/Scripts/Comp/Bookmarker/icons/plus_icon.png?ref_type=heads">Scripts/Comp/Bookmarker/icons/plus_icon.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.Bookmarker/Scripts/Comp/Bookmarker/icons/refresh_icon.png?ref_type=heads">Scripts/Comp/Bookmarker/icons/refresh_icon.png</a></li>
</ul>
