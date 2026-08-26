"""
Atomz Expand.py - v4.1 2026-05-22 07.55 AM (ADT)
By Andrew Hazelden <andrew@andrewhazelden.com>

Overview
---------
The "Atomz Expand" script allows you to import zipped Reactor Atomz Packages by dragging them into the Fusion Nodes view from a desktop Explorer/Finder/Linux folder browsing window.

The DragDrop file supports dragging in multiple zip elements at the same time, and each item will be imported. This allows for easier NAS-based offline Reactor installation use.

You also have the option of importing Atomz package list files (atomz.lst). An atomz list text file works with an IFL image-file-list like document that is stored in the same folder as a collection of atomz zip files. The list is just a text file with a single atomz package name per line that has the .lst file extension added to the filename. Using lst files let you define a custom selection list of packages to be installed at once. This technique can help with bootstrapping a local set of zipped offline usable Atomz packages in a bundle that get bulk loaded in fast.

Atomz.lst Document Example
--------------------------
com.MuseVFX.XGlow.zip
com.PieterVanHoute.SuckLessAudio.zip
com.PieterVanHoute.SuckLessWriteOn.zip
com.Protean.ConvertToRelativePaths.zip
com.Psyop.Cryptomatte.SampleImages.zip
com.RogerMagnusson.ClassBrowser.zip
com.StefanIhringer.srgb_rec709_viewshaders.zip
com.StefanIhringer.XfChroma.zip
com.TomBerakis.SlashFor.zip
com.wesuckless.SlashCommand.zip

Requirements
------------
Python v3.6 to v3.11+ 64-bit

Script Usage
------------
Step 1. Open the "Script > Atomz > Atomz Expand" menu item. In the dialog, select an Atomz packaged .zip file or an Atomz List .lst file. The package will be automatically imported into your "Reactor:" PathMap folder with blazing-fast speed.

The Console window displays the atoms package installation process. This diagnostic information is useful for testing and validating content prepared by the Atomizer GUI.

A file missing entry will be listed in the Console window if an atomz package asks for a file in the .atom deploy textfield that is not present in the zipped folder.

Todo
-----
- Add support for InstallScripts
- Add support for Atom Dependency tags

Version History
----------------
v1.7 2024-07-29 
Added support for expanding GitLab created folder zips of individual atom packages. 

These atomz packages are typically accessed from the Reactor-Docs webpage: https://kartaverse.github.io/Reactor-Docs/

v4.1 2026-05-22
Added support for installing Reactor Standalone "Reactor:/Atomz/" packaged content.

Added support for opening Atom package URL tags in the default web-browser.

"""

import os, shutil, re, csv, datetime, math, zipfile, platform

def GetValue(key, dct, default):
	if key in dct:
		return dct[key]
	else:
		return default

def ImportText(file):
	parentFolder = os.path.dirname(app.MapPath(file))
	textItems = []
	with open(app.MapPath(file), encoding = "utf-8-sig", newline = "") as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) >= 1:
				atom = os.path.join(parentFolder, row[0])
				textItems.append(atom)
	return textItems

def AtomzWindow():
	ui = fu.UIManager
	atomz_disp = bmd.UIDispatcher(ui)

	atomz_dlg = atomz_disp.AddWindow({"WindowTitle": "Atomz Expand", "ID": "AtomzWin", "TargetID" : "AtomzWin", "Geometry": [0, 85, 530, 135], "Spacing": 0,},[
		ui.VGroup({"ID": "root", "Weight": 10.0,},[
			ui.VGroup({
				"Weight": 0.1,
				#"StyleSheet": "background-color: rgb(37, 37, 37);",
			},[
				ui.HGroup({},[
					ui.Label({
						"ID": "ViewLabel",
						"Text": "  Atomz Expand",
						"StyleSheet": "QLabel { color: white; font-weight: bold; font-size: 14px; }",
						"Weight": 0.01,
					}),
				]),
				ui.Label({
					"ID": "DividerLabel",
					"StyleSheet": "QLabel { max-height: 3px; background-color: rgb(76, 154, 109); }",
					"Spacing": 0,
					"Margin": 0,
					"Weight": 0.01,
				}),
			]),
			ui.HGroup({"Weight": 0.0,},[
				ui.Label({"ID": "AtomzLabel", "Text": "Atomz:", "Weight": 0.1}),
				ui.LineEdit({"ID": "AtomzTxt", "Text": "", "PlaceholderText": "Please enter an atomz package (.zip) or atomz list (.lst) filepath.", "Weight": 0.9}),
				ui.Button({"ID": "BrowseButton", "Text": "Browse", "Geometry": [0, 0, 30, 50], "Weight": 0.1}),
			]),
			ui.VGap(10),
			ui.HGroup({"Weight": 0.0,},[
				ui.Button({
					"ID": "CancelButton",
					"Text": "Cancel",
					"Weight": 0.01,
				}),
				ui.Button({
					"ID": "OKButton",
					"Text": "OK",
					"Weight": 0.01,
				}),
			]),
		]),
	])

	atomz_itm = atomz_dlg.GetItems()

	# The window was closed
	def AtomzWinFunc(ev):
		atomz_disp.ExitLoop()
	atomz_dlg.On.AtomzWin.Close = AtomzWinFunc

	# Add your GUI element based event functions here:
	
	def OKButtonFunc(ev):
		atomz_disp.ExitLoop()
	atomz_dlg.On.OKButton.Clicked = OKButtonFunc

	def CancelButtonFunc(ev):
		atomz_itm["AtomzTxt"].Text = ""
		atomz_disp.ExitLoop()
	atomz_dlg.On.CancelButton.Clicked = CancelButtonFunc

	def BrowseButtonFunc(ev):
		selectedPath = fu.RequestFile()
		if selectedPath:
			atomz_itm["AtomzTxt"].Text = str(selectedPath)
	atomz_dlg.On.BrowseButton.Clicked = BrowseButtonFunc

	atomz_dlg.Show()
	atomz_disp.RunLoop()
	atomz_dlg.Hide()

	atomz_path = str(atomz_itm["AtomzTxt"].Text)
	print("\t[Atomz][File Path]", atomz_path)

	# When the window is closed send back the atomz name
	return atomz_path

def ShowWebpage(url):
	hostOS = platform.system()
	viewerPath = ""
	args = ""
	launchCommand = ""
	if hostOS == "Darwin":
		args = "--args"
		launchCommand = ["open"]
		launchCommand.append(url)

		print("[Launching Command]\n")
		print(launchCommand)
		import subprocess
		subprocess.Popen(launchCommand)
	elif hostOS == "Windows":
		# Open the folder in Explorer (Win), Finder (macOS), and xdg-open (Linux)
		os.startfile(url)
	elif hostOS == "Linux":
		launchCommand = ["xdg-open"]
		launchCommand.append(url)

		print("[Launching Command]\n")
		print(launchCommand)
		import subprocess
		subprocess.Popen(launchCommand)

def NativeAtomz(reactor, file):
	# This is an Atomz Create style .zip file hierarchy
	fileBaseName = os.path.basename(file)
	atomName = str(os.path.splitext(fileBaseName)[0]) + ".atom"
	print("[Atomz][Source File]", file)
	print("[Atomz][Atom Name]", atomName)
	if not zipfile.is_zipfile(file):
		print("[Atomz][Zip File Contents Error]")
	else:
		zipFP = zipfile.ZipFile(file, mode = "r")
		if zipFP is None:
			print("[Atomz][Zip File Contents Error]")
			return None
		else:
			try:
				print("[Atomz][Read File]", atomName)
				zipContents = zipFP.read(atomName).decode(encoding = "utf-8")
				print(zipContents)
			except Exception as error:
				zipFP.close()
				print("\t[Unzipping Error]", error)
				return None
			atomDict = bmd.readstring(zipContents)
			if atomDict is None:
				print("[Atomz][Atom Parsing Error]")
				return None
			else:
				name = GetValue("Name", atomDict, "")
				version = GetValue("Version", atomDict, 0.0)
				author = GetValue("Author", atomDict, "")
				print("[Atomz][Info]", name, "v" + str(version), "by", author)

				print("[Atomz][Dict Contents]")
				print(atomDict)
				# allFiles
				# winFiles
				# macFiles
				# linuxFiles

				# Reactor
				atomsDir = os.path.join(reactor, "Atoms", "Reactor")
				result = zipFP.extract(atomName, path = atomsDir)
				print("\n[Install] [Atom]", result)

				# Check the active operating system (Darwin, Windows, Linux)
				hostOS = platform.system()

				print("\n[URL][All]")
				allURL = GetValue("URL", atomDict, {})
				for key in allURL:
					if type(key) is float:
						url = allURL[key]
						print("\t[URL]", url)
						ShowWebpage(url)
				urlLinux = GetValue("Linux", allURL, {})
				urlMac = GetValue("Mac", allURL, {})
				urlWindows = GetValue("Windows", allURL, {})
	
				if hostOS == "Linux":
					print("\n[URL][Linux]")
					for key in urlLinux:
						url = urlLinux[key]
						print("\t[URL]", url)
						ShowWebpage(url)
				if hostOS == "Darwin":
					print("\n[URL][Mac]")
					for key in urlMac:
						url = urlMac[key]
						print("\t[URL]", url)
						ShowWebpage(url)
				if hostOS == "Windows":
					print("\n[URL][Windows]")
					for key in urlWindows:
						url = urlWindows[key]
						print("\t[URL]", url)
						ShowWebpage(url)

				print("\n[Deploy][All]")
				allDeploy = GetValue("Deploy", atomDict, {})
				for key in allDeploy:
					if type(key) is float:
						file = allDeploy[key]
						try:
							result = zipFP.extract(file, path = reactor)
							print("\t[Install]", result)
						except Exception as error:
							print("\t[Install Error]", error)
							return None
				deployLinux = GetValue("Linux", allDeploy, {})
				deployMac = GetValue("Mac", allDeploy, {})
				deployWindows = GetValue("Windows", allDeploy, {})

				if hostOS == "Linux":
					print("\n[Deploy][Linux]")
					for key in deployLinux:
						file = deployLinux[key]
						try:
							src = "Linux/" + str(file)
							dest = str(file)
							zipFP.getinfo(src).filename = dest
							result = zipFP.extract(src, path = reactor)
							print("\t[Install]", result, "\t\t[Src]", src)
						except Exception as error:
							print("\t[Install Error]", error)
							return None
				if hostOS == "Darwin":
					print("\n[Deploy][Mac]")
					for key in deployMac:
						file = deployMac[key]
						try:
							src = "Mac/" + str(file)
							dest = str(file)
							zipFP.getinfo(src).filename = dest
							result = zipFP.extract(src, path = reactor)
							print("\t[Install]", result, "\t\t[Src]", src)
						except Exception as error:
							print("\t[Install Error]", error)
							return None
				if hostOS == "Windows":
					print("\n[Deploy][Windows]")
					for key in deployWindows:
						file = deployWindows[key]
						try:
							src = "Windows\\" + str(file)
							dest = str(file)
							zipFP.getinfo(src).filename = dest
							result = zipFP.extract(src, path = reactor)
							print("\t[Install]", result, "\t\t[Src]", src)
						except Exception as error:
							print("\t[Install Error]", error)
							return None
				zipFP.close()
	return 1

def GitLabSourcedAtomz(reactor, file):
	if os.path.basename(file).startswith("Reactor-master-Atoms-"):
		# This is a GitLab live folder download built zip
		fileBaseName = os.path.basename(file)
		dirtyAtomBaseName = str(os.path.splitext(fileBaseName)[0])
		cleanAtomBaseName = str(os.path.splitext(fileBaseName)[0]).replace("Reactor-master-Atoms-", "")
		atomName = str(cleanAtomBaseName + ".atom")
		fileSubFolder = dirtyAtomBaseName + "/Atoms/" + cleanAtomBaseName + "/"
		print("[Atomz][GitLab Download][Source File]", file)
		print("[Atomz][GitLab Download][Atom Name]", atomName)
		if not zipfile.is_zipfile(file):
			print("[Atomz][Zip File Contents Error]")
		else:
			zipFP = zipfile.ZipFile(file, mode = "r")
			if zipFP is None:
				print("[Atomz][Zip File Contents Error]")
				return None
			else:
				try:
					print("[Atomz][GitLab Download][Read File]", fileSubFolder + atomName)
					zipContents = zipFP.read(fileSubFolder + atomName).decode(encoding = "utf-8")
					print(zipContents)
				except Exception as error:
					zipFP.close()
					print("\t[Unzipping Error]", error)
					return None
				atomDict = bmd.readstring(zipContents)
				if atomDict is None:
					print("[Atomz][Atom Parsing Error]")
					return None
				else:
					name = GetValue("Name", atomDict, "")
					version = GetValue("Version", atomDict, 0.0)
					author = GetValue("Author", atomDict, "")
					print("[Atomz][Info]", name, "v" + str(version), "by", author)
		
					print("[Atomz][Dict Contents]")
					print(atomDict)
					# allFiles
					# winFiles
					# macFiles
					# linuxFiles
		
					# Reactor
					atomsDir = os.path.join(reactor, "Atoms", "Reactor")
					src = fileSubFolder + str(atomName)
					dest = str(atomName)
					result = zipFP.extract(src, path = atomsDir)
					print("\n[Install] [Atom]", result)
		
					# Check the active operating system (Darwin, Windows, Linux)
					hostOS = platform.system()

					print("\n[URL][All]")
					allURL = GetValue("URL", atomDict, {})
					for key in allURL:
						if type(key) is float:
							url = allURL[key]
							print("\t[URL]", url)
							ShowWebpage(url)
					urlLinux = GetValue("Linux", allURL, {})
					urlMac = GetValue("Mac", allURL, {})
					urlWindows = GetValue("Windows", allURL, {})
		
					if hostOS == "Linux":
						print("\n[URL][Linux]")
						for key in urlLinux:
							url = urlLinux[key]
							print("\t[URL]", url)
							ShowWebpage(url)
					if hostOS == "Darwin":
						print("\n[URL][Mac]")
						for key in urlMac:
							url = urlMac[key]
							print("\t[URL]", url)
							ShowWebpage(url)
					if hostOS == "Windows":
						print("\n[URL][Windows]")
						for key in urlWindows:
							url = urlWindows[key]
							print("\t[URL]", url)
							ShowWebpage(url)

					print("\n[Deploy][All]")
					allDeploy = GetValue("Deploy", atomDict, {})
					for key in allDeploy:
						if type(key) is float:
							file = allDeploy[key]
							try:
								src = fileSubFolder + str(file)
								dest = str(file)
								zipFP.getinfo(src).filename = dest
								result = zipFP.extract(src, path = reactor)
								print("\t[Install]", result)
							except Exception as error:
								print("\t[Install Error]", error)
								return None
					deployLinux = GetValue("Linux", allDeploy, {})
					deployMac = GetValue("Mac", allDeploy, {})
					deployWindows = GetValue("Windows", allDeploy, {})
		
					if hostOS == "Linux":
						print("\n[Deploy][Linux]")
						for key in deployLinux:
							file = deployLinux[key]
							try:
								src = fileSubFolder + "Linux/" + str(file)
								dest = str(file)
								zipFP.getinfo(src).filename = dest
								result = zipFP.extract(src, path = reactor)
								print("\t[Install]", result, "\t\t[Src]", src)
							except Exception as error:
								print("\t[Install Error]", error)
								return None
					if hostOS == "Darwin":
						print("\n[Deploy][Mac]")
						for key in deployMac:
							file = deployMac[key]
							try:
								src = fileSubFolder + "Mac/" + str(file)
								dest = str(file)
								zipFP.getinfo(src).filename = dest
								result = zipFP.extract(src, path = reactor)
								print("\t[Install]", result, "\t\t[Src]", src)
							except Exception as error:
								print("\t[Install Error]", error)
								return None
					if hostOS == "Windows":
						print("\n[Deploy][Windows]")
						for key in deployWindows:
							file = deployWindows[key]
							try:
								src = fileSubFolder + "Windows/" + str(file)
								dest = str(file)
								zipFP.getinfo(src).filename = dest
								result = zipFP.extract(src, path = reactor)
								print("\t[Install]", result, "\t\t[Src]", src)
							except Exception as error:
								print("\t[Install Error]", error)
								return None
					zipFP.close()
	return 1

def ReactorStandaloneSourcedAtomz(reactor, file):
	# This is a Reactor Standalone atomz content
	fileBaseName = os.path.basename(file)
	dirtyAtomBaseName = str("Reactor-master-Atoms-") + str(os.path.splitext(fileBaseName)[0])
	cleanAtomBaseName = str(os.path.splitext(fileBaseName)[0]).replace("Reactor-master-Atoms-", "")
	atomName = str(cleanAtomBaseName + ".atom")
	fileSubFolder = dirtyAtomBaseName + "/Atoms/" + cleanAtomBaseName + "/"
	print("[Atomz][Reactor Standalone Download][Source File]", file)
	print("[Atomz][Reactor Standalone Download][Atom Name]", atomName)
	if not zipfile.is_zipfile(file):
		print("[Atomz][Zip File Contents Error]")
		return None
	else:
		zipFP = zipfile.ZipFile(file, mode = "r")
		if zipFP is None:
			print("[Atomz][Zip File Contents Error]")
			return None
		else:
			try:
				print("[Atomz][Reactor Standalone Download][Read File]", fileSubFolder + atomName)
				zipContents = zipFP.read(fileSubFolder + atomName).decode(encoding = "utf-8")
				print(zipContents)
			except Exception as error:
				zipFP.close()
				print("\t[Unzipping Error]", error)
				return None
			atomDict = bmd.readstring(zipContents)
			if atomDict is None:
				print("[Atomz][Atom Parsing Error]")
			else:
				name = GetValue("Name", atomDict, "")
				version = GetValue("Version", atomDict, 0.0)
				author = GetValue("Author", atomDict, "")
				print("[Atomz][Info]", name, "v" + str(version), "by", author)
	
				print("[Atomz][Dict Contents]")
				print(atomDict)
				# allFiles
				# winFiles
				# macFiles
				# linuxFiles
	
				# Reactor
				atomsDir = os.path.join(reactor, "Atoms", "Reactor")
				src = fileSubFolder + str(atomName)
				dest = str(atomName)
				result = zipFP.extract(src, path = atomsDir)
				print("\n[Install] [Atom]", result)
	
				# Check the active operating system (Darwin, Windows, Linux)
				hostOS = platform.system()
	
				print("\n[URL][All]")
				allURL = GetValue("URL", atomDict, {})
				for key in allURL:
					if type(key) is float:
						url = allURL[key]
						print("\t[URL]", url)
						ShowWebpage(url)
				urlLinux = GetValue("Linux", allURL, {})
				urlMac = GetValue("Mac", allURL, {})
				urlWindows = GetValue("Windows", allURL, {})
	
				if hostOS == "Linux":
					print("\n[URL][Linux]")
					for key in urlLinux:
						url = urlLinux[key]
						print("\t[URL]", url)
						ShowWebpage(url)
				if hostOS == "Darwin":
					print("\n[URL][Mac]")
					for key in urlMac:
						url = urlMac[key]
						print("\t[URL]", url)
						ShowWebpage(url)
				if hostOS == "Windows":
					print("\n[URL][Windows]")
					for key in urlWindows:
						url = urlWindows[key]
						print("\t[URL]", url)
						ShowWebpage(url)

				print("\n[Deploy][All]")
				allDeploy = GetValue("Deploy", atomDict, {})
				for key in allDeploy:
					if type(key) is float:
						file = allDeploy[key]
						try:
							src = fileSubFolder + str(file)
							dest = str(file)
							zipFP.getinfo(src).filename = dest
							result = zipFP.extract(src, path = reactor)
							print("\t[Install]", result)
						except Exception as error:
							print("\t[Install Error]", error)
							return None
				deployLinux = GetValue("Linux", allDeploy, {})
				deployMac = GetValue("Mac", allDeploy, {})
				deployWindows = GetValue("Windows", allDeploy, {})
	
				if hostOS == "Linux":
					print("\n[Deploy][Linux]")
					for key in deployLinux:
						file = deployLinux[key]
						try:
							src = fileSubFolder + "Linux/" + str(file)
							dest = str(file)
							zipFP.getinfo(src).filename = dest
							result = zipFP.extract(src, path = reactor)
							print("\t[Install]", result, "\t\t[Src]", src)
						except Exception as error:
							print("\t[Install Error]", error)
							return None
				if hostOS == "Darwin":
					print("\n[Deploy][Mac]")
					for key in deployMac:
						file = deployMac[key]
						try:
							src = fileSubFolder + "Mac/" + str(file)
							dest = str(file)
							zipFP.getinfo(src).filename = dest
							result = zipFP.extract(src, path = reactor)
							print("\t[Install]", result, "\t\t[Src]", src)
						except Exception as error:
							print("\t[Install Error]", error)
							return None
				if hostOS == "Windows":
					print("\n[Deploy][Windows]")
					for key in deployWindows:
						file = deployWindows[key]
						try:
							src = fileSubFolder + "Windows/" + str(file)
							dest = str(file)
							zipFP.getinfo(src).filename = dest
							result = zipFP.extract(src, path = reactor)
							print("\t[Install]", result, "\t\t[Src]", src)
						except Exception as error:
							print("\t[Install Error]", error)
							return None
				zipFP.close()
	return 1

def AtomzExpand(file):
	if app:
		app.DoAction("Console_Show", {"show" : True})
	print("-------------------------------------------------------------------------------------------------------")
	if (file is not None) and (file != ""):
		# Create the Reactor Deploy folder
		reactor = app.MapPath("Reactor:/Deploy/")
		if not os.path.exists(reactor):
			try:
				print("\t[Atomz][Make Reactor Directory]", reactor)
				os.makedirs(reactor)
			except OSError as error:
				print("\t[Atomz][Make Reactor Directory Error]", reactor)
		else:
			print("\t[Atomz][Reactor Directory]", reactor)

		if file.endswith(".zip") and not file.startswith("."):
			if not os.path.exists(file):
				print("[Atomz][Source File Missing]", file)
			else:
				if NativeAtomz(reactor, file) != 1:
					if ReactorStandaloneSourcedAtomz(reactor, file) != 1:
						GitLabSourcedAtomz(reactor, file)

if __name__ == "__main__":
	atomzFile = AtomzWindow()
	if atomzFile.endswith(".lst") and not atomzFile.startswith("."):
		print("[Atomz List]")
		print("-------------------------------------------------------------------------------------------------------")
		# Process the drag and dropped items
		print("\t[List] " + str(atomzFile))
		atomList = ImportText(atomzFile)
		for atmFile in atomList:
			print("\t[Zip] " + str(atmFile))
			if atmFile.endswith(".zip") and not atmFile.startswith("."):
				AtomzExpand(app.MapPath(atmFile))
	elif atomzFile.endswith(".zip") and not atomzFile.startswith("."):
		AtomzExpand(app.MapPath(atomzFile))

	print("[Done]")

