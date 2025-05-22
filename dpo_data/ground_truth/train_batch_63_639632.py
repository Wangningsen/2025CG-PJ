import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.workplane(offset=-92/2).moveTo(12.5,-61.5).box(97,35,92).union(w0.workplane(offset=-33/2).moveTo(-25,43).cylinder(33,36)).union(w0.sketch().segment((6,29),(9,46)).segment((6,47)).close().assemble().finalize().extrude(108))