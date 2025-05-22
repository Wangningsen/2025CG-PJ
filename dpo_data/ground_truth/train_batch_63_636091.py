import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-48,0))
w1=cq.Workplane('XY',origin=(0,0,-41))
r=w0.sketch().arc((-47,76),(-73,1),(6,10)).arc((29,83),(-47,76)).assemble().finalize().extrude(97).union(w1.workplane(offset=125/2).moveTo(-74,11).cylinder(125,26))