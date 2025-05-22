import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-40))
r=w0.workplane(offset=-25/2).moveTo(59.5,-30).box(43,88,25).union(w0.sketch().push([(-62.5,34.5)]).rect(75,79).push([(73,10)]).circle(27).push([(73.5,9.5)]).rect(49,17,mode='s').finalize().extrude(105))