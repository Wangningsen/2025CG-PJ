import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,81,0))
r=w0.sketch().segment((-90,-92),(-40,-92)).arc((0,-100),(40,-92)).segment((90,-92)).segment((90,-45)).arc((100,0),(90,45)).segment((90,92)).segment((40,92)).arc((0,100),(-40,92)).segment((-90,92)).segment((-90,45)).arc((-100,0),(-90,-45)).close().assemble().finalize().extrude(-162)