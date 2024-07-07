# Attribute Spreadsheet
___

## Category
Scripts/Comp

## Author
Alexey Bogomolov

## Version
0.33

___

## Description
<h1>Attribute Spreadsheet</h1>
<p><a href="https://www.svenneve.com/?p=792">Attribute Spreadsheet</a> was written by Sven Neve (House of Secrets) in 2013. This is my attempt of reviving this tool while adding new features to it.</p>
<p><em>AttributeSpreadsheet</em> is a spreadsheet script to edit the input parameters of multiple Fusion tools at once. It is extremely useful for batch tool changes, and a great help for any motion graphics tasks. The most amazing part that it works with any native or third party Fusion tool, such as OFX plugins, macros, Krokodove tools and so on. Any available input is accessible from a very convenient table view. You can link any input to another with expression by a middle mouse drag. Some tools, such at Text+ <code>Font</code> or <code>Style</code>, does not even allow setting expression manually. With <em>AttributeSpreadsheet</em> you can do that easily too. As far as I know, this is the fastest, and the most reliable tool for a batch changing parameters or linking multiple Fusion inputs. It should definitely be in Reactor.</p>
<p><em>Requirements:</em></p>
<ul>
<li>Python 3.8+</li>
<li>Fusion Standalone v.18, Davinci Resolve v.18</li>
<li>PySide6 (can be installed automatically)</li>
</ul>
<p><em>Usage:</em></p>
<ul>
<li>Select one or more tools in Fusion flow and start the script or press "Refresh" button.</li>
<li>Select multiple values in a single column, say, "Blend".</li>
<li>Start typing new numeric value and hit Enter. All Blend values for selected tools will be changed accordingly. That's the basic functionality.</li>
<li>To link multiple tool's inputs to another tool with expression, select the column and drag with middle-click towards the cell you are linking to. </li>
<li>Enter <code>-x</code> to discard the expression on single or multiple inputs. Once the expression is set, you cannot change the values in the table unless the expression is cleared.</li>
<li>Use <code>+=</code>, <code>-=</code>, <code>*=</code>, <code>/=</code> and <code>%=</code> to do mathematical expressions with current numerical values. for example: enter <code>+=0.2123</code> to default Transform Size value, and it will become <code>1.2123</code></li>
<li>Use search bar to find inputs. You can search for multiple inputs, separated by spaces, like <code>size angle</code> to search both Size and Angle inputs.</li>
<li>Enter numerical values or expression to point values, such as <code>Pivot</code> or <code>Center</code>. For instance, enter <code>=time</code> in the Transform Angle cell will create <code>=time</code> expression, adding <code>=time</code> and <code>0.35</code> in Center <code>X</code> and <code>Y</code> values will create <code>Point(time, 0.35)</code> expression.</li>
<li>Enter <code>p</code> in any table cell and all corresponding input attributes will be listed in Console.</li>
<li>Click on the row header (tool name) to activate the tool.</li>
<li>Click on column header to sort inputs alphabetically. Click on the corner button to reset sorting to default state.</li>
</ul>
<p>Current version has quite large changelog in comparison to the last known version of <code>hos_AttributeSpreadsheet</code>. You can find full list of new features and fixes inside a script file. The most significant improvements:</p>
<ul>
<li>Point data with X and Y elements are both adjustable and now work with mathematical modifiers.</li>
<li>You can add expressions to Point data values, such as <code>Point(Pivot.X, 0.5)</code></li>
<li>Corner button will reset sorting to default state</li>
<li>Tool name and ID is added to a table to improve sorting abilities</li>
<li>Added logging, most errors are caught with Console feedback</li>
<li>Set active tool by clicking on row header</li>
<li>Use this script as a standalone tool (Fusion Studio feature). Provide a remote machine IP as an argument to a script to do remote management</li>
</ul>
<p><em>Automatic PySide6 installation</em></p>
<p>My intention was to make this script as straightforward and easy to use as possible. Usually installing third party package to Python is a painless task. So we go further and strip this step, offering automatic PySide6 installation on a first launch. </p>
<p>If there's no Pyside6 installation found on the computer, the script will show a dialogue, whether you want to install the package automatically. If clicked <code>Ok</code>, it attempts to install Pyside6 using standard pip tools. Otherwise, the command for manual installation will be shown in Console. Python modules manager <code>pip</code> should be already installed on the computer. It is a part of standard Python3 installation, thus the reason the script will require Python3 (also for maintenance purposes). Automatic PySide installation process will be visible in Fusion console. In case installation fails, please report the bug here. Once Pyside is installed, launch the script again and standard UI will be shown:</p>
<p><em>Known issues:</em></p>
<ul>
<li>All fields except numerical or point data inputs are treated as text values. This prevents unexpected behavior when changing cells values. </li>
<li>Although script works perfectly both in Resolve and Fusion Standalone separately, sometimes, when both of these apps are loaded, the script cannot read the comp data properly. In this case you'll see <code>No comp data found. Probably both Resolve and Fusion are loaded?</code> error message. I'm looking forward to handling this issue as soon I understand why this is happening.</li>
<li>You should avoid linking inputs to each other. This is a known bug: if you link <code>Transform1.Size</code> to <code>Transform2.Size</code> and then try to link expression from <code>Transform2.Size</code> back to <code>Transform1.Size</code>, Fusion will crash immediately. The same will happen if you try to do that with a script. Just don't.</li>
</ul>
<p><em>TODO:</em></p>
<ul>
<li>Add combobox to inputs with list data, such as <code>INPIDT_ComboControl_ID</code> or <code>INPIDT_MultiButtonControl_ID</code>, so you could choose the appropriate values from a dropdown instead of typing values manually. This can be tricky, because some Fusion inputs addressed by key ('1.0', '2.0') and some - by value ('Red', 'XYZ' etc). Also, this should probably exclude Fonts.</li>
<li>Add a completer with the most commonly used search commands. For instance, if you've already been searching <code>red green blue</code>, this query will be suggested once you type <code>r</code> in search area.</li>
<li>Add an option for partial middle-drag/linking Point data, such as link only <code>X</code> values, or only <code>Y</code>, so the expression would be like <code>Point(Transform1.Center.X, 0.5)</code>. Currently, it is possible by typing expression text to a Point X cell.</li>
<li>Add <code>Select by ID</code> button to quickly select and load to the table all tools with the same ID as the active tool. However, this can be done with ToolManager script, so questionable.</li>
<li>Please suggest any other improvements.</li>
</ul>

<p><em>Copyright:</em> 2011-2013, Sven Neve (House of Secrets); 2019-2023 additions by Alexey Bogomolov</p>
<p><em>License:</em> <a href="https://mit-license.org/">MIT</a></p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AlexBogomolov.AttributeSpreadsheet.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AlexBogomolov.AttributeSpreadsheet)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.AttributeSpreadsheet/Scripts/Comp/AttributeSpreadsheet/AttributeSpreadsheet.py?ref_type=heads">Scripts/Comp/AttributeSpreadsheet/AttributeSpreadsheet.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AlexBogomolov.AttributeSpreadsheet/Scripts/Comp/AttributeSpreadsheet/install_pip_package.py?ref_type=heads">Scripts/Comp/AttributeSpreadsheet/install_pip_package.py</a></li>
</ul>
