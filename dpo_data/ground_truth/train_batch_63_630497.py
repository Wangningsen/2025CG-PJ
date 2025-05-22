import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-53))
r=w0.sketch().segment((-95,-37),(-8,-37)).segment((-8,-81)).segment((43,-81)).arc((66,-100),(89,-81)).segment((95,-81)).segment((95,33)).segment((81,33)).arc((21,100),(-41,35)).segment((-95,35)).close().assemble().finalize().extrude(107)