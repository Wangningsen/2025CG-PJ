import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
r=w0.workplane(offset=-72/2).moveTo(38,10).cylinder(72,62).union(w0.sketch().push([(-68.5,-6)]).rect(63,132).reset().face(w0.sketch().segment((-96,-1),(-43,-16)).segment((-41,-10)).segment((-94,5)).close().assemble(),mode='s').finalize().extrude(44))