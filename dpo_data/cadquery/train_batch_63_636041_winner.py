import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,16))
r=w0.sketch().segment((-100,8),(-95,-33)).segment((100,-8)).segment((95,33)).close().assemble().finalize().extrude(-32)