import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,59))
w1=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().arc((-40,73),(-100,-2),(-32,-75)).segment((-32,-71)).segment((-24,-71)).segment((-24,-72)).arc((51,-10),(-12,74)).arc((-26,71),(-40,73)).assemble().finalize().extrude(-118).union(w1.workplane(offset=-92/2).moveTo(-29,84).cylinder(92,16))