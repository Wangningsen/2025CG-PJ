import cadquery as cq
w0=cq.Workplane('YZ',origin=(-54,0,0))
r=w0.sketch().segment((-100,26),(-87,47)).segment((-92,46)).arc((-96,38),(-100,26)).assemble().finalize().extrude(100).union(w0.workplane(offset=108/2).moveTo(90,-36).cylinder(108,10))