import cadquery as cq
w0=cq.Workplane('YZ',origin=(59,0,0))
r=w0.workplane(offset=-119/2).moveTo(-53,0).box(12,114,119).union(w0.sketch().push([(-88,4.5)]).rect(24,29).push([(68,37)]).rect(64,34).push([(78.5,26)]).rect(7,12,mode='s').finalize().extrude(-31))