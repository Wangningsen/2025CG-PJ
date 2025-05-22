import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,52))
r=w0.sketch().segment((-69,-88),(-5,-88)).segment((-5,-100)).segment((5,-100)).segment((5,-88)).segment((69,-88)).segment((69,88)).segment((5,88)).segment((5,100)).segment((-5,100)).segment((-5,88)).segment((-69,88)).close().assemble().finalize().extrude(-104).union(w0.workplane(offset=-101/2).box(148,70,101))