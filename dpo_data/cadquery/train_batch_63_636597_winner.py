import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-22))
w1=cq.Workplane('ZX',origin=(0,-20,0))
r=w0.sketch().push([(77,14)]).circle(23).circle(20,mode='s').circle(5).finalize().extrude(-42).union(w0.sketch().segment((-46,-2),(-28,-2)).segment((-28,-34)).segment((54,-34)).segment((54,55)).segment((36,55)).segment((36,86)).segment((-46,86)).close().assemble().finalize().extrude(60)).union(w1.sketch().segment((29,-100),(64,-100)).segment((64,-90)).arc((46,-96),(29,-90)).close().assemble().finalize().extrude(-66))