import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
r=w0.workplane(offset=-160/2).moveTo(19,0).cylinder(160,82).union(w0.workplane(offset=-140/2).moveTo(-36,11).cylinder(140,64))