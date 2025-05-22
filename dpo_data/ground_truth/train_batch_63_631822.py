import cadquery as cq
w0=cq.Workplane('YZ',origin=(-54,0,0))
r=w0.sketch().arc((-100,26),(-94,36),(-87,47)).segment((-92,47)).arc((-97,36),(-100,26)).assemble().finalize().extrude(100).union(w0.workplane(offset=108/2).moveTo(90,-36).cylinder(108,10))