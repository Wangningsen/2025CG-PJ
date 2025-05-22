import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().arc((-80,65),(-77,20),(-32,20)).arc((-12,86),(-80,65)).assemble().push([(-54,43)]).circle(5,mode='s').finalize().extrude(-45).union(w0.workplane(offset=19/2).moveTo(16,-54).cylinder(19,34)).union(w0.workplane(offset=48/2).moveTo(43,-55).cylinder(48,45))