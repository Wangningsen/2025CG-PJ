import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
w1=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.sketch().rect(126,118).reset().face(w0.sketch().segment((-28,-16),(31,-32)).segment((34,-20)).segment((-25,-3)).close().assemble(),mode='s').finalize().extrude(-80).union(w1.workplane(offset=80/2).cylinder(80,100))