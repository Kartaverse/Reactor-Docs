# Krokodove for Fusion/Resolve Studio 17
___

## Author
Komkom Doorn

## Version
8.2

## Category
Tools/Plugins

___

## Description
<h1>KROKODOVE v8.20.01</h1>

<p>Krokodove is a plugin for Fusion and DaVinci Resolve Studio on Windows, Mac and Linux. It includes 100+ free Fusion tools.</p>

<p>This Reactor Atom contains Krokodove 8 <strong>for Fusion/Resolve Studio 17, for Windows and macOS only</strong>.</p>

<h3>This package installs Krokodove as KrokodoveFu17.plugin which means it will not overwrite any existing Krokodove installs for earlier versions of Fusion.<br>
Because different Fusion versions share resources, however, this also means that earlier Fusion versions will throw an error on startup.<br><br>
To uninstall, follow the removal instructions below.</h3>

<h2>Updating Krokodove on Windows</h2>

<p>While Fusion is running, plugin files are write protected by the OS. Please follow these steps if you are updating Krokodove through Reactor:</p>
<ol>
	<li>Select the <strong>Reactor > Advanced > Show Reactor Folder</strong> menu item. An Explorer folder browsing window will appear.</li>
	<li>Quit Fusion so the plugin file is not write locked.</li>
	<li>Navigate to the <strong>"<a href="Reactor:/Deploy/Plugins/">Reactor:/Deploy/Plugins/</a>"</strong> folder using the Explorer folder browsing window and manually throw out the <strong>"KrokodoveFu17.plugin"</strong> file.</li>
	<li>Fusion can be restarted and the new KKD plugin can be installed using Reactor.</li>
</ol>

<h2>Krokodove on macOS</h2>

<p>The Krokodove plugin is a universal binary release that includes ARM64 and Intel64 architecture support. macOS Big Sur 10.15 is the minimum OS requirement to be able to use the KKD plugin.</p>

<h2>License</h2>
<p>Krokodove is distributed for free.<br> 

<h2>Krokodove Blog:</h2>
<p>http://www.krokodove.com</p>

<h2>Krokodove Vimeo:</h2>
<p>https://vimeo.com/channels/krokodove</p>

<h2>Krokodove Facebook:</h2>
<p>https://www.facebook.com/krokodove</p>

<h2>Email:</h2>
<p>raf@komkomdoorn.com</p>

___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
</ul>

### macOS

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.KomkomDoorn.KrokodoveFu17/Mac/Plugins/KrokodoveFu17.plugin?ref_type=heads">Plugins/KrokodoveFu17.plugin</a></li>

### Windows

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.KomkomDoorn.KrokodoveFu17/Windows/Plugins/KrokodoveFu17.plugin?ref_type=heads">Plugins/KrokodoveFu17.plugin</a></li>
