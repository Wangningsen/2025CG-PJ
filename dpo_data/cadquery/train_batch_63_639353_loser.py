import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.workplane(offset=-76/2).moveTo(-82,59).cylinder(76,18).union(w0.workplane(offset=-74/2).moveTo(58,-35).cylinder(74,42))