import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().segment((-50,-92),(-40,-92)).arc((0,-100),(40,-92)).segment((50,-92)).segment((50,-87)).arc((100,0),(50,87)).segment((50,92)).segment((40,92)).arc((0,100),(-40,92)).segment((-50,92)).segment((-50,87)).arc((-100,0),(-50,-87)).close().assemble().circle(19,mode='s').finalize().extrude(92)