import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
r=w0.sketch().arc((-33,-15),(-34,-99),(4,-24)).arc((20,98),(-33,-15)).assemble().finalize().extrude(-38)