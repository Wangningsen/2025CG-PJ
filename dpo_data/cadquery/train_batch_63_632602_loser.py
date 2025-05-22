import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,64,0))
r=w0.sketch().push([(-13.5,-72)]).rect(75,56).push([(-3,-79)]).circle(2,mode='s').push([(13,62)]).circle(38).finalize().extrude(-128).union(w0.workplane(offset=-15/2).moveTo(-19.5,0).box(55,84,15))