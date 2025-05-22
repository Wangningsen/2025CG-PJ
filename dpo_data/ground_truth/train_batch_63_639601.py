import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,62,0))
w1=cq.Workplane('XY',origin=(0,0,14))
r=w0.sketch().arc((-54,-44),(-20,-46),(13,-61)).segment((73,-61)).arc((64,-22),(31,6)).arc((-29,98),(-39,-12)).arc((-50,-27),(-54,-44)).assemble().finalize().extrude(-103).union(w1.workplane(offset=-64/2).moveTo(-96,-58).cylinder(64,4))