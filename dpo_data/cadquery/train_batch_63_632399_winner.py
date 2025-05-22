import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.sketch().push([(-16,-73)]).circle(27).push([(18,75)]).circle(25).push([(12,74)]).circle(11,mode='s').finalize().extrude(46)