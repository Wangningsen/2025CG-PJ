import cadquery as cq
w0=cq.Workplane('YZ',origin=(46,0,0))
r=w0.sketch().segment((-50,-97),(-19,-97)).arc((0,-99),(19,-97)).segment((50,-97)).segment((50,-86)).arc((100,0),(50,86)).segment((50,63)).segment((-13,56)).segment((-19,99)).segment((-50,99)).segment((-50,86)).arc((-100,0),(-50,-86)).close().assemble().finalize().extrude(-92)