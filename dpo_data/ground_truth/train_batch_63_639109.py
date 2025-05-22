import cadquery as cq
w0=cq.Workplane('YZ',origin=(-61,0,0))
r=w0.workplane(offset=30/2).moveTo(-64,-77).cylinder(30,7).union(w0.sketch().push([(68.5,0)]).rect(5,200).push([(69,32.5)]).rect(2,3,mode='s').finalize().extrude(123))