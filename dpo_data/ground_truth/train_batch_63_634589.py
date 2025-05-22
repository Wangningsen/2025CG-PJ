import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().segment((-86,-49),(-68,-49)).arc((-16,-96),(-18,-27)).segment((-18,-20)).segment((11,-20)).segment((11,12)).segment((-18,12)).segment((-18,66)).segment((-86,66)).close().assemble().push([(-52,8)]).circle(21,mode='s').finalize().extrude(-122).union(w0.workplane(offset=-103/2).moveTo(78,92).cylinder(103,8))