import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,41))
r=w0.workplane(offset=-82/2).moveTo(66,0).cylinder(82,34).union(w0.workplane(offset=-30/2).moveTo(-94,14).cylinder(30,6))