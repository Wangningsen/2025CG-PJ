import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-55,-21),(17,-21)).segment((17,-71)).segment((55,-71)).segment((55,71)).segment((-55,71)).close().assemble().finalize().extrude(-200)