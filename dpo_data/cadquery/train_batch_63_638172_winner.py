import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
w1=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.workplane(offset=125/2).cylinder(125,60).union(w1.sketch().arc((-100,-1),(-94,-12),(-87,-22)).segment((82,-22)).segment((82,22)).segment((-100,22)).close().assemble().finalize().extrude(47))