import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
r=w0.workplane(offset=-18/2).moveTo(-49,2).box(86,74,18).union(w0.sketch().arc((-21,-39),(-17,-44),(-15,-49)).segment((16,-49)).arc((99,11),(-2,30)).segment((-9,30)).arc((-99,13),(-21,-39)).assemble().finalize().extrude(79))