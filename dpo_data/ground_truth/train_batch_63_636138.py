import cadquery as cq
w0=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.sketch().segment((-22,-100),(22,-100)).segment((22,-90)).arc((93,0),(22,90)).segment((22,100)).segment((-22,100)).segment((-22,90)).arc((-93,0),(-22,-90)).close().assemble().finalize().extrude(119)