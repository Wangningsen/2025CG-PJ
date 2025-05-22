import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.sketch().segment((-22,-42),(22,-42)).segment((22,5)).segment((-22,5)).segment((-22,-27)).segment((-20,-27)).segment((-20,-29)).segment((-22,-29)).close().assemble().push([(-8,-22.5)]).rect(2,5,mode='s').finalize().extrude(-75).union(w0.workplane(offset=125/2).cylinder(125,60))