import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
r=w0.sketch().segment((-62,86),(-59,62)).arc((-84,-12),(-40,-75)).segment((-36,-100)).segment((62,-86)).segment((59,-62)).arc((84,12),(40,75)).segment((36,100)).close().assemble().circle(84,mode='s').finalize().extrude(71)