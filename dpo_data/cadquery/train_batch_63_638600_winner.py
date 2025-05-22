import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-73,0))
r=w0.workplane(offset=17/2).moveTo(46,0).cylinder(17,20).union(w0.workplane(offset=102/2).moveTo(-69.5,26).box(61,78,102)).union(w0.sketch().push([(46.5,0)]).rect(107,140).push([(46,0)]).circle(37,mode='s').finalize().extrude(145))