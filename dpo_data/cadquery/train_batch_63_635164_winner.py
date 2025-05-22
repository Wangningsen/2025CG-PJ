import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,52))
w1=cq.Workplane('YZ',origin=(-12,0,0))
r=w0.sketch().segment((-31,-100),(72,-100)).segment((59,-98)).segment((22,-91)).segment((41,11)).segment((-31,11)).close().assemble().finalize().extrude(-115).union(w1.sketch().push([(87,50)]).circle(13).circle(6,mode='s').finalize().extrude(-60))