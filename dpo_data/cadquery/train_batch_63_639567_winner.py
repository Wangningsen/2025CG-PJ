import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,24,0))
r=w0.workplane(offset=-49/2).moveTo(-37,-55).cylinder(49,45).union(w0.sketch().arc((5,8),(2,-82),(31,1)).arc((41,99),(5,8)).assemble().finalize().extrude(-40))