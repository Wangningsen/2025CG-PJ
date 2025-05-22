import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,94,0))
r=w0.sketch().segment((-85,16),(-63,16)).segment((-63,20)).segment((-13,20)).arc((66,-16),(-20,-3)).segment((-52,-3)).segment((-52,-100)).segment((61,-100)).segment((61,-71)).segment((85,-71)).segment((85,100)).segment((-85,100)).close().assemble().finalize().extrude(-189)