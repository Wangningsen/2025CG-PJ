import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-27,0))
r=w0.workplane(offset=3/2).moveTo(-75,31).cylinder(3,25).union(w0.sketch().arc((100,-54),(99,-53),(100,-52)).arc((96,-54),(100,-54)).assemble().finalize().extrude(11)).union(w0.workplane(offset=55/2).moveTo(0.5,-33.5).box(3,37,55))