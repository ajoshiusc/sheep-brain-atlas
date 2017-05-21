# -*- coding: utf-8 -*-

import vtk
from surfproc import vtkpoly2Surf, view_patch_vtk, patch_color_attrib, reducepatch
from dfsio import writedfs
from nilearn import image
import scipy as sp

#%% Convert Surface Files
filename = "/deneb_disk/sheep_brain/surf_stl.binary/ovine_model_wm_surf.stl"
outfile = "/deneb_disk/sheep_brain/surf_stl.binary/ovine_model_wm_surf.dfs"
reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
reader.Update()
s = vtkpoly2Surf(reader.GetOutput())
patch_color_attrib(s=s, values=s.vertices[:, 1])
print(s.faces.shape, s.vertices.shape)
s = reducepatch(surf=s, ratio=1.0)
print(s.faces.shape, s.vertices.shape)

patch_color_attrib(s=s, values=s.vertices[:, 1])

view_patch_vtk(s)

writedfs(outfile, s)

#%
gm = image.load_img('/deneb_disk/sheep_brain/NIFTI_ovine_025mm/grey.nii')
wm = image.load_img('/deneb_disk/sheep_brain/NIFTI_ovine_025mm/white.nii')
csf = image.load_img('/deneb_disk/sheep_brain/NIFTI_ovine_025mm/csf.nii')


pvc_frac = image.new_img_like(gm,csf.get_data()+2*gm.get_data()+3*wm.get_data())

pvc_frac.to_filename('/deneb_disk/sheep_brain/NIFTI_ovine_025mm/\
sheep.pvc.frac.nii.gz')



