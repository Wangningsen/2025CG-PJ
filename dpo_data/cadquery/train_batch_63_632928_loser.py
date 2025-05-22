import cadquery as cq
w0=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.workplane(offset=-82/2).cylinder(82,34).union(w0.sketch().rect(42,78).reset().face(w0.sketch().segment((-13,-6),(10,-13)).segment((13,3)).segment((-10,9)).close().assemble(),mode='s').finalize().extrude(118))