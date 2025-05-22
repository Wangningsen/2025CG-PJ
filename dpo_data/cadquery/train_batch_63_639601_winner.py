import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-41,0))
w1=cq.Workplane('XY',origin=(0,0,14))
r=w0.sketch().arc((-54,-44),(-19,-46),(13,-61)).segment((73,-61)).arc((64,-21),(31,6)).arc((-22,100),(-39,-11)).arc((-50,-26),(-54,-44)).assemble().finalize().extrude(103).union(w1.workplane(offset=-64/2).moveTo(-96,-59).cylinder(64,4))