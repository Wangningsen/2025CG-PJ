import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
w1=cq.Workplane('XY',origin=(0,0,23))
r=w0.workplane(offset=-46/2).moveTo(59,-59).cylinder(46,41).union(w0.sketch().push([(-86,-20)]).circle(14).push([(-86,-20.5)]).rect(18,7,mode='s').finalize().extrude(109)).union(w1.workplane(offset=77/2).moveTo(-16,23).cylinder(77,34))