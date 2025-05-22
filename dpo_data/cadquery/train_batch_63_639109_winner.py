import cadquery as cq
w0=cq.Workplane('YZ',origin=(-62,0,0))
r=w0.workplane(offset=31/2).moveTo(-64,-77).cylinder(31,7).union(w0.sketch().push([(68.5,0)]).rect(5,200).push([(69,33)]).circle(2,mode='s').finalize().extrude(124))