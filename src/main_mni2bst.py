# -*- coding: utf-8 -*-

import vtk
from surfproc import vtkpoly2Surf, view_patch_vtk, patch_color_attrib, reducepatch
from dfsio import writedfs


filename = "/deneb_disk/sheep_brain/surf_stl.binary/ovine_model_gm_surf.stl"
outfile = "/deneb_disk/sheep_brain/surf_stl.binary/ovine_model_gm_surf.dfs"
reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
reader.Update()
s = vtkpoly2Surf(reader.GetOutput())
patch_color_attrib(s=s, values=s.vertices[:, 1])
print s.faces.shape, s.vertices.shape
#s = reducepatch(surf=s, ratio=1.0)
print s.faces.shape, s.vertices.shape

patch_color_attrib(s=s, values=s.vertices[:, 1])

view_patch_vtk(s)

writedfs(outfile, s)
