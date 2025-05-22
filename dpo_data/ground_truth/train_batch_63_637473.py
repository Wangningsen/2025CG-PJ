import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,43))
r=w0.workplane(offset=-114/2).moveTo(-13.5,36.5).box(119,127,114).union(w0.sketch().segment((-18,-63),(-11,-100)).segment((17,-95)).segment((17,-72)).segment((45,-72)).segment((45,-90)).segment((73,-85)).segment((67,-48)).close().assemble().finalize().extrude(28))