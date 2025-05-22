import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.sketch().segment((-100,-59),(20,-59)).segment((20,-4)).arc((100,16),(20,37)).segment((20,47)).segment((-100,47)).close().assemble().push([(-40,15.5)]).rect(42,9,mode='s').push([(-20.5,-49.5)]).rect(3,5,mode='s').finalize().extrude(18)