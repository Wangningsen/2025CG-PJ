import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-22,-62),(22,-62)).segment((22,-54)).arc((58,0),(22,54)).segment((22,62)).segment((-22,62)).segment((-22,54)).arc((-58,0),(-22,-54)).close().assemble().circle(19,mode='s').finalize().extrude(200)