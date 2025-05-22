import cadquery as cq
w0=cq.Workplane('YZ',origin=(50,0,0))
r=w0.workplane(offset=-101/2).moveTo(91,-57.5).box(18,47,101).union(w0.sketch().push([(-63.5,70)]).rect(73,22).rect(7,16,mode='s').finalize().extrude(-93))