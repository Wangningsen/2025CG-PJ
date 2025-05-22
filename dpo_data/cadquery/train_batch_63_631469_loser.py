import cadquery as cq
w0=cq.Workplane('YZ',origin=(77,0,0))
r=w0.workplane(offset=-154/2).moveTo(-79,38).cylinder(154,21).union(w0.sketch().push([(72.5,-10.5)]).rect(55,97).push([(54,15)]).circle(1,mode='s').finalize().extrude(-19))