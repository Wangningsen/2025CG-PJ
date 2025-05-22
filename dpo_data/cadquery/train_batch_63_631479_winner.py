import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,1))
r=w0.sketch().segment((-23,-100),(-8,-100)).segment((-8,-58)).segment((-23,-58)).segment((-23,-77)).arc((-24,-80),(-23,-83)).close().assemble().push([(6,82)]).circle(18).push([(2,89)]).circle(1,mode='s').finalize().extrude(-2)