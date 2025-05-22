import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
r=w0.workplane(offset=-72/2).moveTo(38,10).cylinder(72,62).union(w0.sketch().push([(-68.5,-6)]).rect(63,132).reset().face(w0.sketch().segment((-91,1),(-47,-16)).segment((-44,-8)).segment((-87,7)).close().assemble(),mode='s').finalize().extrude(44))