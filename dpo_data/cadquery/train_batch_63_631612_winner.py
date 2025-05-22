import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
w1=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().push([(-16,-49)]).rect(64,70).push([(-22,-63)]).rect(26,4,mode='s').finalize().extrude(-40).union(w0.sketch().push([(-36,54)]).circle(46).push([(-37,58)]).rect(48,48,mode='s').finalize().extrude(-3)).union(w1.workplane(offset=-81/2).moveTo(42,-64).cylinder(81,36))