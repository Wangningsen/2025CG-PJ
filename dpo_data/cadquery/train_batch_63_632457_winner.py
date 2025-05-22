import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-83,0))
r=w0.workplane(offset=77/2).moveTo(-77.5,63).box(45,70,77).union(w0.sketch().segment((58,-65),(88,-65)).segment((88,-98)).arc((93,-61),(58,-65)).assemble().finalize().extrude(167))