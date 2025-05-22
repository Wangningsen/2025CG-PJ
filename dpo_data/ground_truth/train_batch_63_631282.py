import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().segment((-38,-88),(-28,-88)).arc((0,-92),(28,-88)).segment((85,-88)).segment((85,-37)).arc((-33,86),(-38,-84)).close().assemble().finalize().extrude(-98).union(w0.sketch().segment((-86,-22),(-20,-22)).arc((27,-75),(64,-14)).segment((64,15)).segment((-86,15)).close().assemble().finalize().extrude(102))