import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-24,0))
w1=cq.Workplane('XY',origin=(0,0,71))
r=w0.sketch().segment((79,44),(88,44)).arc((83,56),(79,69)).close().assemble().finalize().extrude(-25).union(w1.sketch().segment((-100,-59),(-9,-59)).segment((-9,-64)).segment((73,-64)).segment((73,-58)).segment((5,-58)).segment((5,53)).segment((100,53)).segment((100,59)).segment((5,59)).segment((5,64)).segment((-100,64)).close().assemble().push([(-82,44)]).circle(4,mode='s').finalize().extrude(-159))