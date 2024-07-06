# InstantNGP
___

## Author
NVIDIA

## Version
1.0

## Category
Bin

___

## Description
<h1>InstantNGP (Neural Graphics Primitives)</h1>

<p>Ever wanted to train a NeRF model of a fox in under 5 seconds? Or fly around a scene captured from photos of a factory robot? Of course you have! NVIDIA InstantNGP (iNGP) allows you to work with four neural graphics primitives: neural radiance fields (NeRF), signed distance functions (SDFs), neural images, and neural volumes. In each case, we train and render a MLP with multiresolution hash input encoding using the tiny-cuda-nnframework.</p>

<h2>Now with VR Support!</h2>
<p>The latest release of NVIDIA InstantNGP adds VR support for OpenXR based HMDs. This allows live-action captured volumetric NeRF scenes to be explored in 6DoF VR. Also, one can directly edit NeRF scenes using a VR hand controller to modify digital environments by erasing objects in seconds.</p>

<p>Pre-trained NeRF models can be shared with others using the drag and drop compatible &quot;.ingp&quot; based single file deliverable asset format. This technique uses a scene snapshot to containerize NeRF assets into a compact format that can be loaded and saved on demand.</p>

<h2>Open Source License</h2>
<p>InstantNGP is covered by a <a href="https://github.com/NVlabs/instant-ngp/blob/master/LICENSE.txt">NVIDIA Source Code License</a>. Please contact the <a href="https://www.nvidia.com/en-us/research/inquiries/">NVIDIA Research Licensing</a> team for more information about commercial usage of this technology in film & TV production.</p>

<h2>Compatibility</h2>
<p>This atom package provides a Windows 10 & 11 compatible build of NVIDIA InstantNGP that works with NVIDIA GeForce RTX 3000 and 4000 series GPUs. If you have an earlier NVIDIA GeForce or Quadro RTX GPU model, you can download a custom build of InstantNGP for that exact chipset from the <a href="https://github.com/NVlabs/instant-ngp#windows-binary-release">Windows Binary Release</a> section on the InstantNGP project's GitHub repo page.

<h2>Atom Packaging</h2>
<p>The Reactor Package Manager based atom package distribution of InstantNGP for Resolve/Fusion is maintained by the Kartaverse developer <a href="mailto:andrew@andrewhazelden.com">Andrew Hazelden</a>.</p>

<h2>For More Info</h2>
<h3>NVIDIA Resources</h3>
<ul>
  <li><a href="https://www.youtube.com/watch?v=DJ2hcC1orc4">YouTube | NVIDIA Instant NeRF: NVIDIA Research Turns 2D Photos Into 3D Scenes in the Blink of an AI</a></li>
  <li><a href="https://github.com/NVlabs/instant-ngp">GitHub | NVIDIA InstantNGP Repo</a></li>
  <li><a href="https://developer.nvidia.com/blog/getting-started-with-nvidia-instant-nerfs/">NVIDIA | Getting Started with NVIDIA Instant NeRFs</a></li>
</ul>
<h3>3rd Party NeRF Resources</h3>
<ul>
  <li><a href="https://docs.nerf.studio/en/latest/">NeRF Studio</a> + <a href="https://docs.nerf.studio/en/latest/quickstart/blender_addon.html">Blender VFX add-on<</a></li>
  <li><a href="https://docs.google.com/document/d/1vouz5gYpIw7bUBAGfAvPNcvNQoAfY_E7BhUJOGtV2cw/edit">Google Docs | Kartaverse Workflows | Creating Volumetric NeRFs</a></li>
  <li><a href="https://docs.google.com/document/d/15nnPfSXPTwNpovGxr_mRZncRoSfjmYqFoh08CHbNVVY/edit">Google Docs | InstantNGP | Best Practices For Desktop-Based NeRF Workflows</a></li>
</ul>

___

## Dependencies

## Deploy

### Common (No Architecture)


### Windows

> Bin/Win/InstantNGP/LICENSE.txt  
> Bin/Win/InstantNGP/README.md  
> Bin/Win/InstantNGP/configs/image/base.json  
> Bin/Win/InstantNGP/configs/image/frequency.json  
> Bin/Win/InstantNGP/configs/image/hashgrid.json  
> Bin/Win/InstantNGP/configs/image/oneblob.json  
> Bin/Win/InstantNGP/configs/nerf/base.json  
> Bin/Win/InstantNGP/configs/nerf/base_0layer.json  
> Bin/Win/InstantNGP/configs/nerf/base_14.json  
> Bin/Win/InstantNGP/configs/nerf/base_1layer.json  
> Bin/Win/InstantNGP/configs/nerf/base_2layer.json  
> Bin/Win/InstantNGP/configs/nerf/base_3layer.json  
> Bin/Win/InstantNGP/configs/nerf/big.json  
> Bin/Win/InstantNGP/configs/nerf/densegrid.json  
> Bin/Win/InstantNGP/configs/nerf/densegrid_1res.json  
> Bin/Win/InstantNGP/configs/nerf/frequency.json  
> Bin/Win/InstantNGP/configs/nerf/hashgrid.json  
> Bin/Win/InstantNGP/configs/nerf/linear.json  
> Bin/Win/InstantNGP/configs/nerf/none.json  
> Bin/Win/InstantNGP/configs/nerf/small.json  
> Bin/Win/InstantNGP/configs/nerf/tensor.json  
> Bin/Win/InstantNGP/configs/sdf/base.json  
> Bin/Win/InstantNGP/configs/sdf/frequency.json  
> Bin/Win/InstantNGP/configs/sdf/hashgrid.json  
> Bin/Win/InstantNGP/configs/sdf/oneblob.json  
> Bin/Win/InstantNGP/configs/sdf/takikawa.json  
> Bin/Win/InstantNGP/configs/volume/base.json  
> Bin/Win/InstantNGP/cudart64_110.dll  
> Bin/Win/InstantNGP/data/image/LICENSE.txt  
> Bin/Win/InstantNGP/data/image/albert.exr  
> Bin/Win/InstantNGP/data/nerf/fox/images/0001.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0002.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0003.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0004.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0006.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0007.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0008.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0009.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0012.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0014.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0018.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0019.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0021.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0022.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0025.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0026.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0027.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0029.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0030.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0031.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0033.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0034.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0035.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0039.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0042.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0044.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0045.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0046.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0049.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0052.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0054.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0072.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0073.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0074.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0076.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0077.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0078.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0081.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0084.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0085.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0089.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0090.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0094.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0097.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0103.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0105.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0107.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0108.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0110.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/images/0115.jpg  
> Bin/Win/InstantNGP/data/nerf/fox/transforms.json  
> Bin/Win/InstantNGP/data/sdf/armadillo.obj  
> Bin/Win/InstantNGP/data/sdf/bunny.obj  
> Bin/Win/InstantNGP/docs/assets_readme/albert.png  
> Bin/Win/InstantNGP/docs/assets_readme/armadillo.png  
> Bin/Win/InstantNGP/docs/assets_readme/cloud.png  
> Bin/Win/InstantNGP/docs/assets_readme/fox-representative.png  
> Bin/Win/InstantNGP/docs/assets_readme/fox.gif  
> Bin/Win/InstantNGP/docs/assets_readme/fox.png  
> Bin/Win/InstantNGP/docs/assets_readme/robot5.gif  
> Bin/Win/InstantNGP/docs/assets_readme/testbed.png  
> Bin/Win/InstantNGP/docs/nerf_dataset_tips.md  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/COLMAP.bat  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/RUN_TESTS.bat  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/absolute_pose_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/affine_transform_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/bitmap_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/bundle_adjustment_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/cache_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/camera_database_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/camera_models_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/camera_rig_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/camera_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/colmap.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/combination_sampler_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/consistency_graph_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/coordinate_frame_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/correspondence_graph_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/cost_functions_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/database_cache_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/database_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/depth_map_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/endian_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/essential_matrix_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/essential_matrix_utils_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/estimators_utils_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/feature_utils_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/fundamental_matrix_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/generalized_absolute_pose_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/generalized_relative_pose_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/geometry_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/gps_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/graph_cut_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/homography_matrix_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/homography_matrix_utils_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/image_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/inverted_file_entry_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/least_absolute_deviations_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/line_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/loransac_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/mat_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/math_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/matrix_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/misc_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/normal_map_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/opengl_utils_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/point2d_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/point3d_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/polynomial_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/pose_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/progressive_sampler_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/projection_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/random_sampler_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/random_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/ransac_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/reconstruction_manager_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/reconstruction_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/scene_clustering_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/sift_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/similarity_transform_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/string_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/support_measurement_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/threading_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/timer_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/track_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/translation_transform_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/triangulation_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/two_view_geometry_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/types_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/undistortion_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/visibility_pyramid_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/visual_index_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/bin/warp_test.exe  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/FreeImage.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/Half-2_5.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/Iex-2_5.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/IlmImf-2_5.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/IlmThread-2_5.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/Imath-2_5.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/Qt5Core.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/Qt5Gui.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/Qt5Svg.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/Qt5Widgets.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/boost_filesystem-vc143-mt-x64-1_77.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/boost_program_options-vc143-mt-x64-1_77.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/boost_unit_test_framework-vc143-mt-x64-1_77.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/brotlicommon.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/brotlidec.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/bz2.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/ceres.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/freetype.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/gflags.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/glew32.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/glog.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/gmp.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/harfbuzz.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/icudt69.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/icuin69.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/icuuc69.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/jasper.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/jpeg62.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/lcms2.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libamd.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libcamd.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libccolamd.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libcholmod.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libcolamd.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libgcc_s_seh-1.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libgfortran-5.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/liblapack.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libpng16.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libquadmath-0.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libspqr.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libwebpmux.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/libwinpthread-1.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/lzma.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/openblas.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/openjp2.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/pcre2-16.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/iconengines/qsvgicon.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qgif.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qicns.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qico.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qjp2.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qjpeg.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qsvg.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qtga.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qtiff.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qwbmp.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/imageformats/qwebp.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/platforms/qwindows.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/plugins/styles/qwindowsvistastyle.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/raw.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/tiff.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/webp.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/webpdecoder.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/webpdemux.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/zlib1.dll  
> Bin/Win/InstantNGP/external/colmap/COLMAP-3.7-windows-no-cuda/lib/zstd.dll  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/LICENSE  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/README.txt  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/bin/ffmpeg.exe  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/bin/ffplay.exe  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/bin/ffprobe.exe  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/bootstrap.min.css  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/default.css  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/developer.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/faq.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/fate.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-all.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-bitstream-filters.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-codecs.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-devices.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-filters.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-formats.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-protocols.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-resampler.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-scaler.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg-utils.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffmpeg.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffplay-all.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffplay.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffprobe-all.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/ffprobe.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/general.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/git-howto.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/libavcodec.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/libavdevice.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/libavfilter.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/libavformat.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/libavutil.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/libswresample.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/libswscale.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/mailing-list-faq.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/nut.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/platform.html  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/doc/style.min.css  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/presets/libvpx-1080p.ffpreset  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/presets/libvpx-1080p50_60.ffpreset  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/presets/libvpx-360p.ffpreset  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/presets/libvpx-720p.ffpreset  
> Bin/Win/InstantNGP/external/ffmpeg/ffmpeg-5.1.2-essentials_build/presets/libvpx-720p50_60.ffpreset  
> Bin/Win/InstantNGP/instant-ngp.exe  
> Bin/Win/InstantNGP/nvngx_dlss.dll  
> Bin/Win/InstantNGP/requirements.txt  
> Bin/Win/InstantNGP/scripts/category2id.json  
> Bin/Win/InstantNGP/scripts/colmap2nerf.py  
> Bin/Win/InstantNGP/scripts/common.py  
> Bin/Win/InstantNGP/scripts/convert_image.py  
> Bin/Win/InstantNGP/scripts/download_colmap.bat  
> Bin/Win/InstantNGP/scripts/download_ffmpeg.bat  
> Bin/Win/InstantNGP/scripts/flip/__init__.py  
> Bin/Win/InstantNGP/scripts/flip/main.py  
> Bin/Win/InstantNGP/scripts/flip/utils.py  
> Bin/Win/InstantNGP/scripts/nsvf2nerf.py  
> Bin/Win/InstantNGP/scripts/record3d2nerf.py  
