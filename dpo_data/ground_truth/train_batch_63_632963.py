import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-64))
r=w0.sketch().segment((-100,-92),(24,-92)).segment((44,-96)).segment((45,-92)).segment((100,-92)).segment((100,92)).segment((-24,92)).segment((-44,96)).segment((-45,92)).segment((-100,92)).close().assemble().finalize().extrude(128)