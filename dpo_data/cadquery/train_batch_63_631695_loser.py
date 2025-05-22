import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,53))
r=w0.workplane(offset=-106/2).moveTo(-77,-2).cylinder(106,13).union(w0.workplane(offset=-42/2).moveTo(-41,44).cylinder(42,56)).union(w0.workplane(offset=-4/2).moveTo(43,-54).cylinder(4,46))