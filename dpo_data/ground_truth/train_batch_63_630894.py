import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-55,0))
w1=cq.Workplane('YZ',origin=(-64,0,0))
r=w0.sketch().push([(56.5,-81.5)]).rect(11,11).push([(94.5,-81.5)]).rect(11,11).finalize().extrude(78).union(w1.workplane(offset=151/2).moveTo(36.5,-21.5).box(37,157,151))