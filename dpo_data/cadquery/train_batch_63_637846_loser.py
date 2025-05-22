import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-43,-17),(-24,-17)).segment((-24,-54)).segment((24,-54)).segment((24,-17)).segment((43,-17)).segment((43,54)).arc((4,36),(-43,42)).close().assemble().finalize().extrude(-200)