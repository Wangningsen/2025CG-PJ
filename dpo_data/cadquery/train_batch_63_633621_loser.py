import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-41,0))
r=w0.sketch().segment((-100,25),(-95,-34)).segment((-56,-30)).segment((-61,28)).close().assemble().finalize().extrude(-6).union(w0.workplane(offset=88/2).moveTo(45,0).cylinder(88,55))