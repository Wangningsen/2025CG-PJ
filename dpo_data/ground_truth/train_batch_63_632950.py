import cadquery as cq
w0=cq.Workplane('YZ',origin=(-98,0,0))
r=w0.sketch().push([(0,-82)]).rect(160,36).push([(0,82)]).rect(160,36).finalize().extrude(197)