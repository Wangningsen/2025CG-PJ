import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
r=w0.workplane(offset=-37/2).moveTo(-13,12).cylinder(37,5).union(w0.sketch().arc((-31,22),(57,19),(79,-65)).arc((84,30),(-11,43)).segment((-11,65)).segment((-15,65)).segment((-15,39)).arc((-24,31),(-31,22)).assemble().finalize().extrude(-14)).union(w0.workplane(offset=36/2).moveTo(-91,-53).cylinder(36,9))