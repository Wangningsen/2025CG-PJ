import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,82))
w1=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.sketch().segment((-95,-28),(-75,-28)).segment((-75,-48)).segment((-21,-48)).segment((-21,-28)).segment((24,-28)).segment((24,26)).segment((-21,26)).segment((-21,48)).segment((-75,48)).segment((-75,26)).segment((-95,26)).close().assemble().finalize().extrude(-12).union(w1.sketch().segment((-100,46),(-29,46)).arc((94,3),(-21,65)).segment((-100,65)).close().assemble().push([(-51,55)]).circle(8,mode='s').push([(34.5,29)]).rect(11,70,mode='s').finalize().extrude(-38))