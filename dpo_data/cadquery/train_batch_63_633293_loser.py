import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,29))
w1=cq.Workplane('XY',origin=(0,0,7))
r=w0.sketch().segment((-73,-67),(3,-83)).segment((25,13)).segment((-49,28)).close().assemble().push([(-24,-27)]).circle(3,mode='s').finalize().extrude(32).union(w0.workplane(offset=65/2).moveTo(71.5,-18.5).box(57,39,65)).union(w1.sketch().arc((-60,20),(-49,-85),(-21,16)).segment((-18,16)).segment((-18,13)).segment((19,13)).segment((19,85)).segment((-60,85)).close().assemble().push([(-22,-56)]).rect(46,18,mode='s').push([(-22,48)]).circle(2,mode='s').finalize().extrude(-101))