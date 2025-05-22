import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
r=w0.sketch().arc((-70,67),(-68,-58),(53,-23)).segment((53,-84)).segment((100,-84)).segment((100,27)).segment((55,27)).arc((7,79),(-65,71)).segment((-60,68)).segment((-63,63)).close().assemble().push([(21,10)]).circle(20,mode='s').finalize().extrude(12)