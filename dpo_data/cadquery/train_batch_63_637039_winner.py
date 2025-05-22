import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.sketch().segment((-100,-59),(20,-59)).segment((20,-6)).arc((100,16),(20,37)).segment((20,47)).segment((-100,47)).close().assemble().push([(-40,15.5)]).rect(42,9,mode='s').push([(-22,-48)]).circle(1,mode='s').finalize().extrude(18)