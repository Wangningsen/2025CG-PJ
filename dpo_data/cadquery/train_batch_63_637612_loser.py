import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
r=w0.workplane(offset=-76/2).moveTo(-91,-62).cylinder(76,8).union(w0.sketch().segment((-100,-16),(100,-16)).segment((100,-4)).segment((-38,-4)).segment((-38,70)).segment((-100,70)).close().assemble().finalize().extrude(-69))