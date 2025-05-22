import cadquery as cq
w0=cq.Workplane('YZ',origin=(51,0,0))
r=w0.workplane(offset=-102/2).moveTo(91,-57.5).box(18,47,102).union(w0.sketch().push([(-63.5,70)]).rect(73,22).push([(-63.5,70.5)]).rect(7,15,mode='s').finalize().extrude(-94))