import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().segment((-39,-88),(-28,-88)).arc((2,-92),(31,-88)).segment((85,-88)).segment((85,-37)).arc((-30,87),(-39,-84)).close().assemble().finalize().extrude(-98).union(w0.sketch().segment((-86,-22),(-21,-22)).arc((25,-75),(64,-15)).segment((64,15)).segment((-86,15)).close().assemble().finalize().extrude(102))