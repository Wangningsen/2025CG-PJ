import cadquery as cq
w0=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.sketch().push([(33.5,20.5)]).rect(83,135).push([(19,39.5)]).rect(58,21,mode='s').push([(33,21)]).circle(15,mode='s').finalize().extrude(-73).union(w0.workplane(offset=127/2).moveTo(-22.5,-78.5).box(105,19,127))