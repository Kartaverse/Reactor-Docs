# PSDRexa
___

## Category
Tools/IO

## Author
nuroku

## Version
1.1

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

## Donation
The author of the atom has suggested a donation of "$5.00 USD".  
You can donate using the URL: <a href="http://www.paypal.me/nuroku2000" class="button">http://www.paypal.me/nuroku2000</a>
## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Docs/PSDRexa/README.md?ref_type=heads">Docs/PSDRexa/README.md</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Common/Logger.py?ref_type=heads">Modules/PSDRexa/Common/Logger.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/DataStore/CharacterFusionDataStore.py?ref_type=heads">Modules/PSDRexa/DataStore/CharacterFusionDataStore.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/DataStore/CompositedImageDataStore.py?ref_type=heads">Modules/PSDRexa/DataStore/CompositedImageDataStore.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/DataStore/PartsDataStore.py?ref_type=heads">Modules/PSDRexa/DataStore/PartsDataStore.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/DataStore/PsdDataStore.py?ref_type=heads">Modules/PSDRexa/DataStore/PsdDataStore.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/DataStore/ResolveBinDatastore.py?ref_type=heads">Modules/PSDRexa/DataStore/ResolveBinDatastore.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/DataStore/__init__.py?ref_type=heads">Modules/PSDRexa/DataStore/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/BaseLayerProperties.py?ref_type=heads">Modules/PSDRexa/Domain/BaseLayerProperties.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/DTO/CharacterPartsSet.py?ref_type=heads">Modules/PSDRexa/Domain/DTO/CharacterPartsSet.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/DTO/CheckVisibleOperation.py?ref_type=heads">Modules/PSDRexa/Domain/DTO/CheckVisibleOperation.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/DTO/CompositedImage.py?ref_type=heads">Modules/PSDRexa/Domain/DTO/CompositedImage.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/DTO/PSDRexaFusion.py?ref_type=heads">Modules/PSDRexa/Domain/DTO/PSDRexaFusion.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/DTO/__init__.py?ref_type=heads">Modules/PSDRexa/Domain/DTO/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/GroupLayer/GroupLayer.py?ref_type=heads">Modules/PSDRexa/Domain/GroupLayer/GroupLayer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/GroupLayer/OneSelectGroupLayer.py?ref_type=heads">Modules/PSDRexa/Domain/GroupLayer/OneSelectGroupLayer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/GroupLayer/VisibleGroupLayer.py?ref_type=heads">Modules/PSDRexa/Domain/GroupLayer/VisibleGroupLayer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/GroupLayer/__init__.py?ref_type=heads">Modules/PSDRexa/Domain/GroupLayer/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/Image/FlipLayerImage.py?ref_type=heads">Modules/PSDRexa/Domain/Image/FlipLayerImage.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/Image/LayerImage.py?ref_type=heads">Modules/PSDRexa/Domain/Image/LayerImage.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/Image/__init__.py?ref_type=heads">Modules/PSDRexa/Domain/Image/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/ImageLayer/ImageLayer.py?ref_type=heads">Modules/PSDRexa/Domain/ImageLayer/ImageLayer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/ImageLayer/OneSelectImageLayer.py?ref_type=heads">Modules/PSDRexa/Domain/ImageLayer/OneSelectImageLayer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/ImageLayer/__init__.py?ref_type=heads">Modules/PSDRexa/Domain/ImageLayer/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/Layer.py?ref_type=heads">Modules/PSDRexa/Domain/Layer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/Psd/Psd.py?ref_type=heads">Modules/PSDRexa/Domain/Psd/Psd.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/Psd/PsdMeta.py?ref_type=heads">Modules/PSDRexa/Domain/Psd/PsdMeta.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/Psd/PsdTop.py?ref_type=heads">Modules/PSDRexa/Domain/Psd/PsdTop.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/Psd/__init__.py?ref_type=heads">Modules/PSDRexa/Domain/Psd/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Domain/__init__.py?ref_type=heads">Modules/PSDRexa/Domain/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Exception/DataStoreError.py?ref_type=heads">Modules/PSDRexa/Exception/DataStoreError.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Exception/DomainError.py?ref_type=heads">Modules/PSDRexa/Exception/DomainError.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Exception/RepositoryError.py?ref_type=heads">Modules/PSDRexa/Exception/RepositoryError.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Exception/ServiceError.py?ref_type=heads">Modules/PSDRexa/Exception/ServiceError.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Exception/__init__.py?ref_type=heads">Modules/PSDRexa/Exception/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/PSDRexaSyncer/BaseSyncer.py?ref_type=heads">Modules/PSDRexa/PSDRexaSyncer/BaseSyncer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/PSDRexaSyncer/SyncTask.py?ref_type=heads">Modules/PSDRexa/PSDRexaSyncer/SyncTask.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/PSDRexaSyncer/Syncer1.py?ref_type=heads">Modules/PSDRexa/PSDRexaSyncer/Syncer1.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/PSDRexaSyncer/Syncer2.py?ref_type=heads">Modules/PSDRexa/PSDRexaSyncer/Syncer2.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/PSDRexaSyncer/__init__.py?ref_type=heads">Modules/PSDRexa/PSDRexaSyncer/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/PSDRexaSyncer/main_ui.py?ref_type=heads">Modules/PSDRexa/PSDRexaSyncer/main_ui.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Persenter/CheckVisibleOperationPresenter.py?ref_type=heads">Modules/PSDRexa/Persenter/CheckVisibleOperationPresenter.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Persenter/CombineLayerPresenter.py?ref_type=heads">Modules/PSDRexa/Persenter/CombineLayerPresenter.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Persenter/InitPartsPersenter.py?ref_type=heads">Modules/PSDRexa/Persenter/InitPartsPersenter.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Persenter/LayerListPersenter.py?ref_type=heads">Modules/PSDRexa/Persenter/LayerListPersenter.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Persenter/OutputCharacterPresenter.py?ref_type=heads">Modules/PSDRexa/Persenter/OutputCharacterPresenter.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Persenter/SaveCompositedImagePersenter.py?ref_type=heads">Modules/PSDRexa/Persenter/SaveCompositedImagePersenter.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Persenter/__init__.py?ref_type=heads">Modules/PSDRexa/Persenter/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Repository/CompositedImageRepository.py?ref_type=heads">Modules/PSDRexa/Repository/CompositedImageRepository.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Repository/CompositedImageResolveRepository.py?ref_type=heads">Modules/PSDRexa/Repository/CompositedImageResolveRepository.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Repository/PSDRexaFusionRepository.py?ref_type=heads">Modules/PSDRexa/Repository/PSDRexaFusionRepository.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Repository/PartsRepository.py?ref_type=heads">Modules/PSDRexa/Repository/PartsRepository.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Repository/PsdRepository.py?ref_type=heads">Modules/PSDRexa/Repository/PsdRepository.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Repository/__init__.py?ref_type=heads">Modules/PSDRexa/Repository/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/OutputSettingFile/OutputSettingFileService.py?ref_type=heads">Modules/PSDRexa/Service/OutputSettingFile/OutputSettingFileService.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/OutputSettingFile/__init__.py?ref_type=heads">Modules/PSDRexa/Service/OutputSettingFile/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/PSDRexa.drb?ref_type=heads">Modules/PSDRexa/Service/PSDRexa.drb</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/PSDRexaTemplateService.py?ref_type=heads">Modules/PSDRexa/Service/PSDRexaTemplateService.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/PsdMemorySaverService.py?ref_type=heads">Modules/PSDRexa/Service/PsdMemorySaverService.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/ResolveService.py?ref_type=heads">Modules/PSDRexa/Service/ResolveService.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/SettingFileService.py?ref_type=heads">Modules/PSDRexa/Service/SettingFileService.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/__init__.py?ref_type=heads">Modules/PSDRexa/Service/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/dummy.png?ref_type=heads">Modules/PSDRexa/Service/dummy.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Service/settings.json?ref_type=heads">Modules/PSDRexa/Service/settings.json</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/CompositedImageCanvas.py?ref_type=heads">Modules/PSDRexa/UI/CompositedImageCanvas.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/OutputSettingUI.py?ref_type=heads">Modules/PSDRexa/UI/OutputSettingUI.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/Resources/Radio_off.png?ref_type=heads">Modules/PSDRexa/UI/Resources/Radio_off.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/Resources/Radio_off_orig.png?ref_type=heads">Modules/PSDRexa/UI/Resources/Radio_off_orig.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/Resources/Radio_on.png?ref_type=heads">Modules/PSDRexa/UI/Resources/Radio_on.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/Resources/Radio_on_orig.png?ref_type=heads">Modules/PSDRexa/UI/Resources/Radio_on_orig.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/Resources/ico_orig.gif?ref_type=heads">Modules/PSDRexa/UI/Resources/ico_orig.gif</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/Resources/ico_orig.ico?ref_type=heads">Modules/PSDRexa/UI/Resources/ico_orig.ico</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/SettingWindow.py?ref_type=heads">Modules/PSDRexa/UI/SettingWindow.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/__init__.py?ref_type=heads">Modules/PSDRexa/UI/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/layerTreeView.py?ref_type=heads">Modules/PSDRexa/UI/layerTreeView.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/UI/main_ui.py?ref_type=heads">Modules/PSDRexa/UI/main_ui.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Usecase/BuildLayerList.py?ref_type=heads">Modules/PSDRexa/Usecase/BuildLayerList.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Usecase/CheckVisibleLayer.py?ref_type=heads">Modules/PSDRexa/Usecase/CheckVisibleLayer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Usecase/CombineLayer.py?ref_type=heads">Modules/PSDRexa/Usecase/CombineLayer.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Usecase/InitParts.py?ref_type=heads">Modules/PSDRexa/Usecase/InitParts.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Usecase/OutputCharacterFusion.py?ref_type=heads">Modules/PSDRexa/Usecase/OutputCharacterFusion.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Usecase/OutputCompositedImage.py?ref_type=heads">Modules/PSDRexa/Usecase/OutputCompositedImage.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Usecase/SaveCompositedImage.py?ref_type=heads">Modules/PSDRexa/Usecase/SaveCompositedImage.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/Usecase/__init__.py?ref_type=heads">Modules/PSDRexa/Usecase/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/__init__.py?ref_type=heads">Modules/PSDRexa/__init__.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Modules/PSDRexa/requirements.txt?ref_type=heads">Modules/PSDRexa/requirements.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Scripts/Utility/PSDRexa.py?ref_type=heads">Scripts/Utility/PSDRexa.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.nuroku.PSDRexa/Scripts/Utility/PSDRexa_syncer.py?ref_type=heads">Scripts/Utility/PSDRexa_syncer.py</a></li>
</ul>
