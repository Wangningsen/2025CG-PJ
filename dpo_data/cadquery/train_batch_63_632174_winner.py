import cadquery as cq
w0=cq.Workplane('YZ',origin=(42,0,0))
r=w0.sketch().push([(1,-35.5)]).rect(26,129).push([(2,-35)]).circle(12,mode='s').finalize().extrude(-124).union(w0.workplane(offset=40/2).moveTo(0,68).cylinder(40,32))