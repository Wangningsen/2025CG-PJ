import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().circle(72).reset().face(w0.sketch().segment((-35,42),(-14,20)).arc((-14,-12),(15,-31)).segment((36,-53)).segment((38,-51)).segment((19,-30)).arc((17,8),(-17,27)).segment((-38,49)).close().assemble(),mode='s').finalize().extrude(-200)