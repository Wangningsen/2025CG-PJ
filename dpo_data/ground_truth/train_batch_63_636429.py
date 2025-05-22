import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('YZ',origin=(89,0,0))
r=w0.workplane(offset=-20/2).moveTo(29,-37).box(80,104,20).union(w0.workplane(offset=92/2).moveTo(-58.5,17.5).box(5,27,92)).union(w1.workplane(offset=-107/2).moveTo(-63,-31).box(74,76,107))