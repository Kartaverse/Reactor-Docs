# PSDRexa
___

## Author
nuroku

## Version
1.1

## Category
Tools/IO

___

## Description
<p>Use Adobe PSD picture materials in DaVinciResolve in a nice way</p>
<h1>Features</h1>
<ul>
<li>PSD image loading and selection</li>
<li>Output as image and deploy to timeline</li>
<li>Output as a Fusion that allows lip-syncing and deploy it on the timeline</li>
</ul>
<h1>Required operating environment</h1>
<ul>
<li>DaVinci Resolve 18.5 or higher</li>
<li>Python 3.6 or higher
Please install Python so that it can be used on DaVinciResolve.
</ul>
<h1>Compatible OS</h1>
<ul>
<li>Windows</li>
<li>Mac
If it doesn't work well on a Mac, there may be something wrong with your security permissions. Or a bug
Also, it seems that there are cases where it does not work properly when using the Mac App version.</li>
</ul>
<h1>Installation steps</h1>
<p>If the installation is successful, PSDRexa and PSDRexa_syncer can be selected from Workspace → Scripts.</p>
<hr />
<h3>Setting description</h3>
<ul>
<li>Image output destination: Local output destination for PSD images</li>
<li>Output image with original file size: If ON, a standing picture with the same size as the loaded PSD will be output. If OFF, the image will be output at the size specified by Height and Width while maintaining the aspect ratio.</li>
<li>Preview at base file size: Size of the portrait image used for previewing this tool</li>
<li>Use psdtoolkit function: If ON, loads PSD in response to radio button or !. If OFF, load all with checkbox</li>
</ul>
<h3>Explanation of output eye clap and lip sync settings</h3>
<ul>
<li>Image output destination: Local output destination for PSD images</li>
<li>Output as a FusionTemplate that allows eye-blinking and lip-syncing: When turned on, it is output as a Fusion template that allows eye-blinking and lip-syncing.</li>
<li>Miscellaneous: Settings such as eye-click and lip-sync</li>
</ul>
<h3>Instructions for eye-clash and lip-syncing</h3>
<p>You can create eye plashes by following steps 1 to 4. If you want to lip sync, please follow steps from 5 onwards.</p>
<ol>
<li>
<p>Open the eye-blink and lip-sync settings and set it to "Output as a Fusion Template that can perform eye-blink and lip-sync"</p>
</li>
<li>
<p>Select a group for eye/lip synchronization or a closed group/layer. As for the behavior</p>
<ul>
<li>Click where you want to enter and suggestions will appear in the list box on the left.</li>
<li>A number (in the order of layers arranged from top to bottom) is attached to the beginning of the candidate name.</li>
</ul>
</li>
<li>
<p>Click “Output parts for eye and lip synchronization”</p>
<ul>
<li>This process may take some time</li>
</ul>
</li>
<li>
<p>Return to PSDRexa and output the standing picture to create an eye-catching standing picture on DaVinciResolve.</p>
</li>
<li>
<p>Select PSDRexa_syncer from DaVinci Resolve workspace → scripts and run it.</p>
<ul>
<li>video_track : Video track where the portrait you want to lip-sync is placed, 1 for V1, 2 for V2...</li>
<li>audio_track : Audio track where the audio file that is the basis for lip-syncing is placed, 1 for A1, 2 for A2...</li>
<li>audio_folder_path: Local folder where the audio files that are the basis for lip-syncing are located.</li>
<li>Lip sync Sync: Reflects lip sync. When the execution is complete, "Done" will be displayed next to it.</li>
<li>Rebuild eye pachi keyframe: Rebuilds the eye pachi keyframe of the standing picture on the specified video_track</li>
</ul>
</li>
</ol>
<hr />
<h1>License</h1>
<p>This project is licensed under the GNU General Public License v3.0 (GPL-3.0) license.</p>


___

## Dependencies

## Deploy

### Common (No Architecture)

> Docs/PSDRexa/README.md  
> Modules/PSDRexa/Common/Logger.py  
> Modules/PSDRexa/DataStore/CharacterFusionDataStore.py  
> Modules/PSDRexa/DataStore/CompositedImageDataStore.py  
> Modules/PSDRexa/DataStore/PartsDataStore.py  
> Modules/PSDRexa/DataStore/PsdDataStore.py  
> Modules/PSDRexa/DataStore/ResolveBinDatastore.py  
> Modules/PSDRexa/DataStore/__init__.py  
> Modules/PSDRexa/Domain/BaseLayerProperties.py  
> Modules/PSDRexa/Domain/DTO/CharacterPartsSet.py  
> Modules/PSDRexa/Domain/DTO/CheckVisibleOperation.py  
> Modules/PSDRexa/Domain/DTO/CompositedImage.py  
> Modules/PSDRexa/Domain/DTO/PSDRexaFusion.py  
> Modules/PSDRexa/Domain/DTO/__init__.py  
> Modules/PSDRexa/Domain/GroupLayer/GroupLayer.py  
> Modules/PSDRexa/Domain/GroupLayer/OneSelectGroupLayer.py  
> Modules/PSDRexa/Domain/GroupLayer/VisibleGroupLayer.py  
> Modules/PSDRexa/Domain/GroupLayer/__init__.py  
> Modules/PSDRexa/Domain/Image/FlipLayerImage.py  
> Modules/PSDRexa/Domain/Image/LayerImage.py  
> Modules/PSDRexa/Domain/Image/__init__.py  
> Modules/PSDRexa/Domain/ImageLayer/ImageLayer.py  
> Modules/PSDRexa/Domain/ImageLayer/OneSelectImageLayer.py  
> Modules/PSDRexa/Domain/ImageLayer/__init__.py  
> Modules/PSDRexa/Domain/Layer.py  
> Modules/PSDRexa/Domain/Psd/Psd.py  
> Modules/PSDRexa/Domain/Psd/PsdMeta.py  
> Modules/PSDRexa/Domain/Psd/PsdTop.py  
> Modules/PSDRexa/Domain/Psd/__init__.py  
> Modules/PSDRexa/Domain/__init__.py  
> Modules/PSDRexa/Exception/DataStoreError.py  
> Modules/PSDRexa/Exception/DomainError.py  
> Modules/PSDRexa/Exception/RepositoryError.py  
> Modules/PSDRexa/Exception/ServiceError.py  
> Modules/PSDRexa/Exception/__init__.py  
> Modules/PSDRexa/PSDRexaSyncer/BaseSyncer.py  
> Modules/PSDRexa/PSDRexaSyncer/SyncTask.py  
> Modules/PSDRexa/PSDRexaSyncer/Syncer1.py  
> Modules/PSDRexa/PSDRexaSyncer/Syncer2.py  
> Modules/PSDRexa/PSDRexaSyncer/__init__.py  
> Modules/PSDRexa/PSDRexaSyncer/main_ui.py  
> Modules/PSDRexa/Persenter/CheckVisibleOperationPresenter.py  
> Modules/PSDRexa/Persenter/CombineLayerPresenter.py  
> Modules/PSDRexa/Persenter/InitPartsPersenter.py  
> Modules/PSDRexa/Persenter/LayerListPersenter.py  
> Modules/PSDRexa/Persenter/OutputCharacterPresenter.py  
> Modules/PSDRexa/Persenter/SaveCompositedImagePersenter.py  
> Modules/PSDRexa/Persenter/__init__.py  
> Modules/PSDRexa/Repository/CompositedImageRepository.py  
> Modules/PSDRexa/Repository/CompositedImageResolveRepository.py  
> Modules/PSDRexa/Repository/PSDRexaFusionRepository.py  
> Modules/PSDRexa/Repository/PartsRepository.py  
> Modules/PSDRexa/Repository/PsdRepository.py  
> Modules/PSDRexa/Repository/__init__.py  
> Modules/PSDRexa/Service/OutputSettingFile/OutputSettingFileService.py  
> Modules/PSDRexa/Service/OutputSettingFile/__init__.py  
> Modules/PSDRexa/Service/PSDRexa.drb  
> Modules/PSDRexa/Service/PSDRexaTemplateService.py  
> Modules/PSDRexa/Service/PsdMemorySaverService.py  
> Modules/PSDRexa/Service/ResolveService.py  
> Modules/PSDRexa/Service/SettingFileService.py  
> Modules/PSDRexa/Service/__init__.py  
> Modules/PSDRexa/Service/dummy.png  
> Modules/PSDRexa/Service/settings.json  
> Modules/PSDRexa/UI/CompositedImageCanvas.py  
> Modules/PSDRexa/UI/OutputSettingUI.py  
> Modules/PSDRexa/UI/Resources/Radio_off.png  
> Modules/PSDRexa/UI/Resources/Radio_off_orig.png  
> Modules/PSDRexa/UI/Resources/Radio_on.png  
> Modules/PSDRexa/UI/Resources/Radio_on_orig.png  
> Modules/PSDRexa/UI/Resources/ico_orig.gif  
> Modules/PSDRexa/UI/Resources/ico_orig.ico  
> Modules/PSDRexa/UI/SettingWindow.py  
> Modules/PSDRexa/UI/__init__.py  
> Modules/PSDRexa/UI/layerTreeView.py  
> Modules/PSDRexa/UI/main_ui.py  
> Modules/PSDRexa/Usecase/BuildLayerList.py  
> Modules/PSDRexa/Usecase/CheckVisibleLayer.py  
> Modules/PSDRexa/Usecase/CombineLayer.py  
> Modules/PSDRexa/Usecase/InitParts.py  
> Modules/PSDRexa/Usecase/OutputCharacterFusion.py  
> Modules/PSDRexa/Usecase/OutputCompositedImage.py  
> Modules/PSDRexa/Usecase/SaveCompositedImage.py  
> Modules/PSDRexa/Usecase/__init__.py  
> Modules/PSDRexa/__init__.py  
> Modules/PSDRexa/requirements.txt  
> Scripts/Utility/PSDRexa.py  
> Scripts/Utility/PSDRexa_syncer.py  
