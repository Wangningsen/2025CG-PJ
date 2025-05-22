import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.sketch().segment((-83,-49),(-55,-49)).segment((-55,-100)).segment((55,-100)).segment((55,-49)).segment((83,-49)).segment((83,49)).segment((55,49)).segment((55,100)).segment((-55,100)).segment((-55,49)).segment((-83,49)).close().assemble().circle(68,mode='s').finalize().extrude(14)