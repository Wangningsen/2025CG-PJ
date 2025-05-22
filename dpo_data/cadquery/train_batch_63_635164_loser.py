import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,52))
w1=cq.Workplane('YZ',origin=(-12,0,0))
r=w0.sketch().segment((-31,-100),(21,-100)).segment((23,-81)).segment((72,-100)).segment((72,-99)).segment((23,-85)).segment((41,11)).segment((-31,11)).close().assemble().finalize().extrude(-115).union(w1.sketch().push([(87,50)]).circle(13).push([(87,50.5)]).rect(10,13,mode='s').finalize().extrude(-60))