"""
AtomzCreate - v4.0 2025-10-14
By Andrew Hazelden <andrew@andrewhazelden.com

Convert a GitLab Reactor repository folder into individually zipped atomz packaged archives. The zipped packages are easier to use and manage with a NAS-based offline Reactor Package installation approach.

Script Usage:
1. Clone the either the Reactor or Vonk Ultra repo using the terminal:

mkdir -p $HOME/Documents/Git/
cd $HOME/Documents/Git/

git clone https://gitlab.com/WeSuckLess/Reactor.git
git clone https://gitlab.com/AndrewHazelden/Vonk

2. Run the Python script.

3. Move the zipped atom packages onto a shared NAS volume for use in an airgapped network based studio environment.

Example Terminal Output:
[Atomz Create]
[Atomz][Source Folder] /Users/vfx/Documents/Git/Reactor/Atoms
[Atomz][Dest Folder] /Users/vfx/Documents/Git/Reactor/Atomz
/Users/vfx/Documents/Git/Reactor/Atomz/com.AlbertoGZ.ColorLabels.zip (00 Minutes 01 Seconds)
/Users/vfx/Documents/Git/Reactor/Atomz/com.AlbertoGZ.ReloadLoaders.zip (00 Minutes 01 Seconds)
/Users/vfx/Documents/Git/Reactor/Atomz/com.AlexBogomolov.AttributeSpreadsheet.zip (00 Minutes 01 Seconds)
/Users/vfx/Documents/Git/Reactor/Atomz/com.AlexBogomolov.Bookmarker.zip (00 Minutes 01 Seconds)
/Users/vfx/Documents/Git/Reactor/Atomz/com.AlexBogomolov.FrameRanger.zip (00 Minutes 01 Seconds)
...


"""

import os, shutil, datetime, math

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
				ui.LineEdit({"ID": "RepoTxt", "Text": "$HOME/Documents/Git/Reactor/", "PlaceholderText": "Please enter a GitLab Reactor repo folder name", "Weight": 0.9}),
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

def AtomzCreate(folder):
	if app:
		app.DoAction("Console_Show", {"show" : True})

	print("[Atomz Create]")
	repo = os.path.expandvars(app.MapPath(folder))
	if not os.path.exists(repo):
		print("[Atomz][Source Folder Missing]", repo)
	else:
		atomsPath = os.path.join(repo, "Atoms")
		zipPath = os.path.join(repo, "Atomz")
	
		print("[Atomz][Source Folder]", atomsPath)
		print("[Atomz][Dest Folder]", zipPath)

		# Create the output folder
		if not os.path.exists(zipPath):
			try:
				print("\t[Atomz][Make Directory]", zipPath)
				os.makedirs(zipPath)
			except OSError as error:
				print("\t[Atomz][Make Directory Error]", zipPath)

		# Generate the atom package list
		for dirName in sorted(os.listdir(atomsPath)):
			# Ignore hidden files starting with a periopd
			if not dirName.startswith("."):
				startTimer = datetime.datetime.now()

				# Build the filename
				zipBasename = os.path.join(zipPath, dirName)
				fmt = "zip"
				srcPath = os.path.join(atomsPath, dirName)

				# Zip the sub-folder
				result = shutil.make_archive(zipBasename, fmt, root_dir = srcPath, base_dir = ".")

				endTimer = datetime.datetime.now()
				elapsedTime = (endTimer - startTimer).total_seconds()
				mins, secs = divmod(elapsedTime, 60)
				timeFormatted = "(" + str(math.ceil(mins)).zfill(2) + " Minutes " + str(math.ceil(secs)).zfill(2) + " Seconds)"
				print(result, timeFormatted)

if __name__ == "__main__":
	repoPath = RepoWindow()
	AtomzCreate(repoPath)
	print("[Done]")
	
