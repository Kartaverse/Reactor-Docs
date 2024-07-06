# Toolbar for Fusion16
___

## Author
Alexey Bogomolov

## Version
2.84

## Category
Scripts/Comp

___

## Description
<p>This is a Fu9 viewer toolbar replica for Fusion 16, in case you missed for fancy mask buttons and instant fit/100% buttons, DoD etc. Not all original tools are implemented. But those shown at the screenshots are working as expected</p>
<p>You can switch between left and right viewer with buttons.</p>
<p>This toolbar is based on Andrew Hazelden UI Toolbar sample script, I just mapped some buttons. Hope now your Fusion16 workflow will be less painful</p>
<p>For screenshots see WSL forum topic: <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=3071">https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=3071</a></p>
<ul>
    <li>The script works in Fusion16 and Resolve16 on Windows or Mac</li>
	<li>You can start the script even if nothing is loaded to the viewer. You still can add masks and polys</li>
	<li>To use viewer features you still need to load any 2D tool to the viewer</li>
	<li>UI is drawn at the mouse pointer</li>
	<li>The window is borderless by default</li>
	<li>Optional setting is available to render script UI on top of all windows, so you can use it on second monitor too. Set <code>show_on_top</code> to <code>true</code> on line 13 of Toolbar16.lua (this probably works on Windows only)</li>
	<li>checkerboard and gamma/gain sliders buttons are not supported in Fu9</li>
	<li>IsDoDShown(), IsCheckerEnabled() and IsShowGainGamma() are not working properly in Fu9, so default state is set to false</li>
</ul>
<p>v 1.55: </p>
add save window position:<br>
Launch script with shortcut, the window position will be saved in Fusion data, and last position will be restored on next launch.
<p>v 2.1: </p>
-- add preferences window <br>
-- the script now works correctly with 3D viewer<br>
-- you can save preferences for stay on top of all windows and optional remember last position<br>
-- flush button resets position data<br>
-- little triangle button on the right toggles preferences dialogue<br>
-- added check if main UI is already launched to prevent multiple windows<br>
-- added support for Fusion version 16+
<p>v 2.3:</p>
-- add more toolbars button in preferences<br>
-- add close preferences button<br>
-- add toggle TimeVew button<br>
-- add initial window offset based on left viewer window size<br>
-- add optional launch on mouse position<br>
-- if you need to launch the tool at custom position, first set prefs to launch at mouse pos, restart the script, open tool preferences and set Save Position<br>
-- add Fusion9 style View Bar with 4 simple layout presets<br>
-- click Add Toolbars! button to launch Customize Toolbars dialogue <br>
-- toggle UI with launch shortcut (SHIFT+ALT+T)
<p> v 2.4 </p>
-- update ui position on refresh button<br>
-- add toggle layout buttons to reduce buttons count<br>
-- replace TimeView buttom with ExpandViewer button
<p> v 2.6 </p>
-- fix positioning bug in Resolve <br>
-- add Layouter script and preferences button:
<a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?p=29348#p29342">https://www.steakunderwater.com/wesuckless/viewtopic.php?p=29348#p29342</a> <br>
-- add goto currently viewed tool button
<p> v 2.7 </p>
-- add disable JIT for macOS on 16.2, reposition on toggle UI
-- automatic viewer detection: toolbar will operate currently active viewer. If no viewer is active, buttons are used to switch viewers.
-- fix toolbar offset position if native toolbar is enabled
-- add toggle console button in preferences 
<p> v 2.8 </p>
-- add BufferLUT button to toggle in a 3D Viewer (same as go to Global Options -- Buffer LUT -- Enable)
-- no need to refresh Toolbar when adding masks if switched to another comp
<p> v 2.8.1 </p>
-- catch incorrect window dimensions
<p> v 2.8.2 </p>
-- add some consistency to the code, add an option to disable verbose output


___

## Dependencies

## Deploy

### Common (No Architecture)

> Config/toolbar16_conf.fu  
> Layouts/FU16_1mon_bottom-timeview.layout  
> Layouts/FU16_1mon_bottom-timeview_Hide-Inspector.layout  
> Layouts/FU16_1mon_bottom-timeview_Hide-Inspector_Splines.layout  
> Layouts/FU16_1mon_bottom-timeview_Hide-Inspector_Timeline.layout  
> Layouts/FU16_1mon_bottom-timeview_Splines-Only.layout  
> Layouts/FU16_1mon_bottom-timeview_Timeline-Only.layout  
> Layouts/FU16_1mon_default.layout  
> Layouts/FU16_2mon_tl_spline.layout  
> Layouts/FU16_2mon_tl_spline_tw_console.layout  
> Layouts/beta/FU16_1mon_modifiers-detached_tabbed_beta.layout  
> Layouts/beta/FU16_1mon_tabbed_beta.layout  
> Layouts/beta/FU16_2mon_spline_tabbed_beta.layout  
> Layouts/beta/FU16_2mon_t_s_modifiers-detached_no-tabs_beta.layout  
> Layouts/beta/FU16_2mon_tl_spl_timeview_console_tabbed_beta.layout  
> Layouts/beta/MelbFilmSetup.layout  
> Layouts/beta/AbdelrahmanMSaidSetup.layout  
> Scripts/Comp/Toolbar16/Icons/PT_ABuffer.png  
> Scripts/Comp/Toolbar16/Icons/PT_BBuffer.png  
> Scripts/Comp/Toolbar16/Icons/PT_BSpline.png  
> Scripts/Comp/Toolbar16/Icons/PT_Bitmap.png  
> Scripts/Comp/Toolbar16/Icons/PT_Chequers.png  
> Scripts/Comp/Toolbar16/Icons/PT_Circle.png  
> Scripts/Comp/Toolbar16/Icons/PT_Colour.png  
> Scripts/Comp/Toolbar16/Icons/PT_Controls.png  
> Scripts/Comp/Toolbar16/Icons/PT_DisabledBSpline.png  
> Scripts/Comp/Toolbar16/Icons/PT_DisabledBitmap.png  
> Scripts/Comp/Toolbar16/Icons/PT_DisabledCircle.png  
> Scripts/Comp/Toolbar16/Icons/PT_DisabledPaint.png  
> Scripts/Comp/Toolbar16/Icons/PT_DisabledPolyline.png  
> Scripts/Comp/Toolbar16/Icons/PT_DisabledRectangle.png  
> Scripts/Comp/Toolbar16/Icons/PT_DisabledTriangle.png  
> Scripts/Comp/Toolbar16/Icons/PT_DisabledWand.png  
> Scripts/Comp/Toolbar16/Icons/PT_Expand.png  
> Scripts/Comp/Toolbar16/Icons/PT_Guides.png  
> Scripts/Comp/Toolbar16/Icons/PT_Layout01.png  
> Scripts/Comp/Toolbar16/Icons/PT_Layout02.png  
> Scripts/Comp/Toolbar16/Icons/PT_Layout03.png  
> Scripts/Comp/Toolbar16/Icons/PT_LockCold.png  
> Scripts/Comp/Toolbar16/Icons/PT_MultiView.png  
> Scripts/Comp/Toolbar16/Icons/PT_Normalise.png  
> Scripts/Comp/Toolbar16/Icons/PT_One2One.png  
> Scripts/Comp/Toolbar16/Icons/PT_Paint.png  
> Scripts/Comp/Toolbar16/Icons/PT_Polyline.png  
> Scripts/Comp/Toolbar16/Icons/PT_Rectangle.png  
> Scripts/Comp/Toolbar16/Icons/PT_Sliders.png  
> Scripts/Comp/Toolbar16/Icons/PT_SplitBuffer.png  
> Scripts/Comp/Toolbar16/Icons/PT_Stereo.png  
> Scripts/Comp/Toolbar16/Icons/PT_StereoHot.png  
> Scripts/Comp/Toolbar16/Icons/PT_Triangle.png  
> Scripts/Comp/Toolbar16/Icons/PT_Wand.png  
> Scripts/Comp/Toolbar16/Icons/refresh_icon.png  
> Scripts/Comp/Toolbar16/Layouter.lua  
> Scripts/Comp/Toolbar16/Toolbar16.lua  
