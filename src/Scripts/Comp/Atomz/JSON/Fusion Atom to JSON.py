# Reactor Git Repo Location
repoPath = "$HOME/Documents/Git/Reactor/"

# Zip Package Download URL
ZipFile = "https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/"

"""
Fusion Atom to JSON.py - v4.0 2025-10-29 02.59 PM
By Andrew Hazelden <andrew@andrewhazelden.com>

Overview
---------
The "Fusion Atom to JSON" Fusion comp script generates (.json) documents from Reactor Package Manager "atom" package descriptions. This allows external tools to work with atoms.

Requirements
------------
- Python v3.6 to v3.11 64-bit

Script Usage
------------
Step 1. Open the "Script > Atomz > Fusion Atom to JSON" menu item. The Console window displays the atoms package conversion process.

Todo
-----
- List if there is an InstallScript/UninstallScript
- Possibly use the Reactor package manager CSS theme for the atom description html content formatting?
- Parse description content for a file:// based "Reactor:" URL path.

"""

import os, shutil, datetime, math, re, csv, platform, json

def GetValue(key, dct, default):
	if key in dct:
		return dct[key]
	else:
		return default

def RepoWindow():
	ui = fu.UIManager
	repo_disp = bmd.UIDispatcher(ui)


	repo_dlg = repo_disp.AddWindow({"WindowTitle": "GitLab Repo", "ID": "RepoWin", "TargetID" : "RepoWin", "Geometry": [0, 85, 430, 135], "Spacing": 0,},[
		ui.VGroup({"ID": "root", "Weight": 10.0,},[
			ui.VGroup({
				"Weight": 0.1,
				#"StyleSheet": "background-color: rgb(37, 37, 37);",
			},[
				ui.HGroup({},[
					ui.Label({
						"ID": "ViewLabel",
						"Text": "  GitLab Reactor Repo",
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
				ui.Label({"ID": "RepoLabel", "Text": "Git Repo:", "Weight": 0.1}),
				ui.LineEdit({"ID": "RepoTxt", "Text": repoPath, "PlaceholderText": "Please enter a GitLab Reactor repo folder name", "Weight": 0.9}),
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

	repo_itm = repo_dlg.GetItems()

	# The window was closed
	def RepoWinFunc(ev):
		repo_disp.ExitLoop()
	repo_dlg.On.RepoWin.Close = RepoWinFunc

	# Add your GUI element based event functions here:

	def OKButtonFunc(ev):
		repo_disp.ExitLoop()
	repo_dlg.On.OKButton.Clicked = OKButtonFunc

	def CancelButtonFunc(ev):
		repo_itm["RepoTxt"].Text = ""
		repo_disp.ExitLoop()
	repo_dlg.On.CancelButton.Clicked = CancelButtonFunc

	def BrowseButtonFunc(ev):
		selectedPath = fu.RequestDir()
		if selectedPath:
			repo_itm["RepoTxt"].Text = str(selectedPath)
	repo_dlg.On.BrowseButton.Clicked = BrowseButtonFunc

	repo_dlg.Show()
	repo_disp.RunLoop()
	repo_dlg.Hide()

	# When the window is closed send back the repo name
	return str(repo_itm["RepoTxt"].Text)

def JSONCreate(folder):
	if app:
		app.DoAction("Console_Show", {"show" : True})

	print("-------------------------------------")
	print("[Atom to JSON]")
	print("-------------------------------------")
	repo = os.path.expandvars(app.MapPath(folder))
	if not os.path.exists(repo):
		print("[Atom][Source Folder Missing]", repo)
	else:
		atomsPath = os.path.join(repo, "Atoms")
		jsonPath = os.path.join(repo, "JSON")

		print("[Atom][Source Folder]", atomsPath)
		print("[JSON][Dest Folder]", jsonPath)
		print("-------------------------------------")

		# Create the output folder
		if not os.path.exists(jsonPath):
			try:
				print("\t[JSON][Make Directory]", jsonPath)
				os.makedirs(jsonPath)
			except OSError as error:
				print("\t[JSON][Make Directory Error]", jsonPath)

		atomJumboDict = {}
		atomJumboIndex = 0
		jsonJumboFilepath = os.path.join(jsonPath, "Reactor.json")
		startTimer = datetime.datetime.now()

		# Generate the atom package list
		for dirName in sorted(os.listdir(atomsPath)):
			# Ignore hidden files starting with a periopd
			if not dirName.startswith("."):
				# Build the filenames
				# Atom file
				atomFilepath = os.path.join(atomsPath, dirName, dirName + ".atom")

				# JSON file
				#jsonFilepath = os.path.join(jsonPath, dirName + ".json")
				#jsonFilename = dirName + ".json"
				jsonAtomName = dirName

				atomDict = bmd.readfile(atomFilepath)
				if atomDict is None:
					print("[Atom][Atom Parsing Error]", jsonAtomName)
				else:
					name = GetValue("Name", atomDict, "")
					cat = GetValue("Category", atomDict, "")
					version = GetValue("Version", atomDict, 0.0)
					date = GetValue("Date", atomDict,"")
					author = GetValue("Author", atomDict, "")
					html = GetValue("Description", atomDict, "")
					htmlClean = "\n".join([line.strip() for line in html.splitlines()])

					# Escape accent
					#author = author.replace(u"\u00e9", "é")
					#atomDict.update({"Author": author})
					#print(author)

					# Add the GitLab Reactor repo zipped package URL
					atomDict.update({"Zipfile":  str(ZipFile) + str(dirName)})

					# Add an ID entry
					atomDict.update({"ID": dirName})

					# Write the individual atom json files
					# with open(jsonFilepath, "w", encoding="utf-8") as fAtom:
					#	json.dump(atomDict, fAtom, indent = 4)

					# Append the dict to the composite json file
					atomJumboIndex += 1
					atomJumboDict.update({str(atomJumboIndex): atomDict})

		# Write the composite json file
		with open(jsonJumboFilepath, "w", encoding="utf-8") as fAtom:
			json.dump(atomJumboDict, fAtom, indent = 4)

		endTimer = datetime.datetime.now()
		elapsedTime = (endTimer - startTimer).total_seconds()
		mins, secs = divmod(elapsedTime, 60)
		timeFormatted = "(" + str(math.ceil(mins)).zfill(2) + " Minutes " + str(math.ceil(secs)).zfill(2) + " Seconds)"
		print("\nWrite JSON file:")
		print(jsonJumboFilepath, timeFormatted)
	print("-------------------------------------")

if __name__ == "__main__":
	repoPath = RepoWindow()
	JSONCreate(repoPath)
	print("[Done]")
	
