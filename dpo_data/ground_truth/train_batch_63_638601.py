import cadquery as cq
w0=cq.Workplane('YZ',origin=(44,0,0))
w1=cq.Workplane('XY',origin=(0,0,71))
r=w0.workplane(offset=24/2).moveTo(-36.5,83.5).box(25,9,24).union(w1.sketch().segment((-100,-59),(-9,-59)).segment((-9,-64)).segment((73,-64)).segment((73,-58)).segment((5,-58)).segment((5,53)).segment((100,53)).segment((100,59)).segment((5,59)).segment((5,64)).segment((-100,64)).close().assemble().push([(-86,44)]).circle(7,mode='s').finalize().extrude(-159))