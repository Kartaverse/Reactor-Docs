# ToolManagement
___

## Author
Alexey Bogomolov

## Version
1.32

## Category
Scripts/Comp

___

## Description
<h1>Tool Management scripts</h1>
<p>This submission installs two scripts that allow to manage multiple tools at once. They essentially do the same job, but internally work differently, so you can choose, which tool to use. 
The main difference between them: <code>Tool Tagger</code> uses comp data to store tool tags and select them based on this data. <code>Tool Comment Manager</code> works on a per-tool basis and stores tags in a tool's comments section. Thus, you can have a visible representation of the tagged tools in a flow (if you hover with the mouse over the tool, you'll see the tag, assigned to it, prepended with <code>%</code> symbol). This tool will erase any comment already assigned to the tagged tool, so don't use it if you want them to be intact.</p>
<p>Either of these scripts is a great companion to a recently released to Reactor <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?p=35321#p35321">Attribute Spreadseet script</a>. Tag some tools with a Tool Management script and select these tools to adjust inputs with the <code>Attribute spreadsheet</code>. This is a very convenient workflow once you get used to it.</p>
<h2>Tool Tagger</h2>
<p>This is a comp data driven tool manager for making basic operations with groups Fusion nodes, such as: <em>disable, enable, toggle passthrough</em> (disabled tools become enabled and vice versa), <em>select</em> and <em>lock</em>. </p>
<p>I wrote this script when I realized I would like to keep comments in some tools. This script has some advantages over the comment manager (see in description), and I actually prefer using it. </p>
<p><em>Description:</em></p>
<p>This script operates with comp data, and does not change tool comments at all. The <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?p=22734#p22734">idea</a> belongs to @PingKing. Here's his proof of concept video: <a href="https://www.youtube.com/watch?v=RmlzyVVHkIM">https://www.youtube.com/watch?v=RmlzyVVHkIM</a>. You can group different tools by assigning a special tag to them. The main difference with <code>Tool Comment Manager</code> - you can assign any number of tags to the same tool. So you can manage, say, <code>Merge1</code> and <code>Merge2</code> with a tag <em>"My favorite Merges"</em>, and <code>Merge1</code>, <code>Merge3</code> and <code>Merge4</code> with <em>"Some Merges I'm slowly starting to hate"</em> tag. This would be virtually impossible to do with a comment driven script. Unfortunately, unlike Tool Comment Manager, there won't be any visual representation of the tagged tools in a flow.</p>
<p>List of the tags will be shown in the middle section. If the text field underneath is empty, the script will be managing all tools of the same ID.</p>
<p><em>Usage:</em></p>
<ol>
<li>Select single Merge tool, click 'Disable' and all Merge tools in a comp will be disabled.</li>
<li>Select some nodes, i.e. last two merges, then fill the text field: "<em>my favorite merges</em>".</li>
<li>Click <code>Set Tag</code> or hit <code>Enter</code> to add tag to selected tools. The tag will appear in comments list.</li>
<li>Now click Disable, and only tools with assigned tag will be disabled.</li>
<li>Press <code>Delete Tag</code> button to delete the tag from the list and from the comp data.</li>
<li>You can Exclude the tool(s) from particular tag with the dedicated button. 
<li>Doubleclick on a tag to select tha tagged tools</li>
<li>Use Refresh button to load tags in a different comp without relaunching the script</li>
</ol>

<h2>Tool Comment Manager</h2>
<p>This is a comment based tool manager for making basic operations with Fusion nodes, such as: <em>disable, enable, toggle passthrough</em> (disabled tools become enabled and vice versa), <em>select</em> and <em>lock</em>. </p>
<p><em>Description:</em></p>
<p>This script is an evolution of @SirEdric's <a href="https://www.steakunderwater.com/VFXPedia/96.0.243.189/images/SE_PriorityPassthrough.eyeonscript">Priority Passthrough script</a>. You can group different tools by assigning a special comment to them. The tool manager will operate only tools with a given comment. List of the comments will be shown in the middle section. If the text field underneath is empty, the script will be managing all tools of the same ID. The script tags tools with a comment rather than internal tool data, in order the tagged tools would be visible in a Flow.</p>
<p><em>Usage:</em></p>
<ol>
<li>Select single Merge tool, click 'Disable' and all Merge tools in a comp will be disabled.</li>
<li>Select some nodes, i.e. last two merges, then fill the text field: "<em>my favorite merges</em>". </li>
<li>Click <code>Set or Replace comment</code> or hit <code>Enter</code>. The given comment will be applied to the selected tools. ALso, this comment will appear in comments list. Next time you click Disable, only these two tools will be disabled. </li>
<li>The comment added to the tool will be prepended with <code>@</code> symbol. Thus, ToolManager will not list other commented tools. </li>
<li>To clear the comment, press clear button in text field, then with tools selected press Set comment. The comments will be cleared. This can be applied to any tools with comments, not only the managed ones.</li>
<li>Doubleclick on comments list to manually refresh it. I will probably replace this redundant function later to show the list of tagged tools in a console, just like the <code>Tool Tagger</code> does.</li>
</ol>

<p><em>Copyright:</em> Alexey Bogomolov (mail@abogomolov.com)</p>
<p><em>License:</em> <a href="https://mit-license.org/">MIT</a></p>
<p><em>Version:</em> v.1.3 - &#91;2020/12/08&#93;</p>
<i>update v1.31</i>: fix Resolve 17 compatibility (omit __flags data)<li>



___

## Dependencies

## Deploy

### Common (No Architecture)

> Scripts/Comp/Tool Management/ToolCommentManager.lua  
> Scripts/Comp/Tool Management/ToolTagger.lua  
