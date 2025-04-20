# Reactor Git Repo Location
repoPath = "$HOME/Documents/Git/Reactor/"

"""
Atom to JSON.py - v2.0 2025-04-20 05.50 AM
By Andrew Hazelden <andrew@andrewhazelden.com>

Overview
---------
The "Atom to JSON" Fusion comp script generates (.json) documents from Reactor Package Manager "atom" package descriptions. This allows external tools to work with atoms.

Requirements
------------
- Python v3.6 to v3.11 64-bit

Script Usage
------------
Step 1. Open the "Script > Atomz > Atom to JSON" menu item. The Console window displays the atoms package conversion process.

Todo
-----
- List if there is an InstallScript/UninstallScript
- Possibly use the Reactor package manager CSS theme for the atom description html content formatting?
- Parse description content for a file:// based "Reactor:" URL path.
- Update the "Atomz Expand.py" script to handle GitLab repo directly package zipped files
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

		# Docisfy sidebar file
		mdSidebar = os.path.join(jsonPath, "_sidebar.md")

		# Create the sidebar file
		with open(mdSidebar, "w", encoding="utf-8") as fBar:
			fBar.write("""<!-- docs/_sidebar.json -->
- [Home](/)
- [Reactor](reactor.json)
- **Atoms**
""")

			# Create the menu structure
			def AddMenuItems(menu, segments):
				if segments:
					# Split the category into segments to build the sidebar hierarchy
					head, *tail = segments
					if head not in menu:
						menu[head] = {}
					AddMenuItems(menu[head], tail)

			def BuildMenu(cat):
				menu = {}
				# Split the category into segments based on the slash separator
				for c in cat:
					segments = c.strip().split("/")
					AddMenuItems(menu, segments)
				return menu

			def GetAtomName(atomsPath, atomFilename):
				if atomFilename.endswith(".atom"):
					dirName = atomFilename.replace(".atom", "")
					atomFilepath = os.path.join(atomsPath, dirName, atomFilename)
					atomDict = bmd.readfile(atomFilepath)
					if atomDict is None:
						print("[Atom][Get Atom Name][Atom Parsing Error]")
						return ""
					else:
						name = GetValue("Name", atomDict, "")
						return name
				else:
					return atomFilename

			def GetAtomNameFromJSON(atomsPath, jsonFilename):
				if jsonFilename.endswith(".json"):
					atomFilename = jsonFilename.replace(".json", ".atom")
					dirName = jsonFilename.replace(".json", "")
					atomFilepath = os.path.join(atomsPath, dirName, atomFilename)
					atomDict = bmd.readfile(atomFilepath)
					if atomDict is None:
						print("[Atom][Get Atom Name][Atom Parsing Error]")
						return ""
					else:
						name = GetValue("Name", atomDict, "")
						return name
				else:
					return jsonFilename

			def SortMenus(file):
				if file.endswith(".json"):
					return 0
				else:
					return 1

			def BuildCategories(jsonPath, atomsPath):
				category = []
				# Generate the atom menu list
				for dirName in sorted(os.listdir(atomsPath)):
					# Ignore hidden files starting with a periopd
					if not dirName.startswith("."):
						# Build the filenames
						# Atom file
						atomFilepath = os.path.join(atomsPath, dirName, dirName + ".atom")
	
						# JSON file
						jsonFilepath = os.path.join(jsonPath, dirName + ".json")
						jsonFilename = dirName + ".json"
						jsonAtomName = dirName
	
						atomDict = bmd.readfile(atomFilepath)
						if atomDict is None:
							print("[Atom][Build Categories][Atom Parsing Error]")
						else:
							name = GetValue("Name", atomDict, "")
							cat = GetValue("Category", atomDict, "")
							catItem = (cat + "/" + jsonFilename)
							category.append(catItem)
				return category

			menus = {}
			category = {}

			# Add the menu items
			category = BuildCategories(jsonPath, atomsPath)
			menus = BuildMenu(category)
			# print(category)
			# print(menus)
			for i in sorted(menus.keys(), key=lambda item: (SortMenus(item), GetAtomNameFromJSON(atomsPath, item).lower())):
				print("- [" + i + "](/ ':disabled')")
				fBar.write("- [" + i + "](/ ':disabled')\n")
				for j in sorted(menus[i].keys(), key=lambda item: (SortMenus(item), GetAtomNameFromJSON(atomsPath, item).lower())):
					if j.endswith(".json"):
						cleanName = GetAtomNameFromJSON(atomsPath, j)
						print("  - [" + cleanName + "](" + j + ")")
						fBar.write("  - [" + cleanName + "](" + j + ")\n")
					else:
						print("  - [" + j + "](/ ':disabled')")
						fBar.write("  - [" + j + "](/ ':disabled')\n")
						for k in sorted(menus[i][j].keys(), key=lambda item: (SortMenus(item), GetAtomNameFromJSON(atomsPath, item).lower())):
							if k.endswith(".json"):
								cleanName = GetAtomNameFromJSON(atomsPath, k)
								print("    - [" + cleanName + "](" + k + ")")
								fBar.write("    - [" + cleanName + "](" + k + ")\n")
							else:
								print("    - [" + k + "](/ ':disabled')")
								fBar.write("    - [" + k + "](/ ':disabled')\n")
								for l in sorted(menus[i][j][k].keys(), key=lambda item: (SortMenus(item), GetAtomNameFromJSON(atomsPath, item).lower())):
									if l.endswith(".json"):
										cleanName = GetAtomNameFromJSON(atomsPath, l)
										print("      - [" + cleanName + "](" + l + ")")
										fBar.write("      - [" + cleanName + "](" + l + ")\n")
									else:
										print("      - [" + l + "](/ ':disabled')")
										fBar.write("      - [" + l + "](/ ':disabled')\n")

			# Generate the atom package list
			for dirName in sorted(os.listdir(atomsPath)):
				# Ignore hidden files starting with a periopd
				if not dirName.startswith("."):
					# Build the filenames
					# Atom file
					atomFilepath = os.path.join(atomsPath, dirName, dirName + ".atom")

					# JSON file
					jsonFilepath = os.path.join(jsonPath, dirName + ".json")
					jsonFilename = dirName + ".json"
					jsonAtomName = dirName

					atomDict = bmd.readfile(atomFilepath)
					if atomDict is None:
						print("[Atom][Atom Parsing Error]")
					else:
						name = GetValue("Name", atomDict, "")
						cat = GetValue("Category", atomDict, "")

						# Sidebar atom entry
						#fBar.write("  - [" + name + "](" + jsonFilename + ")\n")

			# Sidebar atom entry
			fBar.write("""- **Links**
  - [WSL Forum](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3067)
  - [Reactor Atoms Repo](https://gitlab.com/WeSuckLess/Reactor)
  - [Reactor Docs Repo](https://github.com/Kartaverse/Reactor-Docs)
""")

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
						print("[Atom][Atom Parsing Error]")
					else:
						name = GetValue("Name", atomDict, "")
						cat = GetValue("Category", atomDict, "")
						version = GetValue("Version", atomDict, 0.0)
						date = GetValue("Date", atomDict,"")
						author = GetValue("Author", atomDict, "")
						html = GetValue("Description", atomDict, "")
						htmlClean = "\n".join([line.strip() for line in html.splitlines()])

						# Add the GitLab Reactor repo zipped package URL
						atomDict.update({"Zipfile":  "https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/" + str(dirName)})

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
	
