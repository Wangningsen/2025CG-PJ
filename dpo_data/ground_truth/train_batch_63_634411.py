import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,95,0))
r=w0.sketch().segment((-100,-15),(-98,-19)).arc((-93,-38),(-84,-55)).segment((-82,-59)).segment((-81,-59)).arc((38,-93),(99,15)).segment((100,15)).segment((98,19)).arc((93,38),(84,55)).segment((82,59)).segment((81,59)).arc((-38,93),(-99,-15)).close().assemble().finalize().extrude(-190)