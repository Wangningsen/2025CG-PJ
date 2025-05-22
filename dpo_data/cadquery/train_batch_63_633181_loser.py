import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,87))
r=w0.workplane(offset=-174/2).moveTo(-13.5,0.5).box(173,169,174).union(w0.workplane(offset=-171/2).moveTo(41,-16).cylinder(171,59))