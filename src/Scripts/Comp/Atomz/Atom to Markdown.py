# Reactor Git Repo Location
repoPath = "$HOME/Documents/Git/Reactor/"

"""
Atom to Markdown.py - v2.0 2025-04-20 05.50 AM
By Andrew Hazelden <andrew@andrewhazelden.com>

Overview
---------
The "Atom to Markdown" Fusion comp script generates markdown (.md) documentation from Reactor Package Manager "atom" package descriptions. This allows Docisfy to publish a Reactor docs website.

Requirements
------------
- Python v3.6 to v3.11 64-bit

Script Usage
------------
Step 1. Open the "Script > Atomz > Atom to Markdown" menu item. The Console window displays the atoms package conversion process.

Todo
-----
- List if there is an InstallScript/UninstallScript
- Possibly use the Reactor package manager CSS theme for the atom description html content formatting?
- Parse description content for a file:// based "Reactor:" URL path.
- Update the "Atomz Expand.py" script to handle GitLab repo directly package zipped files
"""

import os, shutil, datetime, math, re, csv, platform

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

def MarkdownCreate(folder):
	if app:
		app.DoAction("Console_Show", {"show" : True})

	print("-------------------------------------")
	print("[Atom to Markdown]")
	print("-------------------------------------")
	repo = os.path.expandvars(app.MapPath(folder))
	if not os.path.exists(repo):
		print("[Atom][Source Folder Missing]", repo)
	else:
		atomsPath = os.path.join(repo, "Atoms")
		mdPath = os.path.join(repo, "Markdown")

		print("[Atom][Source Folder]", atomsPath)
		print("[Markdown][Dest Folder]", mdPath)
		print("-------------------------------------")

		# Create the output folder
		if not os.path.exists(mdPath):
			try:
				print("\t[Markdown][Make Directory]", mdPath)
				os.makedirs(mdPath)
			except OSError as error:
				print("\t[Markdown][Make Directory Error]", mdPath)

		# Docisfy sidebar file
		mdSidebar = os.path.join(mdPath, "_sidebar.md")

		# Create the sidebar file
		with open(mdSidebar, "w", encoding="utf-8") as fBar:
			fBar.write("""<!-- docs/_sidebar.md -->
- [Home](/)
- [Reactor](reactor)
	- [Reactor SPEED BOOST](reactor-speed-boost)
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

			def GetAtomNameFromMD(atomsPath, mdFilename):
				if mdFilename.endswith(".md"):
					atomFilename = mdFilename.replace(".md", ".atom")
					dirName = mdFilename.replace(".md", "")
					atomFilepath = os.path.join(atomsPath, dirName, atomFilename)
					atomDict = bmd.readfile(atomFilepath)
					if atomDict is None:
						print("[Atom][Get Atom Name][Atom Parsing Error]")
						return ""
					else:
						name = GetValue("Name", atomDict, "")
						return name
				else:
					return mdFilename

			def SortMenus(file):
				if file.endswith(".md"):
					return 0
				else:
					return 1

			def BuildCategories(mdPath, atomsPath):
				category = []
				# Generate the atom menu list
				for dirName in sorted(os.listdir(atomsPath)):
					# Ignore hidden files starting with a periopd
					if not dirName.startswith("."):
						# Build the filenames
						# Atom file
						atomFilepath = os.path.join(atomsPath, dirName, dirName + ".atom")
	
						# Markdown file
						mdFilepath = os.path.join(mdPath, dirName + ".md")
						mdFileName = dirName + ".md"
						mdAtomName = dirName
	
						atomDict = bmd.readfile(atomFilepath)
						if atomDict is None:
							print("[Atom][Build Categories][Atom Parsing Error]")
						else:
							name = GetValue("Name", atomDict, "")
							cat = GetValue("Category", atomDict, "")
							catItem = (cat + "/" + mdFileName)
							category.append(catItem)
				return category

			menus = {}
			category = {}

			# Add the menu items
			category = BuildCategories(mdPath, atomsPath)
			menus = BuildMenu(category)
			# print(category)
			# print(menus)
			for i in sorted(menus.keys(), key=lambda item: (SortMenus(item), GetAtomNameFromMD(atomsPath, item).lower())):
				print("- [" + i + "](/ ':disabled')")
				fBar.write("- [" + i + "](/ ':disabled')\n")
				for j in sorted(menus[i].keys(), key=lambda item: (SortMenus(item), GetAtomNameFromMD(atomsPath, item).lower())):
					if j.endswith(".md"):
						cleanName = GetAtomNameFromMD(atomsPath, j)
						print("  - [" + cleanName + "](" + j + ")")
						fBar.write("  - [" + cleanName + "](" + j + ")\n")
					else:
						print("  - [" + j + "](/ ':disabled')")
						fBar.write("  - [" + j + "](/ ':disabled')\n")
						for k in sorted(menus[i][j].keys(), key=lambda item: (SortMenus(item), GetAtomNameFromMD(atomsPath, item).lower())):
							if k.endswith(".md"):
								cleanName = GetAtomNameFromMD(atomsPath, k)
								print("    - [" + cleanName + "](" + k + ")")
								fBar.write("    - [" + cleanName + "](" + k + ")\n")
							else:
								print("    - [" + k + "](/ ':disabled')")
								fBar.write("    - [" + k + "](/ ':disabled')\n")
								for l in sorted(menus[i][j][k].keys(), key=lambda item: (SortMenus(item), GetAtomNameFromMD(atomsPath, item).lower())):
									if l.endswith(".md"):
										cleanName = GetAtomNameFromMD(atomsPath, l)
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

					# Markdown file
					mdFilepath = os.path.join(mdPath, dirName + ".md")
					mdFileName = dirName + ".md"
					mdAtomName = dirName

					atomDict = bmd.readfile(atomFilepath)
					if atomDict is None:
						print("[Atom][Atom Parsing Error]")
					else:
						name = GetValue("Name", atomDict, "")
						cat = GetValue("Category", atomDict, "")

						# Sidebar atom entry
						#fBar.write("  - [" + name + "](" + mdFileName + ")\n")

			# Sidebar atom entry
			fBar.write("""- **Links**
  - [WSL Forum](https://www.steakunderwater.com/wesuckless/viewtopic.php?t=3067)
  - [Reactor Atoms Repo](https://gitlab.com/WeSuckLess/Reactor)
  - [Reactor Docs Repo](https://github.com/Kartaverse/Reactor-Docs)
""")

			# Generate the atom package list
			for dirName in sorted(os.listdir(atomsPath)):
				# Ignore hidden files starting with a periopd
				if not dirName.startswith("."):
					startTimer = datetime.datetime.now()

					# Build the filenames
					# Atom file
					atomFilepath = os.path.join(atomsPath, dirName, dirName + ".atom")

					# Markdown file
					mdFilepath = os.path.join(mdPath, dirName + ".md")
					mdFileName = dirName + ".md"
					mdAtomName = dirName

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

						# Create the atom markdown file
						with open(mdFilepath, "w", encoding="utf-8") as fAtom:
							fAtom.write("# " + str(name) + "\n")
							fAtom.write("___\n\n")

							fAtom.write("## Category\n")
							fAtom.write(str(cat) + "\n\n")

							fAtom.write("## Author\n")
							fAtom.write(author + "\n\n")

							fAtom.write("## Version\n")
							fAtom.write(str(version) + "\n\n")

							fAtom.write("___\n\n")

							fAtom.write("## Description\n")
							#fAtom.write(str(html))
							fAtom.write(str(htmlClean))

							#print("[Atomz][Info]", name, "v" + str(version), "by", author)
							#print("[Atom][Dict Contents]")
							#print(atomDict)

							fAtom.write("\n\n___\n\n")

							if "Donation" in atomDict:
								donate = GetValue("Donation", atomDict, {})
								if donate:
									fAtom.write("## Donation\n")
									try:
										if "Amount" in donate:
											fAtom.write("The author of the atom has suggested a donation of \"" + donate["Amount"] + "\".  \n")
										if "URL" in donate:
											fAtom.write("You can donate using the URL: <a href=\"" + donate["URL"] + "\">" + donate["URL"]  + "</a>\n")
									except Exception as error:
										print("\t[Error]", error)
									fAtom.write("\n")

							fAtom.write("## Download\n\n")
							fAtom.write("Download a zipped atom package for offline installation:\n")
							fAtom.write("> [" + str(dirName + ".zip") + "](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/" + dirName + ")  \n\n")

							fAtom.write("## Dependencies\n\n")
							#print("\n[Deploy][All]")
							allDependencies = GetValue("Dependencies", atomDict, {})
							for key in allDependencies:
								if type(key) is float:
									file = allDependencies[key]
									try:
										#print("\t[Install]", file)
										fAtom.write("> [" + str(file) + "](" + file + ".md)  \n")
									except Exception as error:
										print("\t[Error]", error)

							# Reactor
							# Check the active operating system (Darwin, Windows, Linux)
							hostOS = platform.system()

							fAtom.write("## Deploy\n\n")

							#print("\n[Deploy][All]")
							allDeploy = GetValue("Deploy", atomDict, {})
							if allDeploy:
								fAtom.write("### Common (No Architecture)\n\n")
								fAtom.write("<ul>\n")
								
								for key in allDeploy:
									if type(key) is float:
										file = allDeploy[key]
										try:
											#print("\t[Install]", file)
											fAtom.write("<li><a href=\"https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/" + dirName + "/" + file + "?ref_type=heads\">" + str(file) + "</a></li>\n")
										except Exception as error:
											print("\t[Error]", error)
								fAtom.write("</ul>\n")

							deployLinux = GetValue("Linux", allDeploy, {})
							deployMac = GetValue("Mac", allDeploy, {})
							deployWindows = GetValue("Windows", allDeploy, {})

							if deployLinux:
								fAtom.write("\n### Linux\n\n")
								#print("\n[Deploy][Linux]")
								for key in deployLinux:
									file = deployLinux[key]
									try:
										#print("\t[Install]", file)
										fAtom.write("<li><a href=\"https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/" + dirName + "/Linux/" + file + "?ref_type=heads\">" + str(file) + "</a></li>\n")
									except Exception as error:
										print("\t[Install Error]", error)

							if deployMac:
								fAtom.write("\n### macOS\n\n")
								#print("\n[Deploy][Mac]")
								for key in deployMac:
									file = deployMac[key]
									try:
										#print("\t[Install]", file)
										fAtom.write("<li><a href=\"https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/" + dirName + "/Mac/" + file + "?ref_type=heads\">" + str(file) + "</a></li>\n")
									except Exception as error:
										print("\t[Install Error]", error)

							if deployWindows:
								fAtom.write("\n### Windows\n\n")
								#print("\n[Deploy][Windows]")
								for key in deployWindows:
									file = deployWindows[key]
									try:
										#print("\t[Install]", file)
										fAtom.write("<li><a href=\"https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/" + dirName + "/Windows/" + file + "?ref_type=heads\">" + str(file) + "</a></li>\n")
									except Exception as error:
										print("\t[Install Error]", error)

					endTimer = datetime.datetime.now()
					elapsedTime = (endTimer - startTimer).total_seconds()
					mins, secs = divmod(elapsedTime, 60)
					timeFormatted = "(" + str(math.ceil(mins)).zfill(2) + " Minutes " + str(math.ceil(secs)).zfill(2) + " Seconds)"
					#print(atomFilepath, "->", mdFilepath, timeFormatted)
					print(mdFileName, timeFormatted)
	print("-------------------------------------")

if __name__ == "__main__":
	repoPath = RepoWindow()
	MarkdownCreate(repoPath)
	print("[Done]")
	