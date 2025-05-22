import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,49,0))
r=w0.sketch().segment((-35,3),(-15,-11)).arc((-2,-28),(18,-39)).segment((57,-69)).segment((100,-15)).segment((65,12)).arc((54,29),(34,39)).segment((-6,69)).segment((-32,37)).arc((-100,22),(-35,3)).assemble().finalize().extrude(-98)