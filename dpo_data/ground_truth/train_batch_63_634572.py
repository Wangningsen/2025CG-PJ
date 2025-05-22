import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,91,0))
r=w0.sketch().arc((73,-68),(70,-47),(90,-43)).arc((-83,56),(73,-68)).assemble().circle(31,mode='s').finalize().extrude(-181)