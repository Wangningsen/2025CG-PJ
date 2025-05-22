import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,1,0))
r=w0.workplane(offset=-49/2).moveTo(-33,66).cylinder(49,34).union(w0.sketch().segment((-50,-15),(-47,-92)).segment((-7,-90)).arc((67,-59),(-3,-14)).close().assemble().push([(5.5,-71.5)]).rect(5,31,mode='s').finalize().extrude(47))