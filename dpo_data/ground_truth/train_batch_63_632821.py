import cadquery as cq
w0=cq.Workplane('YZ',origin=(-56,0,0))
r=w0.sketch().arc((-33,-4),(-100,-42),(-29,-73)).arc((-8,-65),(3,-44)).arc((27,-47),(46,-33)).arc((65,-25),(81,-10)).segment((100,-10)).segment((100,26)).segment((92,26)).arc((16,80),(-17,-7)).arc((-25,-4),(-33,-4)).assemble().finalize().extrude(113)