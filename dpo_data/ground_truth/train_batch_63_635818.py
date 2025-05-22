import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.sketch().segment((-34,4),(-12,-13)).arc((1,-31),(21,-40)).segment((57,-69)).segment((100,-16)).segment((64,13)).arc((51,31),(31,40)).segment((-6,69)).segment((-32,37)).arc((-100,25),(-34,4)).assemble().finalize().extrude(99)