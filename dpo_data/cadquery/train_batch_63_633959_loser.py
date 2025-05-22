import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-11))
w1=cq.Workplane('XY',origin=(0,0,-10))
r=w0.sketch().push([(-29,22)]).circle(10).push([(-37,23)]).circle(1,mode='s').finalize().extrude(-18).union(w0.workplane(offset=39/2).moveTo(50,-79).cylinder(39,5)).union(w1.sketch().segment((-100,37),(-67,-40)).segment((15,-6)).arc((58,53),(95,-5)).segment((100,-5)).segment((100,60)).segment((16,60)).segment((16,64)).segment((12,64)).segment((12,84)).close().assemble().finalize().extrude(38))