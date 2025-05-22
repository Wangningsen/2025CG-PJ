import cadquery as cq
w0=cq.Workplane('YZ',origin=(-39,0,0))
w1=cq.Workplane('XY',origin=(0,0,0))
r=w0.workplane(offset=-46/2).moveTo(-14,24).cylinder(46,6).union(w0.workplane(offset=124/2).moveTo(26.5,42.5).box(39,115,124)).union(w1.sketch().push([(-10.5,-14.5)]).rect(75,63).push([(-2.5,-33)]).rect(15,10,mode='s').finalize().extrude(-100))