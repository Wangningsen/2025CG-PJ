import cadquery as cq
w0=cq.Workplane('YZ',origin=(50,0,0))
r=w0.workplane(offset=-101/2).moveTo(91,-57.5).box(18,47,101).union(w0.sketch().segment((-100,59),(-95,59)).arc((-94,61),(-93,59)).segment((-27,59)).segment((-27,81)).segment((-100,81)).close().assemble().push([(-63.5,70)]).rect(7,16,mode='s').finalize().extrude(-93))