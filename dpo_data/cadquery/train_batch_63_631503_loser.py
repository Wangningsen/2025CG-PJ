import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().segment((-100,-60),(10,-60)).segment((10,-54)).arc((84,-55),(84,21)).segment((80,70)).segment((1,62)).segment((3,44)).segment((-100,44)).close().assemble().push([(47,-28)]).circle(8,mode='s').finalize().extrude(-34)