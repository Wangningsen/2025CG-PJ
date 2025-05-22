import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,24,0))
r=w0.workplane(offset=-49/2).moveTo(-36,-55).cylinder(49,45).union(w0.sketch().arc((-5,-12),(14,-82),(27,-10)).arc((32,-5),(36,1)).arc((55,94),(-1,15)).arc((-11,2),(-5,-12)).assemble().finalize().extrude(-40))