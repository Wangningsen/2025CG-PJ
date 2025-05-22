import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
r=w0.sketch().push([(12.5,-61.5)]).rect(67,75).push([(26,-39)]).circle(2,mode='s').finalize().extrude(-95).union(w0.workplane(offset=105/2).moveTo(0,44).cylinder(105,55))