import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
r=w0.sketch().segment((-49,-20),(-42,-25)).segment((-42,-100)).segment((42,-100)).segment((42,10)).segment((49,20)).segment((42,25)).segment((42,100)).segment((-42,100)).segment((-42,-10)).close().assemble().finalize().extrude(83)